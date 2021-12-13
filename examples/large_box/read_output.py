#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:53:18 2021

@author: jguterl
"""
import numpy as np
FileName='/Users/Alyssa/Dev/pyGITR/examples/large_box/output/surface.nc'

import netCDF4
from netCDF4 import Dataset
SurfaceData = Dataset(FileName, "r", format="NETCDF4")
Distrib = np.array(SurfaceData.variables['surfEDist'])
print('Total particle={}'.format(np.sum(Distrib,(0,1,2))))
