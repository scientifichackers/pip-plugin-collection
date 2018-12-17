# pip-plugin-collection

This adds the following packages as `pip` plugins. 
  - [pip-tools](https://github.com/jazzband/pip-tools/)
  - [pipdeptree](https://github.com/naiquevin/pipdeptree)
  - [pip-upgrader](https://github.com/simion/pip-upgrader/)
  
(Please raise an issue to see your favourite package added here!)

## Install

Run `$ pip install pip-plugin-collection`. After that you should see something like this-

```
$ pip --help
...
  completion                  A helper command used for command completion.
  help                        Show help for commands.

3rd Party Commands:
  upgrade
  tree
  compile
  sync

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
...
```

(You only need to install it once on the global python, and after that they should be available on virtualenvs too.)

## Known Issues
  - pipdeptree shows global packages by default. This means it's mandatory to use `pip tree -l` inside a virtualenv, or else it will show global packages too.

---

Made using [plugingen](https://github.com/pycampers/plugingen).

(This is a prof of concept for a [fork](https://github.com/devxpy/pip) of `pip` that supports plugins. Follow discussion [here](https://github.com/pypa/pip/issues/3999#issuecomment-447743331).)

