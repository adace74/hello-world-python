#!/usr/local/bin/python3.7
######################################################################
#
# Name: patchit.py
#
# Description:  A smallish script that will attempt to patch a
#               downloaded codebase with files from DragonFly BSD's
#               DPorts collection.
#
#               It currently assumes your working directory
#               is the top-level directory of the codebase,
#               and that DPorts is installed and readable in the
#               usual /usr/dports/ location.
#
#               NOTE: Currently written for, and only tested on
#               DragonFly BSD.
#
# (c) Copyright 2019 Adam W. Dace.  All rights reserved.
#
######################################################################

# Pydoc comments
"""Application entry point for patchit."""

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

    usage = """Usage: %s [OPTION] dport_name

This script will attempt to patch a downloaded codebase with files
from DragonFly BSD's DPorts collection.

It currently assumes your working directory is the top-level directory
of the codebase, and that DPorts is installed and readable in the
usual /usr/dports/ location.

NOTE: Currently written for, and only tested on DragonFly BSD.

The available options are(fixme):

    -b=MATCH / --banner=MATCH
    Specifies that in order to achieve success, the remote service
    must return a banner containing the string specified.
    OPTIONAL

    -h / --help / -? / --?
    Prints the usage statement.
    OPTIONAL

    -p=TCP_PORT / --port=TCP_PORT
    Specifies which port on the remote host to connect to.
    Default: 22
    OPTIONAL

    -q / --quiet
    Specifies that only an exit code is wanted.  i.e. no STDOUT output.
    OPTIONAL

    -t / --timeout=TIMEOUT
    Specifies the socket-level timeout in seconds.
    Default: 10
    OPTIONAL

    -v / --version
    Prints the version banner.
    OPTIONAL

Exit Status Codes:
------------------
0 = Success
1 = Socket error type 1.
2 = Socket error type 2.
3 = Socket error type 3.
4 = Socket timeout during connect() / recv().
5 = Unknown exception caught.
6 = Received non-matching or zero-length service banner.

Examples:
---------
pingtcp.py --banner=OpenSSH --timeout=20 sshbox.somewhere.com
pingtcp.py --banner=ESMTP --port=25 mailbox.somewhere.com
""" % argv[0]

    version = """patchit.py v%s
Sourecode Level Patch Script
(c) Copyright 2019 Adam W. Dace.  All rights reserved.
------------------------------------------------------
""" % __version__

######################################################################
# Variable initialization.
######################################################################

    # Various variables.
    banner_string = ''
    host_name = ''
    host_port = 22
    timeout = 10
    is_banner_mode = 0
    is_quiet_mode = 0

    # Getopt variables.
    short_options = 'b:hp:qt:v?'
    long_options = ['banner=',
                    'help',
                    'port=',
                    'quiet',
                    'timeout=',
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
                if (opt[0] in ('-b', '--banner')):
                    is_banner_mode = 1
                    banner_string = opt[1]
                elif (opt[0] in ('-h', '-?', '--help', '--?')):
                    print(version)
                    print(usage)
                    sys.exit(0)
                elif (opt[0] in ('-p', '--port')):
                    host_port = int(opt[1])
                elif (opt[0] in ('-q', '--quiet')):
                    is_quiet_mode = 1
                elif (opt[0] in ('-t', '--timeout')):
                    timeout = int(opt[1])
                elif (opt[0] in ('-v', '--version')):
                    print(version)
                    sys.exit(0)

        if len(args) > 0:
            host_name = args[0]

    except RuntimeError:
        print(version)
        print("ERROR: Invalid argument or flag found.  Please check your syntax.")
        print("ERROR: Please run again with the --help flag for more information.")
        print
        sys.exit(1)

    except getopt.GetoptError:
        print(version)
        print("ERROR: Invalid argument or flag found.  Please check your syntax.")
        print("ERROR: Please run again with the --help flag for more information.")
        print
        # Displaying original getopt error.
        #traceback.print_exc(1, file=sys.stdout)
        sys.exit(1)

    if not is_quiet_mode:
        print(version)

    print("Hello!")
    sys.exit(0)

######################################################################
# If called from the command line, invoke thyself!
######################################################################

if __name__ == '__main__': main(sys.argv)

######################################################################
