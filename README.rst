atmos_pyproject : displaying geophysical data with Python
=====================================================================================

A Python package designed as a teaching tool for introductory-level atmospheric sciences students. Contains functions and skeleton code for analyzing meteorological data.

In some of the instructions below, it is assumed that users have installed the Anaconda Python distribution.

How to Download:
----------------

- Click the green **Clone or Download** button near the top right of this repository.
- If you are familiar with git, you can copy the URL in the box and run ``git clone [URL]`` in a terminal/command prompt within the desired directory. **Otherwise**, you can click the **Download ZIP** button to download a zip file of this repository. Then simply move that zip file into whatever directory (folder) you will be working in and unzip it (you can usually do this by double-clicking or right-clicking the zip file).
- Once you have either cloned the repository or unzipped the zip file, move into the new directory (which should be named **atmos_pyproject-master** if you did the download method).

Package Contents:
-----------------

- **PROJECT_INSTRUCTIONS.rst**: The instructions for the project. Click on this file on Github to read the formatted instructions page.
- **README.rst**: This file.
- **plotting_tutorial.ipynb**: A Jupyter notebook that serves as an introduction to using matplotlib and Basemap for making line plots, 2-D contour plots, and 2-D contour plots projected onto maps.
- **plotting_functions.py**: Python module containing functions for plotting meteorological data. Some of the functions are not complete (skeleton code) and require the user to finish them.
- **utilities.py**: Python module containing "utility" functions to read data, make calculations, and perform other miscellanious tasks. The ``calculate_rh()`` function is skeleton code and requires completing.
- **data/**: A folder containing the data used in this project: a preprocessed NARR analysis netCDF, text files containing ASOS (meteorogram) data for different stations, and text files containing RAOB (sounding) data for different stations.

Installing Required Packages with Conda:
----------------------------------------

This package requires the netcdf4_ and basemap_ tools. These can be installed simply, using the Anaconda installation tool **conda**.

- First, open a command prompt. Mac/Linux users simply need to open a Terminal window (i.e., launch the **Terminal** application). Windows users need to open an **Anaconda Command Prompt** (found in your applications).
- To install **netcdf4**, simply type ``conda install netcdf4`` into the command prompt and press **Enter**.
- To install **basemap**, try doing the same, but instead type ``conda install basemap``. Since **basemap** support is ending with Python 2, Python 3 users may have trouble installing this package. If that first command did not work, try typing ``conda install -c conda-forge basemap`` instead. If unsuccessful still, contact the instructor for assistance.
- Now these packages can be imported the next time you launch Python. If you are currently running Python, restart the kernel in order to use these packages.

.. _netcdf4: http://unidata.github.io/netcdf4-python/
.. _basemap: https://matplotlib.org/basemap/

How to do the Plotting Tutorial:
--------------------------------

- In order to interactively do the plotting tutorial (which is a Jupyter Notebook, stored in **plotting_tutorial.ipynb**), you will need to launch the Jupyter Notebook application.
- If you are a Mac/Linux user, you can do this by simply opening a Terminal window (look for **Terminal** in your applications) in this project directory, then typing ``jupyter notebook`` into the command prompt.
- Windows users do almost the same thing. Open an **Anaconda Command Prompt** (which you can find by searching your applications) and type ``jupyter notebook`` into the command prompt.
- After launching Jupyter Notebook, a new tab should automatically open up in your browser. You should see all the files and directories within your current directory. Find and click on **plotting_tutorial.ipynb** to launch that notebook.
