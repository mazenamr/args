import sys

__args, __allargs, argvalues = [], {}, {}

class __Arg(str):
    pass

def __init():
    __args.clear()
    for i in sys.argv[1:]:
        if i[0] == '-':
            if i[1] == '-':
                __args.append(__Arg(i[2:]))
            else:
                for j in i[1:]:
                    __args.append(__Arg(j))
        else:
            __args.append(i)

def setargs(allargs):
    argparameters = {"".join(list(filter(lambda c: c != ':', i))):\
        len(list(filter(lambda c: c == ':', i))) for i in allargs}
    allargs = {__Arg("".join(list(filter(lambda c: c != ':', i)))):\
               __Arg(allargs[i]) for i in allargs}
    p = [0, None]
    for i in allargs:
        __allargs[i] = allargs[i]
        if allargs[i] != 'None' and len(allargs[i]) > 1:
            print(allargs[i])
            sys.exit(77)
    for i in range(len(__args)):
        if isinstance(__args[i], __Arg):
            if __args[i] not in allargs:
                __args[i] = list(allargs.keys())\
                            [list(allargs.values()).index(__args[i])]
            if p[0] != 0:
                sys.exit(78)
            if __args[i] in list(allargs.keys()):
                argvalues[__args[i]] = []
                p = [argparameters[__args[i]], __args[i]]
            else:
                sys.exit(80)
        else:
            if p[0] == 0:
                sys.exit(79)
            else:
                argvalues[p[1]].append(__args[i])
                p[0] -= 1
    for i in argvalues:
        argvalues[i] = None if not argvalues[i] else argvalues[i]

def checkargs(args):
    return any([i in argvalues for i in args])

def checkgroup(args):
    return all([i in argvalues for i in args])

__init()
