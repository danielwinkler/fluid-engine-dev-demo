#!/usr/bin/env python

import getopt
import os
import sys
import utils

def print_help():
    print 'render_level_set_liquid_sim.py -i <input_obj_file> -o <output_img>'

def main(argv):
    input_obj_file = ''
    output_img = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['input=', 'output='])
    except:
        print_help()
        quit(-1)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            quit(0)
        elif opt in ['-i', '--input']:
            input_obj_file = arg
        elif opt in ['-o', '--output']:
            output_img = arg
    if input_obj_file == '' or output_img == '':
        print_help()
        quit(-1)

    mitsuba_home = os.getenv('MITSUBA_HOME', '')
    mitsuba_exe = 'mitsuba'
    if mitsuba_home:
        mitsuba_exe = os.path.join(mitsuba_home, mitsuba_exe)

    args = [mitsuba_exe, '-o', output_img, '-Dobjfile=' + abs_input_obj_file, 'render/water_drop.xml']

    os.system(' '.join(args))

if __name__ == '__main__':
    main(sys.argv[1:])
