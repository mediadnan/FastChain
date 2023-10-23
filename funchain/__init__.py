"""
FunChain is a package that provides tools for creating ready to use function chains,
the main goal is to ease chaining functions and capture errors without breaking the whole program.
the main user interface tools are Chain class, parse function and the two decorators chainable and funfact.
Chain is the main component, it parses the given model and creates the right execution structure.
it also takes a callback that takes a report as its only parameter.
chains are callables, they take an input and returns the last result.
"""
from .factory import nd
from .nodes import BaseNode, Severity, OPTIONAL, NORMAL, REQUIRED
from failures import Reporter   # shortcut # noqa # pylint: disable=unused-import

__version__ = '0.1.0'
