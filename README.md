# Args

## About

A Python 3 library for handling command line arguments.

## Getting Started

### Prerequisites

Python 3 or newer.

### Installation

#### For A System-wide Installation

##### 1 - Clone it

```sh
git clone https://github.com/mazenamr/args.git
```

##### 2 - Copy the contents to one of the Python Paths

```sh
cp ./args /usr/lib/python3.6
```

###### To View Your Python Paths

```py
from system import path
print(path)
```

#### For Usage Within A Project

##### 1 - Clone it

```sh
git clone https://github.com/mazenamr/args.git
```

##### 2 - Add it to your project folder

```sh
cp -r ./args ./myproject
```

##### 3 - Don't forget to give me credit :wink:

## Usage

### 1 - Importing The library

```py
import args
```

### 2 - Creating A Dictionary Of Arguments

```py
import args

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

userargs = args.getargs(allargs)
```

### 3 - Checking If All Required Arguments Exist

```py
import args, sys

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

userargs = args.getargs(allargs)

if not args.checkargs(["input", "interactive"], [i for i in userargs]):
    print("You must either provide an input file or choose the interactive mode!")
    sys.exit(7)
```

### 4 - Checking If Certain Groups Of Arguments Exist Together

```py
import args, sys

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

userargs = args.getargs(allargs)

if args.checkgroup(["verbose", "silent"], [i for i in userargs]):
    print("You can't use the verbose mode and silent mode together!")
    sys.exit(7)
```

## Modules

### 1 - getargs(args)

#### Description

Takes a dictionary of arguments as input in the form of {*Long Form*: *Short Form*}.

Returns a dictionary of user arguments and their parameters in the form of {*Long Form*: *Parameters*}.

#### Notes

+ The short form has to be only one letter long.

+ You can replace short form by None if no short form exists.

+ Arguments that take a parameter have to end with a column (:) in their long form.

+ Arguments that don't take a parameter are returned with a parameter value *None*.

#### Inputs

##### 1 - args

A dictionary of valid arguments. Form: {*Long Form*: *Short form*}

#### Output

A dictionary of user arguments and their parameters if required.
Form: {*Long Form*: *Parameters*}

#### Error Codes

+ 77 - Unknown argument.
+ 78 - No parameter for an argument that requires one.

#### Examples

```py
import args

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

print(getargs(allargs))

>>> {"input": "in.text",
     "output": "out.txt",
     "verbose": None}
```

### 2 - checkargs(args, userargs)

#### Description

Takes a list of args and checks if at least one of them exists.

Returns True or False.

#### Notes

+ If you use the output of getargs in userargs, be sure to provide arguments in the long form.

#### Inputs

##### 1 - args
A list of arguments which one of has to exist. Form: [*args*]

##### 2 - userargs
A list of arguments provided by the user. Form: [*args*]

#### Output

True of False

#### Examples

```py
import args, sys

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

userargs = args.getargs(allargs)

if not args.checkargs(["input", "interactive"], [i for i in usera]):
    print("You must either provide an input file or choose the interactive mode!")
    sys.exit(7)
```

### 3 - checkgroup(args, userargs)

#### Description

Takes a list of args and checks if all of them exist.

Returns True or False

#### Notes

+ If you use the output of getargs in userargs, be sure to provide arguments in the long form.

#### Inputs

##### 1 - args

A list of arguments that must all exist. Form: [*args*]

##### 2 - userargs

A list of arguments provided by the user.Form: [*args*]

#### Output

True or False

#### Examples

```py
import args, sys

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

userargs = args.getargs(allargs)

if args.checkgroup(["verbose", "silent"], [i for i in userargs]):
    print("You can't use the verbose mode and the silent mode together!")
    sys.exit(7)
```
## License

This library is licensed under the GNU Affero General Public License v3.0 - see [LICENSE](LICENSE) file for more details.
