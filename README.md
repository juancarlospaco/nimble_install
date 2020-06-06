# Nimble integration for Python PIP

- Install [Nim](http://nim-lang.org) packages directly from [Python PIP](https://pypi.org/project/nimble-install). https://pypi.org/project/nimble-install

# Use

Uses PIP `--install-option=`, there you can pass [Nim](http://nim-lang.org) packages separated by comma.
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


# Requisites

- [Nim](http://nim-lang.org)


# More Info

- [**For Python Developers.**](https://github.com/nim-lang/Nim/wiki/Nim-for-Python-Programmers#table-of-contents)
