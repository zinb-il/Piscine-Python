# ft_package

`ft_package` is a Python package that provides a function to count occurrences of an element in an iterable.

## Build

using 'setup.py'

```
python3 setup.py sdist bdist_wheel
```

using 'pyproject.toml'

For Linux:
```
python3 -m pip install --upgrade build
python3 -m build
```

## Install

```
pip install ./dist/ft_package-0.0.1.tar.gz
```
Or 
```
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## More informations about the package

```
pip show -v ft_package
```

## Uninstall

```
pip uninstall ft_package
```

## Testing

```
python3 tests/test_count_in_list.py
```
