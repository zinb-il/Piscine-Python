# ft_package

`ft_package` est un Python package qui compte les occurrences de l'élément cible dans la table itérative.

## Build

using 'setup.py'

```
python3 setup.py sdist bdist_wheel
```

using 'pyproject.toml'

```
python3 -m pip install --upgrade build
python3 -m build
```

## Install

```
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Display

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
