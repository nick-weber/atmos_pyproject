#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module containing functions to plot atmospheric data in various forms.

@author: njweber2
"""
import utilities as ut    # our utilities.py file!
import numpy as np        # for doing math and dealing with arrays
import matplotlib.pyplot as plt # plotting tools
from datetime import datetime  # this allows us to make datetime objects
# These following two lines will allow us to ignore the warnings that are
# raised when using the basemap toolkit (which is being phased out).
import warnings
warnings.filterwarnings("ignore")

def plot_meteorogram(stid, dt1, dt2):
    """
    Plots and ASOS meteorogram (multi-panel weather timeseries plot) for a 
    given station and time range.
    
    Requires:
        stid -> tation ID (string)
        dt1 --> starting time (datetime object)
        dt2 --> ending time (datetime object)
        
    Returns:
        nothing! Saves figure as "meteorogram_[stid]_[dt1]-[dt2].png"
    """
    
    # Load the ASOS data dictionary using our function in utilities.py
    metdata = ut.get_meteorogram(stid, dt1, dt2)
    # Now we have the ob. dates ('dates'), temperatures ('t'), dew point 
    # temperatures ('td'), wind directions ('wdir'), wind speeds ('wspd'), 
    # pressures ('pres'), and 1-hour precipitation values ('prec')
    
    
    ######################################################################
    ### FILL IN THIS BLOCK ###############################################
    ######################################################################
    
    # TODO: create a SIX-PANEL figure and w/ axes, using plt.subplots()
    #       pro-tip: make it taller than it is wide using "figsize"

    
    # TODO: plot the data onto the different axes
    # Let the dates be the x-axis values (matplotlib can handle datetimes)
    #   - row1 : temperature and dewpoint
    #   - row2 : relative humidity (calculate this using ut.calculate_rh())
    #   - row3 : wind direction
    #   - row4 : wind speed
    #   - row5 : pressure
    #   - row6 : hourly precipitation
    
    
    # TODO: label each axis by setting its ylabel to the variable name
    #       and set the x-limits to dt1 and dt2
    
    
    ######################################################################
    ### END HERE #########################################################
    ######################################################################
    
    # Format the datetime xticklabels to clean it up
    # first, get rid of xticklabels on all but the bottom plot
    for ax in axes[:-1]:
        ax.set_xticklabels([])
    # now let's rotate the date labels on the bottom so we can read them
    plt.setp(axes[-1].get_xticklabels(), rotation=20, ha='right')
    
    # Title the figure
    title = '{} meteorogram beginning {:%Y-%m-%d %H:00}'
    axes[0].set_title(title.format(stid, dt1), loc='left')
    
    # Save the figure as a .png file
    figdir = ut.get_figdir() # find/create a "figures" directory here
    # each filename describes the figure type and date range
    savefile = '{}/meteorogram_{}_{:%b%d}-{:%b%d}.png'
    plt.savefig(savefile.format(figdir, stid, dt1, dt2)) 
    plt.close() # close this figures so we don't use tons of memory
    
    
    
def plot_sounding(stid, date):
    """
    Plots radiosonde data (temp. and dewpoint) for a given station and time.
    
    Requires:
        stid --> station ID (string)
        date --> desired time (datetime object)
        
    Returns:
        nothing! Saves figure as "sounding_[stid]_[dt].png"
    """
    
    # Load the sounding data dictionary using our function in utilities.py
    sounding = ut.get_sounding(stid, date)
    # Now we have the sounding date ('date'), pressures ('p'), heights ('z'),
    # temperatures ('t'), and dew point temperatures ('td')
    
    
    ######################################################################
    ### FILL IN THIS BLOCK ###############################################
    ######################################################################
    
    # TODO: create a figure and (optionally) an axis object
    
    # TODO: plot a single dry adiabat, starting from the surface temperature,
    #       with a dashed black line
    
    # TODO: plot the temperature (in red) and dew point (in blue) with either
    #       height or pressure as the vertical coordinate
    
    # TODO: label the x and y axes, zoom in to the bottom ~14km (<150hPa) of
    #       the atmosphere, adjust the x-limits (if necessary), and draw a grid
    
    ######################################################################
    ### END HERE #########################################################
    ######################################################################
    
    # Title the figure
    ax.set_title('{} sounding on {:%Y-%m-%d %H:00}'.format(stid, date), loc='left')
    
    # Save the figure as a .png file
    figdir = ut.get_figdir() # find/create a "figures" directory here
    # each filename describes the figure type and observation date
    savefile = '{}/sounding_{}_{:%Y%m%d%H}.png'.format(figdir, stid, date)
    plt.savefig(savefile)
    plt.close() # close this figures so we don't use tons of memory



def plot_narr_t2m_mslp(dt1, dt2, verbose=False):
    """
    Plots/saves a US map of 2-meter temperature, MSLP, and wind barbs (from the
    NARR dataset) every 3 hours in the date range [dt1] to [dt2].
    
    Requires:
        dt1 -----> a datetime object containing the starting date
        dt2 -----> a datetime object containing the ending date
        verbose -> if True, function prints logging information
        
    Returns:
        nothing! Saves figures as "t2m_mslp_*.png
    """
    from mpl_toolkits.basemap import Basemap   # for projecting data onto a map
    
    plt.ioff() # we don't want plots to display
    
    # Load the NARR temp., press., and wind data from the netcdf file
    if verbose: print('Loading NARR data...')
    narr = ut.load_narr_data(dt1, dt2)  # from utilities.py
    # ^ this is a dictionary of numpy arrays (see load_narr_data() for details)
    
    ######################################################################
    ### FILL IN THIS BLOCK ###############################################
    ######################################################################
    
    # TODO: Choose a colormap and contour levels for temp./pressure
    #        (we will use these variables for plotting later)
    #       Contour temperature every 2C and pressure every 4hPa
    
    # TODO: Create a Basemap object to plot the data on (over North America)
    
    # TODO: Project lat/lon variables onto this map projection
    
    # Loop through the dates and create/save a figure at each time
        
        # TODO: Create Figure and Axes objects
        
        # TODO: Contour-fill the temperatures (using the colormap and levels
        #       defined above) and solid-contour the pressures in black (also
        #       using pre-defined levels)
        
        # Freebie: plot wind barbs in black (I coarsen the grid by a factor 
        # of 8, otherwise the barbs will be FAR too densely packed)
        m.barbs(x[::8,::8], y[::8,::8], narr['u10m'][d,::8,::8], 
                narr['v10m'][d,::8,::8], length=5, barbcolor='k', 
                flagcolor='k', linewidth=0.5)
        
        # TODO: Draw the map (coast/country/state lines and lat/lon lines)
        
        # TODO: Add a colorbar and (optionally) contour labels (using clabel())
        
        ##################################################################
        ### END HERE #####################################################
        ##################################################################
        
        # Add a title describing the fields, their units, and the date
        title = '2-meter temp. [C; colors], MSLP [hPa; contours], and ' + \
                'winds [kts; barbs] -- {:%Y-%m-%d %H:00} UTC'
        ax.set_title(title.format(date), loc='left')
        
        # Save the figure as a .png file
        figdir = ut.get_figdir() # find/create a "figures" directory here
        savefile = '{}/t2m_mslp_{:%Y%m%d%H}.png'.format(figdir, date)
        plt.savefig(savefile) # each filename describes the fields & date
        plt.close() # close this figures so we don't use tons of memory
    if verbose: print('Done!\n')
    
    
    

def plot_narr_olr(dt1, dt2, verbose=False):
    """
    Plots/saves a US map of 2-meter temperature, MSLP, and outgoing longwave
    radiation (from the NARR dataset) every 3 hours in the date range [dt1] to [dt2].
    
    Requires:
        dt1 -----> a datetime object containing the starting date
        dt2 -----> a datetime object containing the ending date
        verbose -> if True, function prints logging information
        
    Returns:
        nothing! Saves figures as "olr_*.png
    """
    from mpl_toolkits.basemap import Basemap   # for projecting data onto a map
    
    plt.ioff() # we don't want plots to display
    
    # Establish our colormap and contour intervals
    cmap  = plt.cm.binary                   # colormap for OLR
    olevs = np.arange(100., 350., 10.)     # contour levels for olr
    plevs = np.arange(940., 1051., 4.)     # contour levels for pressures
    
    # Load the NARR temp., press., and wind data from the netcdf file
    if verbose: print('Loading NARR data...')
    narr = ut.load_narr_data(dt1, dt2)  # from utilities.py
    # ^ this is a dictionary of numpy arrays
    
    # Create our Basemap object to plot the data on (domain = North America)
    m = Basemap(width=8000000,height=5000000,projection='lcc',
                resolution='l',lat_1=45.,lat_2=55,lat_0=45,lon_0=-97.)
    # Project out lat/lon variables onto this map projection
    x, y = m(narr['lons'], narr['lats'])
    
    # Loop through the dates and create/save a figure at each time
    if verbose: print('Plotting olr/pressure/temp maps...')
    for d, date in enumerate(narr['dates']):
        if verbose: print('  ', date)
        
        # Create our figure and axis objects
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10,6))
        # adjust the axis that we've just made to make room for a colorbar axis
        # (which we will make later) to its right
        fig.subplots_adjust(left=0.05, right=0.90, bottom=0.05, top=0.92)
        
        # Contour-fill the OLR using the colormap [cmap]
        cs1 = ax.contourf(x, y, narr['olr'][d,:,:], levels=olevs, cmap=cmap, 
                          extend='both', antialiasing=True)
        # Solid-contour the temperatures in blue/red
        #   below-freezing temps = blue
        ax.contour(x, y, narr['t2m'][d,:,:], levels=range(-32,0,4), colors='b',
                   linestyles='-', linewidths=0.8, antialiasing=True) 
        #   above-freezing temps = red
        ax.contour(x, y, narr['t2m'][d,:,:], levels=range(4,33,4),
                   colors='r', linewidths=0.8,  antialiasing=True) 
        #   freezing level = magenta
        ax.contour(x, y, narr['t2m'][d,:,:], levels=[0],
                   colors='m', linewidths=0.8,  antialiasing=True) 
        # Solid-contour the pressures in black
        cs2 = ax.contour(x, y, narr['mslp'][d,:,:], levels=plevs, colors='k', 
                         antialiasing=True)
        
        # Draw the map (coast/country/state lines and lat/lon lines)
        m.drawcoastlines(color='k')
        m.drawcountries(color='k')
        m.drawstates(color='k')
        m.drawparallels(np.arange(0.,81,10.), dashes=[2,1], labels=[1,0,0,0])
        m.drawmeridians(np.arange(0.,360,20.), dashes=[2,1], labels=[0,0,0,1])
        
        # Add the colorbar and the contour labels
        # make a new axis object for our colorbar
        cax = fig.add_axes([0.92, 0.05, 0.02, 0.87]) # [left, bottom, width, height]
        # assign the data from our contour-fills to this colorba
        plt.colorbar(cs1, cax=cax, ticks=olevs[::2])
        # label the pressure contours every other pressure level ("::2")
        plt.clabel(cs2, plevs[::2], fmt='%d')
        
        # Add a title describing the fields, their units, and the date
        title = 'OLR [W m$^{-2}$], 2-m temp. [every 4C ' + \
                '], and MSLP [hPa] -- {:%Y-%m-%d %H:00} UTC'.format(date)
        ax.set_title(title, loc='left')
        
        # Save the figure as a .png file
        figdir = ut.get_figdir() # find/create a "figures" directory here
        savefile = '{}/olr_{:%Y%m%d%H}.png'.format(figdir, date)
        plt.savefig(savefile) # each filename describes the fields & date
        plt.close() # close this figures so we don't use tons of memory
    if verbose: print('Done!\n')
    
      
# Any code within the following block with be executed if this module is run
# as a script! FEEL FREE TO ADD CODE FOR TESTING.
if __name__ == '__main__':
    print('Currently, this script does nothing!')
    plot_meteorogram('ORD', datetime(2010, 10, 26, 0), 
                               datetime(2010, 10, 28, 0))
#    plot_sounding('KGRB', datetime(2010, 10, 27, 6))
#    dt1 = datetime(2010, 10, 25, 0)
#    dt2 = datetime(2010, 10, 29, 0)
#    plot_narr_olr(dt1, dt2, verbose=True)
        