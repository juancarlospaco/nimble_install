# Nimble integration for Python PIP

- Install [Nim](http://nim-lang.org) packages directly from [Python PIP](https://pypi.org/project/nimble-install). https://pypi.org/project/nimble-install

![](https://img.shields.io/github/languages/top/juancarlospaco/nimble_install?style=for-the-badge)
![](https://img.shields.io/github/stars/juancarlospaco/nimble_install?style=for-the-badge "Star faster-than-requests on GitHub!")
![](https://img.shields.io/maintenance/yes/2020?style=for-the-badge "2020")
![](https://img.shields.io/github/languages/code-size/juancarlospaco/nimble_install?style=for-the-badge)
![](https://img.shields.io/github/issues-raw/juancarlospaco/nimble_install?style=for-the-badge "Bugs")
![](https://img.shields.io/github/last-commit/juancarlospaco/nimble_install?style=for-the-badge "Commits")


# Use

Uses [Python PIP](https://pypi.org/project/nimble-install) `--install-option=`, 
there you can pass [Nim](http://nim-lang.org) packages separated by comma.

You can install [Frontend packages](https://mildred.github.io/nclearseam) to use with a Python Backend directly from PIP.
You can install [Nimpy](https://github.com/yglukhov/nimpy) directly from PIP.

```console
$ pip install nimble_install --install-option="--nimble=contra"
Skipping wheel build for nimble-install, due to binaries being disabled for it.
Installing collected packages: nimble-install
  running install
  Downloading https://github.com/juancarlospaco/nim-contra using git
    Verifying dependencies for contra@0.2.5
    Installing contra@0.2.5
      Prompt: contra@0.2.5 already exists. Overwrite? -> [forced yes]
      Success: contra installed successfully.

  CompletedProcess(args='nimble --accept --noColor install contra', returncode=0)

  Running setup.py install for nimble-install... done
Successfully installed nimble-install-0.0.1

$
```

**Examples:**

```
pip install nimble_install --install-option="--nimble=nimpy"
```

```
pip install nimble_install --install-option="--nimble=gatabase,nimterlingua"
```

```
pip install nimble_install --install-option="--nimble=compiler"
```


# More Info

- [**For Python Developers.**](https://github.com/nim-lang/Nim/wiki/Nim-for-Python-Programmers#table-of-contents)


# Requisites

- [Nim](http://nim-lang.org)


# Extras

- https://github.com/juancarlospaco/faster-than-requests#faster-than-requests
- https://github.com/juancarlospaco/faster-than-csv#faster-than-csv
- https://github.com/juancarlospaco/faster-than-walk#faster-than-walk
- https://github.com/juancarlospaco/choosenim_install
