#!/usr/local/bin/python3.7
######################################################################
#
# Name: patchit.py
#
# Description:  A smallish script that provides a starting point
#               for various Python endeavors.
#
# (c) Copyright 2019 Adam W. Dace.  All rights reserved.
#
######################################################################

# Pydoc comments
"""Application entry point for hello."""

# File version tag
__version__ = '0.1'

# Standard modules
import getopt
import os
import os.path
import socket
import sys
import traceback

######################################################################
# Good old main...
######################################################################

def main(argv):
    """Good old main."""

    usage = """Usage: %s [OPTION] required_arg

A smallish script that provides a starting point for various Python endeavors.

The available options are:

    -h / --help / -? / --?
    Prints the usage statement.
    OPTIONAL

    -v / --version
    Prints the version banner.
    OPTIONAL

Exit Status Codes:
------------------
0 = Success
1 = Failure

Examples:
---------
hello.py testing
hello.py --help
""" % argv[0]

    version = """hello.py v%s
Hello Wortld Script
(c) Copyright 2019 Adam W. Dace.  All rights reserved.
------------------------------------------------------
""" % __version__

######################################################################
# Variable initialization.
######################################################################

    # Various variables.
    help_string = ''

    # Getopt variables.
    short_options = 'hv?'
    long_options = ['help',
                    'version',
                    '?']

######################################################################
# Main logic flow.
######################################################################

    try:
        if len(argv) < 2:
            raise RuntimeError

        optlist, args = \
                 getopt.getopt(sys.argv[1:], short_options, long_options)

        if len(optlist) > 0:
            for opt in optlist:
                if (opt[0] in ('-h', '-?', '--help', '--?')):
                    print(version)
                    print(usage)
                    sys.exit(0)
                elif (opt[0] in ('-v', '--version')):
                    print(version)
                    sys.exit(0)

        if len(args) > 0:
            required_arg = args[0]

    except RuntimeError:
        print(version)
        print("ERROR: Invalid argument or flag found.  Please check your syntax.")
        print("ERROR: Run again with the --help flag for more information.")
        print
        sys.exit(1)

    except getopt.GetoptError:
        print(version)
        print("ERROR: Invalid argument or flag found.  Please check your syntax.")
        print("ERROR: Please run again with the --help flag for more information.")
        print
        sys.exit(1)

    print(version)
    print("Hello World!")
    print("Your given required argument is: %s" % required_arg)
    sys.exit(0)

######################################################################
# If called from the command line, invoke thyself!
######################################################################

if __name__ == '__main__': main(sys.argv)

######################################################################
