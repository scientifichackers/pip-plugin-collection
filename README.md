# pip-plugin-collection

This adds the following packages as `pip` plugins. 
  - [pip-tools](https://github.com/jazzband/pip-tools/)
  - [pipdeptree](https://github.com/naiquevin/pipdeptree)
  - [pip-upgrader](https://github.com/simion/pip-upgrader/)
  
Please raise an issue to see your favourite package added here!

## Known Issues
  - pipdeptree shows global packages by default. This means it's mandatory to use `pip tree -l` inside a virtualenv, or else it will show global packages too.

---

Made using [plugingen](https://github.com/pycampers/plugingen).

(This is a proof of concept for a [fork](https://github.com/devxpy/pip) of `pip` that supports plugins.)
