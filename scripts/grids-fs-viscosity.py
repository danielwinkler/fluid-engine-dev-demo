#!/usr/bin/env python

import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters

import render

render.render_still_scalar_grid2(
    'manual_tests_output/GridBackwardEulerDiffusionSolver3/SolveWithBoundaryNoFlux/dst_#grid2.npy',
    'grids-fs-viscosity-boundary-results-noflux.pdf',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)
render.render_still_scalar_grid2(
    'manual_tests_output/GridBackwardEulerDiffusionSolver3/SolveWithBoundaryNoFlux/dst_#grid2.npy',
    'grids-fs-viscosity-boundary-results-noflux.png',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)
render.render_still_scalar_grid2(
    'manual_tests_output/GridBackwardEulerDiffusionSolver3/SolveWithBoundaryNoSlip/dst_#grid2.npy',
    'grids-fs-viscosity-boundary-results-noslip.pdf',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)

render.render_still_scalar_grid2(
    'manual_tests_output/GridBackwardEulerDiffusionSolver3/SolveWithBoundaryNoSlip/dst_#grid2.npy',
    'grids-fs-viscosity-boundary-results-noslip.png',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)

render.render_still_scalar_grid2(
    'manual_tests_output/GridBackwardEulerDiffusionSolver3/Stable/dst_#grid2.npy',
    'grids-fs-viscosity-stability-broken-unstable.pdf',
    has_iso=False, has_colorbar=True, has_xtick=False, has_ytick=False)

render.render_still_scalar_grid2(
    'manual_tests_output/GridForwardEulerDiffusionSolver3/Unstable/dst_#grid2.npy',
    'grids-fs-viscosity-stability-broken-stable.pdf',
    has_iso=False, has_colorbar=True, has_xtick=False, has_ytick=False)
