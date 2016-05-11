#!/usr/bin/env python

import render

render.render_still_line2(
    'manual_tests_output/Animation/OnUpdateSineWithDecay/data.#line2,x.npy',
    'manual_tests_output/Animation/OnUpdateSineWithDecay/data.#line2,y.npy',
    'basics-pba-ex-motion-damping.pdf', has_xtick=False, has_ytick=False, markersize=0, linestyle=':')

render.render_still_line2(
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0000,x.npy',
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0000,y.npy',
    'basics-pba-ex-final0.pdf', has_xtick=False, has_ytick=False, markersize=3, xlim=(-12,12), ylim=(-7, 1))
render.render_still_line2(
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0050,x.npy',
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0050,y.npy',
    'basics-pba-ex-final1.pdf', has_xtick=False, has_ytick=False, markersize=3, xlim=(-12,12), ylim=(-7, 1))
render.render_still_line2(
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0100,x.npy',
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0100,y.npy',
    'basics-pba-ex-final2.pdf', has_xtick=False, has_ytick=False, markersize=3, xlim=(-12,12), ylim=(-7, 1))
render.render_still_line2(
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0200,x.npy',
    'manual_tests_output/PhysicsAnimation/SimpleMassSpringAnimation/data.#line2,0200,y.npy',
    'basics-pba-ex-final3.pdf', has_xtick=False, has_ytick=False, markersize=3, xlim=(-12,12), ylim=(-7, 1))
