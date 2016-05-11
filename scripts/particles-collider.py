#!/usr/bin/env python

import render

render.render_still_line2(
    'manual_tests_output/ParticleSystemSolver3/PerfectBounce/data.#line2,1000,x.npy',
    'manual_tests_output/ParticleSystemSolver3/PerfectBounce/data.#line2,1000,y.npy',
    'particles-collision-results-a.pdf', has_xtick=False, has_ytick=False)

render.render_still_line2(
    'manual_tests_output/ParticleSystemSolver3/HalfBounce/data.#line2,1000,x.npy',
    'manual_tests_output/ParticleSystemSolver3/HalfBounce/data.#line2,1000,y.npy',
    'particles-collision-results-b.pdf', has_xtick=False, has_ytick=False)

render.render_still_line2(
    'manual_tests_output/ParticleSystemSolver3/NoBounce/data.#line2,1000,x.npy',
    'manual_tests_output/ParticleSystemSolver3/NoBounce/data.#line2,1000,y.npy',
    'particles-collision-results-c.pdf', has_xtick=False, has_ytick=False)

render.render_still_line2(
    'manual_tests_output/ParticleSystemSolver3/HalfBounceWithFriction/data.#line2,1000,x.npy',
    'manual_tests_output/ParticleSystemSolver3/HalfBounceWithFriction/data.#line2,1000,y.npy',
    'particles-collision-results-d.pdf', has_xtick=False, has_ytick=False)
