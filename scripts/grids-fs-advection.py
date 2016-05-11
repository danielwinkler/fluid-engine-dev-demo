#!/usr/bin/env python

import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters

def render_still_scalar_grid2(filename, output_filename, **kwargs):
    interpolation = 'nearest'
    has_iso = False
    has_colorbar = True
    has_xtick = True
    has_ytick = True
    if 'interpolation' in kwargs:
        interpolation = kwargs['interpolation']
    if 'has_iso' in kwargs:
        has_iso = kwargs['has_iso']
    if 'has_colorbar' in kwargs:
        has_colorbar = kwargs['has_colorbar']
    if 'has_xtick' in kwargs:
        has_xtick = kwargs['has_xtick']
    if 'has_ytick' in kwargs:
        has_ytick = kwargs['has_ytick']
    grid_data = np.load(filename)
    fig, ax = plt.subplots()
    if not has_xtick:
        ax.set_xticks(())
        ax.set_xticklabels(())
    if not has_ytick:
        ax.set_yticks(())
        ax.set_yticklabels(())
    if has_iso:
        ax.set_aspect('equal')
        plt.contour(grid_data, 1, colors='k')
    if has_colorbar:
        plt.colorbar(im)
    plt.savefig(output_filename)
    plt.close(fig)
    print 'Rendered <%s>' % output_filename

render_still_scalar_grid2(
    'manual_tests_output/CubicSemiLagrangian2/Zalesak/orig_#grid2,iso.npy',
    'grids-fs-advection-interpolation-compare-orig.pdf',
    has_iso=True, has_colorbar=False, has_xtick=False, has_ytick=False)

render_still_scalar_grid2(
    'manual_tests_output/SemiLagrangian2/Zalesak/rev0628_#grid2,iso.npy',
    'grids-fs-advection-interpolation-compare-linear.pdf',
    has_iso=True, has_colorbar=False, has_xtick=False, has_ytick=False)

render_still_scalar_grid2(
    'manual_tests_output/CubicSemiLagrangian2/Zalesak/rev0628_#grid2,iso.npy',
    'grids-fs-advection-interpolation-compare-cubic.pdf',
    has_iso=True, has_colorbar=False, has_xtick=False, has_ytick=False)

catmull_rom = [0.000000, 0.005446, 0.011768, 0.018942, 0.026944, 0.035750, 0.045336, 0.055678, 0.066752, 0.078534, 0.091000, 0.104126, 0.117888, 0.132262, 0.147224, 0.162750, 0.178816, 0.195398, 0.212472, 0.230014, 0.248000, 0.266406, 0.285208, 0.304382, 0.323904, 0.343750, 0.363896, 0.384318, 0.404992, 0.425894, 0.447000, 0.468286, 0.489728, 0.511302, 0.532984, 0.554750, 0.576576, 0.598438, 0.620312, 0.642174, 0.664000, 0.685766, 0.707448, 0.729022, 0.750464, 0.771750, 0.792856, 0.813758, 0.834432, 0.854854, 0.875000, 0.894846, 0.914368, 0.933542, 0.952344, 0.970750, 0.988736, 1.006278, 1.023352, 1.039934, 1.056000, 1.071526, 1.086488, 1.100862, 1.114624, 1.127750, 1.140216, 1.151998, 1.163072, 1.173414, 1.183000, 1.191806, 1.199808, 1.206982, 1.213304, 1.218750, 1.223296, 1.226918, 1.229592, 1.231294, 1.232000, 1.231686, 1.230328, 1.227902, 1.224384, 1.219750, 1.213976, 1.207038, 1.198912, 1.189574, 1.179000, 1.167166, 1.154048, 1.139622, 1.123864, 1.106750, 1.088256, 1.068358, 1.047032, 1.024254, 1.000000]
monotonic_catmull_rom = [0.000000, 0.005199, 0.010788, 0.016759, 0.023104, 0.029812, 0.036876, 0.044285, 0.052032, 0.060107, 0.068500, 0.077203, 0.086208, 0.095504, 0.105084, 0.114937, 0.125056, 0.135430, 0.146052, 0.156912, 0.168000, 0.179309, 0.190828, 0.202550, 0.214464, 0.226562, 0.238836, 0.251276, 0.263872, 0.276617, 0.289500, 0.302514, 0.315648, 0.328894, 0.342244, 0.355687, 0.369216, 0.382820, 0.396492, 0.410221, 0.424000, 0.437818, 0.451668, 0.465539, 0.479424, 0.493313, 0.507196, 0.521065, 0.534912, 0.548726, 0.562500, 0.576223, 0.589888, 0.603485, 0.617004, 0.630437, 0.643776, 0.657010, 0.670132, 0.683132, 0.696000, 0.708728, 0.721308, 0.733729, 0.745984, 0.758062, 0.769956, 0.781655, 0.793152, 0.804437, 0.815500, 0.826334, 0.836928, 0.847274, 0.857364, 0.867188, 0.876736, 0.886001, 0.894972, 0.903642, 0.912000, 0.920039, 0.927748, 0.935120, 0.942144, 0.948812, 0.955116, 0.961046, 0.966592, 0.971747, 0.976500, 0.980843, 0.984768, 0.988265, 0.991324, 0.993937, 0.996096, 0.997791, 0.999012, 0.999752, 1.000000]

fig, ax = plt.subplots()
ax.set_xticks(())
ax.set_xticklabels(())
ax.set_yticks(())
ax.set_yticklabels(())
plt.plot(catmull_rom, color='k', linestyle='--')
plt.plot(monotonic_catmull_rom, color='k', linestyle='-')
plt.savefig('grids-fs-advection-interpolation-mcerp.pdf')
