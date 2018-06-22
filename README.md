# disport

Like ``python -m dis``, but with imports.

When invoked as a script, the ``dis`` module lets you disassemble a python file.
This script works similarly, but with imports, so that you can disassemble
modules, classes, functions, and other code objects.

Imports are specified with the same syntax that setuptools use for entry points:
``<module>[.<submodule>][:<name>[.<attr>]]``.

Example:

```
python -m disport os.path:exists
```
