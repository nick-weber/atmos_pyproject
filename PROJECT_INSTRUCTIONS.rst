Project Instructions
====================

In this coding activity, you will be displaying meteorological data to analyze the `strong North American extratropical cyclone of October 2010`_. You will use three different datasets: gridded analyses (from the NARR_), ASOS surface station observations, and RAOB radiosonde (sounding) observations. The bulk of this exercise will involve coding in Python (briefly outlined in the paragraph below), with a short writing/analysis portion at the end.

To execute the following steps, you will need to both **a)** fill in some gaps within the code that has been provided and **b)** write your own code to call the functions within ``plotting_functions.py``. Task **a)** is fairly straightforward; you can find the "skeleton code" blocks by looking for the obnoxiously-commented ``FILL THIS BLOCK`` statements. Individual tasks are marked by commented ``# TODO:`` lines. You can accomplish task **b)** by either creating your own new module/script (e.g., ``project.py``) and importing ``plotting_functions`` or by writing code to call the functions within the ``plotting_functions.py`` module itself, in the "main" block (denoted by ``if __name__=='__main__':``).

.. _strong North American extratropical cyclone of October 2010: https://en.wikipedia.org/wiki/October_2010_North_American_storm_complex
.. _NARR: https://www.esrl.noaa.gov/psd/data/gridded/data.narr.html

1) Plot NARR analysis maps for the entire time period (Oct. 23-29)
------------------------------------------------------------------

a) Write some code (again, either in a new script or the main block of ``plotting_functions.py``) that uses the fully written ``plot_narr_olr()`` function in ``plotting_functions.py`` to make maps of NARR outgoing longwave radiation (OLR; think infrared satellite image), mean sea level pressure, and temperature.
b) Finish the partially written ``plot_narr_t2m_mslp()`` function, which plots 2-meter temperatures, mean sea level pressure, and wind barbs onto a map. Then, as in part a), call this function to make maps for the desired dates.

2) Plot radiosonde (sounding) data at a few RAOB sites at several times
-----------------------------------------------------------------------

a) Finish the ``plot_sounding()`` function in ``plotting_functions.py``.
b) Call this function for a few RAOB stations (e.g., KILX; see data directory for availability) and at several times, preferably just before/after frontal passage.

3) Plot multi-panel meteorogram (timeseries) data at a few ASOS sites
---------------------------------------------------------------------

a) Finish the ``plot_meteorogram()`` function in ``plotting_functions.py``.
b) Call this function for a few ASOS stations (e.g., ORD; see data directory for availability), preferably encompassing the time of a frontal passage.

4) Write a brief (500-1000 words) analysis of the event
-------------------------------------------------------

You can choose to focus on whatever aspects are most interesting to you. If you need a bit more direction, you can write about how you can use the weather maps and meteorograms to identify frontal passages at different locations. Here are some questions to consider:

- How can a front be identified on a gridded analysis map? How can you tell a warm front from a cold front?
- How can you tell a warm front from a cold front by only looking at a meteorogram? How are the different meteorological fields affected by frontal passage?
- Are there any differences in the vertical profile of temperature and dewpoint before/after frontal passage?

