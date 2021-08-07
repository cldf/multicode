
Releasing multicode
===================

- Do platform test via tox:
```
tox -r
```

- Make sure statement coverage is at 100%
- Make sure flake8 passes:
```
flake8 src
```

- Update the version number, by removing the trailing `.dev0` in:
  - `setup.py`
  - `pycldf/__init__.py`

- Bump version number:
```
git commit -a -m"bumped version number"
```

- Create a release tag:
```
git tag -a v<version> -m"first version to be released on pypi"
```

- Release to PyPI:
```shell
rm dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
```

- Push to github:
```
git push origin
git push --tags
```

- Change version for the next release cycle, i.e. incrementing and adding .dev0
  - `setup.py`
  - `src/multicode/__init__.py`

- Commit/push the version change:
```shell
git commit -a -m "bump version for development"
git push origin
```
