
'''
\ntemplate of script
This is the __doc__ and is pulled in as usage mod as needed
Usage: python template.py  -i <input>    -o <output>"
Arguments:
-i      data in to be processed
-o      result of processing
          Default output = "output.txt"


Flags:
-h      help

Version: 001

'''


import sys
import getopt


def usage(inData):
    print("\n ", inData)
    print(__doc__)


def pars_cmd(argv):
    # sets a simple internel default to check file options
    output = "output.txt"
    input = " "

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:vh")
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage(1)
        sys.exit(2)

    # checks to see if opts(list) is empty
    if not opts:
        print("There were no options given use -h to see help\n")

    # parses opts and arguments
    for o, a in opts:

        if o in ("-h"):
            usage(2)

        elif o in ("-o"):
            output = a
            print("out:", a)

        elif o in ("-i"):
            input = a
            print("in:", a)

        else:
            assert False, "unhandled option"
    # ...
    # change options check as needed.
    # if (output is None) or (input is None):
    if input is None:
        usage(3)

    return(output, input)
