# flake8-annotations-coverage

An extension for flake8 to report on files with lot of code
without type annotations.

This is mostly useful when you add type annotations to existing
large codebase and want to know if new code in annotated modules
 is annotated.

Minimal annotations coverage percent for each file can be configured via
`--min-coverage-percents` option, default is 75.

Function is treated as annotated if it has annotation for at least
one argument or return type. This is enough for mypy to threat the function
not as dynamically typed.

## Installation

    pip install git+https://github.com/best-doctor/flake8-annotations-coverage.git


## Example

Sample file:

    # test.py

    def annotated_function(some_arg: int):
        pass


    def unannotated_function():
        pass

Usage:

    $ flake8 test.py
    test.py:0:1: TAE001 too few type annotations

Tested on Python 3.6.5 and flake8 3.7.4.
