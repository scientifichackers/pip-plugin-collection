import plugingen

__version__ = "0.0.1"

upgrade = plugingen.create(
    "from pip_upgrader.cli import main\nmain()", ["pip_upgrader"]
)
tree = plugingen.create("import pipdeptree\npipdeptree.main()", ["pipdeptree"])

_pip_tools_template = "from piptools.scripts import {name}\n{name}.cli()"
compile = plugingen.create(
    _pip_tools_template.format(name="compile"), ["piptools"]
)
sync = plugingen.create(
    _pip_tools_template.format(name="sync"), ["piptools"]
)
