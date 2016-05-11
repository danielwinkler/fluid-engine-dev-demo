#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import render

def render_basics_kernel1d():
    fig, ax = plt.subplots()

    data_x = np.load('manual_tests_output/SphStdKernel3/Operator/kernel1.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphStdKernel3/Operator/kernel1.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle='-', color="black", linewidth=2.5)

    data_x = np.load('manual_tests_output/SphStdKernel3/Operator/kernel2.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphStdKernel3/Operator/kernel2.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle='--', color="black", linewidth=2.5)

    data_x = np.load('manual_tests_output/SphStdKernel3/Operator/kernel3.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphStdKernel3/Operator/kernel3.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle=':', color="black", linewidth=2.5)

    plt.xticks(
        [-1.5, -1.2, -1.0, 0, 1.0, 1.2, 1.5],
        [r'$-1.5$', r'$-1.2$', r'$-1.0$', r'$0.0$', r'$1.0$', r'$1.2$', r'$1.5$'])

    plt.yticks(
        [0, 1, 2],
        [r'$0$', r'$1$', r'$2$'])

    plt.savefig('particles-sph-basics-kernel1d.pdf')
    plt.close(fig)

def render_basics_dkernel_std():
    fig, ax = plt.subplots()

    data_x = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/std.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/std.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle='-', color="black")

    data_x = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/std_1st.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/std_1st.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle='--', color="black")

    data_x = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/std_2nd.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/std_2nd.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle=':', color="black")

    plt.xticks(
        [-1.0, -0.5, 0.0, 0.5, 1.0],
        [r'$-1.0$', r'$-0.5$', r'$0.0$', r'$0.5$', r'$1.0$'])

    plt.yticks(
        [-10, -5, 0, 5],
        [r'$-10$', r'$-5$', r'$0$', r'$5$'])

    plt.savefig('particles-sph-basics-dkernel_std.pdf')
    plt.close(fig)

def render_basics_dkernel_spiky():
    fig, ax = plt.subplots()

    data_x = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/spiky.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/spiky.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle='-', color="black")

    data_x = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/spiky_1st.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/spiky_1st.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle='--', color="black")

    data_x = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/spiky_2nd.#line2,x.npy')
    data_y = np.load('manual_tests_output/SphSpikyKernel3/Derivatives/spiky_2nd.#line2,y.npy')
    plt.plot(data_x, data_y, linestyle=':', color="black")

    plt.xticks(
        [-1.0, -0.5, 0.0, 0.5, 1.0],
        [r'$-1.0$', r'$-0.5$', r'$0.0$', r'$0.5$', r'$1.0$'])

    plt.yticks(
        [-15, 0, 15, 30],
        [r'$-15$', r'$0$', r'$15$', r'$30$'])

    plt.savefig('particles-sph-basics-dkernel_spiky.pdf')
    plt.close(fig)

render_basics_kernel1d()
render_basics_dkernel_std()
render_basics_dkernel_spiky()
