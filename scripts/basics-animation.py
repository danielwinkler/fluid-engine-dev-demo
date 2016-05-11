#!/usr/bin/env python

import render

render.render_still_line2(
    'manual_tests_output/Animation/OnUpdateSine/data.#line2,x.npy',
    'manual_tests_output/Animation/OnUpdateSine/data.#line2,y.npy',
    'basics-animation-sine-a.pdf', has_xtick=False, has_ytick=False)

render.render_still_line2(
    'manual_tests_output/Animation/OnUpdateSineWithDecay/data.#line2,x.npy',
    'manual_tests_output/Animation/OnUpdateSineWithDecay/data.#line2,y.npy',
    'basics-animation-sine-b.pdf', has_xtick=False, has_ytick=False)
