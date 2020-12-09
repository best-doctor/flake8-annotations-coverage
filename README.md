# flake8-annotations-coverage

[![Build Status](https://travis-ci.org/best-doctor/flake8-annotations-coverage.svg?branch=master)](https://travis-ci.org/best-doctor/flake8-annotations-coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/8480286aaae1c0612351/maintainability)](https://codeclimate.com/github/best-doctor/flake8-annotations-coverage/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8480286aaae1c0612351/test_coverage)](https://codeclimate.com/github/best-doctor/flake8-annotations-coverage/test_coverage)

An extension for flake8 to report on files with a lot of code
without type annotations.

This is mostly useful when you add type annotations to existing
large codebase and want to know if new code in annotated modules
 is annotated.

Minimal annotations coverage percentage for each file can be configured via
`--min-coverage-percents` option, default is 75.

Function is treated as annotated if it has annotation for at least
one argument or return type. This is enough for mypy to threat the function
not as dynamically typed.

## Installation

```bash
pip install flake8-annotations-coverage
```

## Example

Sample file:

```python
# test.py

def annotated_function(some_arg: int):
    pass


def unannotated_function():
    pass
```

Usage:

```terminal
$ flake8 test.py
test.py:0:1: TAE001 too few type annotations
```

Tested on Python 3.6.5 and flake8 3.7.4.

## Error codes

| Error code | Description                      |
|:----------:|:--------------------------------:|
| TAE001     | Too few type annotations in file |

## Contributing

We would love you to contribute to our project. It's simple:

1. Create an issue with bug you found or proposal you have.
   Wait for approve from maintainer.
1. Create a pull request. Make sure all checks are green.
1. Fix review comments if any.
1. Be awesome.

Here are useful tips:

- You can run all checks and tests with `make check`.
  Please do it before TravisCI does.
- We use [BestDoctor python styleguide](https://github.com/best-doctor/guides/blob/master/guides/en/python_styleguide.md).
- We respect [Django CoC](https://www.djangoproject.com/conduct/).
  Make soft, not bullshit.
