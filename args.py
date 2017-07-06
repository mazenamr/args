#     Args - A Python 3 library for handling command line arguments
#     Copyright (C) 2017  Mazen Amr
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Also add information on how to contact you by electronic and paper mail.
#
#   If your software can interact with users remotely through a computer
# network, you should also make sure that it provides a way for users to
# get its source.  For example, if your program is a web application, its
# interface could display a "Source" link that leads users to an archive
# of the code.  There are many ways you could offer source, and different
# solutions will be better for different programs; see section 13 for the
# specific requirements.
#
#   You should also get your employer (if you work as a programmer) or school,
# if any, to sign a "copyright disclaimer" for the program, if necessary.
# For more information on this, and how to apply and follow the GNU AGPL, see
# <http://www.gnu.org/licenses/>.

import sys

__args = [] # List of all arguments provided by the user
argvalues = {} # Dictionary of the arguments provided and their parameters

class __Arg(str):
    pass

def __init():
    """Fills __args with the arguments provided by the user."""
    __args.clear()
    for i in sys.argv[1:]:
        if i[0] == '-':
            if i[1] == '-':
                __args.append(__Arg(i[2:]))
            else:
                # If an argument is preceded by only one dash,
                # it will be treated like a group of arguments
                # in the short form (-vc = -v -c = --verbose --clean).
                for j in i[1:]:
                    __args.append(__Arg(j))
        else:
            __args.append(i)

def setargs(allargs):
    """Fills argvalues with the arguments provided by the user \
and their parameters.\n
Exits with an error code if the user provided an unkown argument, \
or provided an argument in the place of a parameter or vice versa, \
or didn't provide enough parameters for an argument."""
    argvalues.clear()
    # Checks for duplicates
    args = list(allargs.keys()) + list(allargs.values())
    if not any([args.count(i) != 1 or i == None for i in args]):
        sys.exit(76)
    # List of all the valid arguments and the number of parameters
    # each of them requires
    argparameters = {"".join(list(filter(lambda c: c != ':', i))):\
        len(list(filter(lambda c: c == ':', i))) for i in allargs}
    # Removes the columns (:) from the long forms of the args
    allargs = {__Arg("".join(list(filter(lambda c: c != ':', i)))):\
               __Arg(allargs[i]) for i in allargs}
    # Checks if any of the short forms is longer than one character
    for i in allargs:
        if allargs[i] != 'None' and len(allargs[i]) > 1:
            sys.exit(77)
    # p[1] is the last argument p[0] is the number of parameters it takes
    p = [0, None]
    for i in range(len(__args)):
        # Checks if the item is an argument
        if isinstance(__args[i], __Arg):
            # Converts the item to the long form if it's in the short form
            if __args[i] not in allargs:
                __args[i] = list(allargs.keys())\
                            [list(allargs.values()).index(__args[i])]
            # Checks if all parameters have been provided
            # for the previous argument
            if p[0] != 0:
                sys.exit(78)
            # Checks if the item is a valid argument
            if __args[i] in list(allargs.keys()):
                argvalues[__args[i]] = []
                p = [argparameters[__args[i]], __args[i]]
            else:
                sys.exit(80)
        else:
            # Checks if a parameter is provided when no parameter is required
            if p[0] == 0:
                sys.exit(79)
            else:
                argvalues[p[1]].append(__args[i])
                p[0] -= 1
    # Checks if any more parameters were required but not provided
    if p[0] != 0:
        sys.exit(81)
    # Turns all the empty lists in argvalues to None
    for i in argvalues:
        argvalues[i] = None if not argvalues[i] else argvalues[i]

def checkargs(args):
    """Checks if any of the arguments in args was provided"""
    return any([i in argvalues for i in args])

def checkgroup(args):
    """Checks if all of the arguments in args were provided"""
    return all([i in argvalues for i in args])

__init()
