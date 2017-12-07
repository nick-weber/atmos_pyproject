#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing functions to manipulate/load atmospheric data, along with
additional tools.

@author: njweber2
"""
import numpy as np
from datetime import datetime
import os

def calculate_rh(t, td):
    """
    Given 1-D numpy arrays of temperature and dewpoint, calculates a timeseries
    of relative humidity values.
    
    Requires:
        t ---> a 1-D array of temperatures (floats)
        td --> a 1-D array of dewpoint temperatures(floats)
        
    Returns:
        rh --> a 1-D array of relative humidities (floats)
    """
    ######################################################################
    ### FILL IN THIS BLOCK ###############################################
    ######################################################################
    
    # TODO: Calculate RH!
    #       Hint: use the first two equations in the "Calculating the dew
    #       point" section on the Dew Point wikipedia page:
    #       https://en.wikipedia.org/wiki/Dew_point#Humidity
    
    # remove these two lines and write your own!
    print('calculate_rh(): YOU NEED TO WRITE THIS FUNCTION!')
    rh = np.nan
    
    ######################################################################
    ### END HERE #########################################################
    ######################################################################
    return rh



def load_narr_data(dt1, dt2, ncfile='narr_oct2010.nc'):
    """
    Loads temperature, pressure, wind, and OLR data from [ncfile], a pre-
    -processed netCDF of North American Regional Analysis (NARR) data. All
    times (3-hourly) between [dt1] and [dt2] are loaded.
    
    Requires:
        dt1 ------> starting time (datetime object)
        dt2 ------> ending time (datetime object)
        ncfile ---> pre-processed NARR netcdf filename (string)
        
    Returns:
        datadict -> a dictionary of numpy arrays containing the data in the
                    desired time range. The dictionary has the following keys:
                    ('dates', 'lats', 'lons', 't2m', 'mslp', 'u10m', 'v10m',
                     'olr')
    """
    from netCDF4 import Dataset, num2date
    
    # Get the directory that this module is located in
    thisdir = os.path.dirname(os.path.realpath(__file__))
    
    # Load the 2-meter temperature and mslp data from [ncfile]
    with Dataset(os.path.join(thisdir, 'data', ncfile), 'r') as ncdata:
        # Get the dates (which are floats w/ units of "hours since 1800-01-01")
        # and convert to datetime objects
        dates = ncdata.variables['time']
        dates = num2date(dates[:], dates.units)
        # Get the indices corresponding to [dt1] and [dt2]
        ti1 = nearest_ind(dates, dt1)
        ti2 = nearest_ind(dates, dt2) + 1
        dates = dates[ti1:ti2]
        
        # Get the latitudes and longitudes
        lats = ncdata.variables['lat'][:,:]
        lons = ncdata.variables['lon'][:,:]
        
        # Load the temperatures, pressures, winds, and precipitation
        t2m = ncdata.variables['t2m'][ti1:ti2, :, :] # in Celsius
        mslp = ncdata.variables['mslp'][ti1:ti2, :, :] # in hPa
        uwnd = ncdata.variables['u10m'][ti1:ti2, :, :] # in kts
        vwnd = ncdata.variables['v10m'][ti1:ti2, :, :] # in kts
        olr = ncdata.variables['olr'][ti1:ti2, :, :] # in W/m^2
        
    # Store all of the dimensions and data in a dictionary
    datadict = {'dates':dates, 'lats':lats, 'lons':lons, 't2m':t2m, 
                'mslp':mslp, 'u10m':uwnd, 'v10m':vwnd, 'olr':olr}
    return datadict



def get_meteorogram(stid, dt1, dt2):
    """
    Retrieves ASOS surface station data at the desired station and time range.
    
    Requires:
        stid --> the ASOS station ID (string; e.g., "ORD")
        dt1 ---> starting date/time (datetime object)
        dt2 ---> ending date/time (datetime object)
        
    Returns:
        datadict -> a dictionary of 1D numpy arrays containing the data in the
                    desired time range. The dictionary has the following keys:
                    ('dates', )
    """
    # Get the directory that this module is located in
    thisdir = os.path.dirname(os.path.realpath(__file__))
    # Get the full path to the sounding data
    asosfile = os.path.join(thisdir, 'data', 'asos_{}.txt'.format(stid))
    
    # Load the data from the sounding file
    try:
        data = np.genfromtxt(asosfile, dtype=str, delimiter=',', 
                             skip_header=1)
    except:
        raise ValueError('ERROR: station "{}" does not exist!'.format(stid))
        
    # Convert the date strings to datetime objects
    dates = np.array([datetime.strptime(dstr, '%Y-%m-%d %H:%M') for \
                      dstr in data[:,1]])
    # Get the indices for the dates within the desired date range
    t1 = nearest_ind(dates, dt1)
    t2 = nearest_ind(dates, dt2) + 1
    # Now select that subset of the dates (and all other variables)
    dates = dates[t1:t2]
    
    # Now get the other variables
    t = data[t1:t2, 2].astype(float)  # temperature in Celsius
    td = data[t1:t2, 3].astype(float)  # dewpoint in Celsius
    wdir = data[t1:t2, 4].astype(float) # wind direction in degrees
    wspd = data[t1:t2, 5].astype(float) # wind speed in knots
    # pressure in hPa:
    pres = np.array([float(x) if x!='M' else np.nan for x in data[t1:t2, 6]])
    # 1-hour precipitation in mm
    # pressure in hPa:
    prec = np.array([float(x) if x!='M' else 0. for x in data[t1:t2, 7]])

    # Return the data in a dictionary
    datadict = {'dates':dates, 't':t, 'td':td, 'wdir':wdir, 'wspd':wspd, 
                'pres':pres, 'prec':prec}
    return datadict



def get_sounding(stid, date):
    """
    Retrieves sounding data (temperature and dewpoint) at the desired 
    station and time.
    
    Requires:
        stid --> the radiosonde station ID (string; e.g., "KILX")
        date --> the desired sounding date/time (datetime object)
        
    Returns:
        datadict -> a dictionary of 1D numpy arrays containing the data in the
                    desired time range. The dictionary has the following keys:
                    ('date', 'p', 'z', 't', 'td')
    """
    # Get the directory that this module is located in
    thisdir = os.path.dirname(os.path.realpath(__file__))
    # Get the full path to the sounding data
    soundingfile = os.path.join(thisdir, 'data', 'soundings_{}.txt'.format(stid))
    
    # Load the data from the sounding file
    try:
        data = np.genfromtxt(soundingfile, dtype=str, delimiter=',', 
                             skip_header=1, usecols=(1,2,4,5,6))
    except:
        raise ValueError('ERROR: station "{}" does not exist!'.format(stid))
        
    # Get the dates for all the soundings
    dates = np.array([datetime.strptime(dstr, '%Y-%m-%d %H:00:00') for \
                      dstr in data[:,0]])
    # Find the date that is *closest* to the given date [date]
    diffs = np.abs(dates-date)
    d_inds = np.where(diffs==np.min(diffs))[0] #indices for the matching sounding
    sdate = dates[d_inds[0]] # the date of this sounding
    # Now get the other variables
    p = data[d_inds,1].astype(float)  # pressure in hPa
    z = data[d_inds,2].astype(float)  # height in meters
    # temperature in Celsius:
    t = np.array([float(x) if x!='M' else np.nan for x in data[d_inds,3]])
    # dew point in Celsius:
    td = np.array([float(x) if x!='M' else np.nan for x in data[d_inds,4]])
    
    # Reorder so that z is always increasing
    p = np.array([x for _,x in sorted(zip(z,p))])
    t = np.array([x for _,x in sorted(zip(z,t))])
    td = np.array([x for _,x in sorted(zip(z,td))])
    z = np.array([x for _,x in sorted(zip(z,z))])
    
    # Return only the data where T and Td aren't missing
    good = ~np.isnan(t) * ~np.isnan(td)
    datadict = {'date':sdate, 'p':p[good], 'z':z[good], 
                't':t[good], 'td':td[good]}
    return datadict

        

def nearest_ind(array,value):
    """
    Finds the nearest index of the given value in the given array.
    """
    return int((np.abs(array-value)).argmin())



def get_figdir():
    """
    Returns the full path to the "figures" directory in the same directory
    as this module. If "figures" does not exist, it is created.
    """
    # Get the directory that this module is located in
    thisdir = os.path.dirname(os.path.realpath(__file__))
    
    # The "figures" directory should also be in this directory
    figdir = os.path.join(thisdir, 'figures')
    
    # If it isn't, then create the "figures" directory
    if not os.path.isdir(figdir):
        os.mkdir(figdir)
    return figdir


# Any code within the following block with be executed if this module is run
# as a script! FEEL FREE TO ADD CODE FOR TESTING.
if __name__ == '__main__':
    print('Currently, this script does nothing!')
  
    