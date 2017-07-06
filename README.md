# Args

## About

A Python 3 library for handling command line arguments.

## Getting Started

### Prerequisites

Python 3 or newer.

### Installation

#### For A System-wide Installation

##### 1 - Download [**args.py**](args.py)

```sh
curl -o args.py https://raw.githubusercontent.com/mazenamr/args/master/args.py
```

##### 2 - Copy [**args.py**](args.py) To One Of Your *Python Paths*

```sh
cp ./args.py /usr/lib/python3.6
```

###### To View Your Python Paths

```py
from system import path
print(path)
```

#### For Usage Within A Project

##### 1 - Download [**args.py**](args.py)

```sh
curl -o args.py https://raw.githubusercontent.com/mazenamr/args/master/args.py
```

##### 2 - Copy [**args.py**](args.py) To Your Project's Directory

```sh
cp -r ./args.py ./myproject
```

##### 3 - Don't Forget To Mention Me! :wink:

## Usage

### 1 - Importing The Library

```py
import args
```

### 2 - Getting The User's Arguments And Their Parameters

```py
import args

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

args.setargs(allargs)
print(args.argvalues)

>>> {"input": ["in.txt"],
     "output": ["out.txt"],
     "verbose": None}
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

args.setargs(allargs)

if not args.checkargs(["input", "interactive"]):
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

args.setargs(allargs)

if args.checkgroup(["verbose", "silent"]):
    print("You can't use the verbose mode and silent mode together!")
    sys.exit(7)
```

## Modules

### 1 - setargs(allargs)

#### Description

Takes a dictionary of arguments as input in the form of { *Long Form*: *Short Form* }. and updates **argvalues** (**args.argvalues**) with the arguments *in the long form* and a list of their parameters.

> { *Long Form*: [ *Parameters* ] }

#### Notes

+ The short form has to be only one letter long.

+ The short form is case sensitive.

+ Enter *None* instead of a short form is a short form doesn't exist.

+ Arguments that take a parameter have to end with a column (:) in their long form.

+ Arguments can take more than one parameter through adding multiple columns (:) in their long form.

+ Arguments that don't take a parameter are returned with a parameter value *None*.

#### Inputs

##### allargs

A dictionary of valid arguments.

> { *Long Form*: *Short Form* }

#### Error Codes

+ 77 - The *short form* of the argument is longer than one character.

+ 78 - An argument is provided by the user in the place of a parameter.

+ 79 - A parameter is provided by the user in the place of an argument.

+ 80 - An Unknown argument is provided by the user.

+ 81 - The user didn't provide enough parameters for an argument.

#### Examples

```py
import args

allargs = {"help": 'h',
           "input:": 'i',
           "interactive": None,
           "output:": 'o',
           "verbose": 'v',
           "silent": 's'}

args.setargs(allargs)
print(args.argvalues)

>>> {"input": ["in.txt"],
     "output": ["out.txt"],
     "verbose": None}
```

### 2 - checkargs(args)

#### Description

Takes a list of args and checks if at least one of them exists and returns True or False.

#### Notes

+ The arguments should be *in the long form*.

+ Don't add columns (:) for arguments that take parameters.

#### Inputs

##### args

A list of arguments that you want to check if any of them exist.

> [ *Long Form* ]

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

args.setargs(allargs)

if not args.checkargs(["input", "interactive"]):
    print("You must either provide an input file or choose the interactive mode!")
    sys.exit(7)
```

### 3 - checkgroup(args)

#### Description

Takes a list of args and checks if all of them exist and returns True or False.

#### Notes

+ The arguments should be in the long form.

+ Don't add columns (:) for arguments that take parameters.

#### Inputs

##### args

A list of arguments that you want to check if all of them exist.

> [ *Long Form* ]

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

args.setargs(allargs)

if args.checkgroup(["verbose", "silent"]):
    print("You can't use the verbose mode and the silent mode together!")
    sys.exit(7)
```
## License

This library is licensed under the GNU Affero General Public License v3.0 - see [**LICENSE**](LICENSE) file for more details.
