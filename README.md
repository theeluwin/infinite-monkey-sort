# Infinite Monkey Sort

Simple integer sorting algorithm based on [infinite monkey theorem](http://en.wikipedia.org/wiki/Infinite_monkey_theorem).

## Usage

```python
from infinite_monkey_sort import monkey_sort
print(monkey_sort([1, 0, 3, 2]))  # will give [0, 1, 2, 3]
print(monkey_sort([1, 0, 3, 2], reverse=True))  # will give [3, 2, 1, 0]
```

## Test

Testing requires some additional packages (`flake8` is optional, though).

```bash
$ pip install nose nose-exclude flake8 coverage
```

Test with [nose](https://nose.readthedocs.io/).

```bash
$ nosetests --config=.noserc
```

Or, you can use docker.

```bash
$ docker build -t monkey_sort -f Dockerfile .
$ docker run monkey_sort
```

## Remark

Everything is untested.
