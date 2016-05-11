#!/usr/bin/env python

import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters

import render

# http://matplotlib.org/examples/pylab_examples/contour_demo.html
def render_basics_math_field_gradient():
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    # difference of Gaussians
    Z = 10.0 * (Z1 - Z2)

    # You can set negative contours to be solid instead of dashed:
    matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
    fig, ax = plt.subplots()
    ax.set_xticks(())
    ax.set_xticklabels(())
    ax.set_yticks(())
    ax.set_yticklabels(())
    CS = plt.contour(X, Y, Z, 6,
                     colors='k',  # negative contours will be dashed by default
                     )

    delta = 0.25
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    # difference of Gaussians
    Z = 10.0 * (Z1 - Z2)
    grad_v, grad_u = np.gradient(Z)
    plt.quiver(X, Y, grad_u, grad_v)

    plt.savefig('basics-math-field-gradient.pdf')

def render_basics_math_field_laplacian():
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = 10.0 * (Z2 - Z1)

    # You can set negative contours to be solid instead of dashed:
    matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
    fig, ax = plt.subplots()
    ax.set_xticks(())
    ax.set_xticklabels(())
    ax.set_yticks(())
    ax.set_yticklabels(())
    ax.set_aspect('equal')
    CS = plt.contour(X, Y, Z, 6,
                     colors='k',  # negative contours will be dashed by default
                     )
    plt.savefig('basics-math-field-laplacian0.pdf')
    plt.close(fig)

    # Gradient field
    delta = 0.25
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = 10.0 * (Z2 - Z1)

    grad_v, grad_u = np.gradient(Z)

    fig, ax = plt.subplots()
    ax.set_xticks(())
    ax.set_xticklabels(())
    ax.set_yticks(())
    ax.set_yticklabels(())
    ax.set_aspect('equal')
    plt.quiver(X, Y, -grad_u, -grad_v,units='x',scale=2.0,angles='xy')
    plt.savefig('basics-math-field-laplacian1.pdf')
    plt.close(fig)

    # Laplacian field
    delta = 0.025
    x = np.arange(-3.0, 3.0, delta)
    y = np.arange(-2.0, 2.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = 10.0 * (Z2 - Z1)

    lapl = scipy.ndimage.filters.laplace(Z)
    lapl = np.flipud(lapl)

    fig, ax = plt.subplots()
    ax.set_xticks(())
    ax.set_xticklabels(())
    ax.set_yticks(())
    ax.set_yticklabels(())
    ax.set_aspect('equal')
    print lapl.min(), lapl.max()
    im = ax.imshow(lapl, cmap=plt.cm.gray, interpolation='nearest')
    plt.savefig('basics-math-field-laplacian2.png')
    plt.close(fig)


render.render_still_scalar_grid2(
    'manual_tests_output/ScalarField3/Sample/data_#grid2.npy',
    'basics-math-field-sin.pdf',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)
render.render_still_vector_grid2(
    'manual_tests_output/ScalarField3/Gradient/data_#grid2,x.npy',
    'manual_tests_output/ScalarField3/Gradient/data_#grid2,y.npy',
    'basics-math-field-sin-gradient.pdf',
    has_xtick=False, has_ytick=False)
render.render_still_scalar_grid2(
    'manual_tests_output/ScalarField3/Laplacian/data_#grid2.npy',
    'basics-math-field-sin-laplacian.pdf',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)

render.render_still_vector_grid2(
    'manual_tests_output/VectorField3/Sample/data_#grid2,x.npy',
    'manual_tests_output/VectorField3/Sample/data_#grid2,y.npy',
    'basics-math-field-vecsin.pdf',
    has_xtick=False, has_ytick=False)
render.render_still_scalar_grid2(
    'manual_tests_output/VectorField3/Divergence/data_#grid2.npy',
    'basics-math-field-vecsin-divergence.pdf',
    has_iso=False, has_colorbar=False, has_xtick=False, has_ytick=False)
render.render_still_vector_grid2(
    'manual_tests_output/VectorField3/Curl/data_#grid2,x.npy',
    'manual_tests_output/VectorField3/Curl/data_#grid2,y.npy',
    'basics-math-field-vecsin-curl.pdf',
    has_xtick=False, has_ytick=False)

render.render_still_vector_grid2(
    'manual_tests_output/VectorField3/Sample2/data_#grid2,x.npy',
    'manual_tests_output/VectorField3/Sample2/data_#grid2,y.npy',
    'basics-math-field-curl-simple-ex.pdf',
    has_xtick=False, has_ytick=False)

render_basics_math_field_gradient()
render_basics_math_field_laplacian()
