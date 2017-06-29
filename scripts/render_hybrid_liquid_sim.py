#!/usr/bin/env python

import getopt
import os
import sys
import utils

def print_help():
    print('render_hybrid_liquid_sim.py -i <input_obj_file> -o <output_img>')

def main(argv):
    input_obj_file = ''
    output_img = ''
    template_xml = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:o:t:', ['input=', 'output=', 'template='])
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
        elif opt in ['-t', '--template']:
            template_xml = arg
    if input_obj_file == '' or output_img == '' or template_xml == '':
        print_help()
        quit(-1)

    mitsuba_exe = '"C:/Users/daniel/dev/Mitsuba 0.5.0/mitsuba.exe"'

    args = [mitsuba_exe, '-o', output_img, '-Dobjfile=' + input_obj_file, template_xml]

    os.system(' '.join(args))

if __name__ == '__main__':
    main(sys.argv[1:])