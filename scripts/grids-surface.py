#!/usr/bin/env python

import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters

import render

render.render_still_scalar_grid2(
    'manual_tests_output/LevelSetSolver2/Reinitialize/data0_#grid2,iso.npy',
    'grids-fs-surface-lsm-distortion-init.pdf',
    has_iso=True, has_colorbar=False, has_xtick=False, has_ytick=False, iso_colors='w')

render.render_still_vector_grid2(
    'manual_tests_output/LevelSetSolver2/Reinitialize/flow_#grid2,x.npy',
    'manual_tests_output/LevelSetSolver2/Reinitialize/flow_#grid2,y.npy',
    'grids-fs-surface-lsm-distortion-flow.pdf',
    has_xtick=False, has_ytick=False)

render.render_still_scalar_grid2(
    'manual_tests_output/LevelSetSolver2/NoReinitialize/data_#grid2,iso.npy',
    'grids-fs-surface-lsm-distortion-noreinit.pdf',
    has_iso=True, has_colorbar=False, has_xtick=False, has_ytick=False, iso_colors='w')

render.render_still_scalar_grid2(
    'manual_tests_output/LevelSetSolver2/Reinitialize/data_#grid2,iso.npy',
    'grids-fs-surface-lsm-distortion-reinit.pdf',
    has_iso=True, has_colorbar=False, has_xtick=False, has_ytick=False, iso_colors='w')
