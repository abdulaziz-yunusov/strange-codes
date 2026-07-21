"""
quine.py
========
WHAT IS A QUINE?
A "Quine" (named after logician Willard Van Orman Quine) is a program that 
outputs an exact copy of its own source code without reading its source file 
from disk or accepting any user input.

THE QUINE PARADOX:
Writing a quine creates an infinite recursion problem:
  - To print the code, you need a string variable containing the source text.
  - But that string variable MUST ALSO contain the string variable itself!
  - A string inside a string inside a string... ad infinitum.

THE ELEGANT SOLUTION:
We solve this by separating the program into two distinct layers:
  1. DATA LAYER : A single template string (`s`) containing code placeholders.
  2. CODE LAYER : A formatting engine that passes `s` into ITSELF.

KEY PYTHON TRICKS USED:
  - `%r` : Calls Python's internal `repr()`, which automatically wraps 
          strings in quote marks (`'...'`). This quotes the string without us
          having to write literal quote marks inside the data layer.
  - `\n` : Literal newline character dividing Line 1 and Line 2.
  - `%%` : Escapes the `%` character so Python treats it as a literal `%` 
          instead of a formatting operator during evaluation.
"""

# =====================================================================
# LINE 1: THE DATA LAYER (THE BLUEPRINT)
# =====================================================================
# `s` is a template containing placeholders (%r, \n, %%) that describe 
# both Line 1 AND Line 2 of this script simultaneously.
s = 's = %r\nprint(s %% s)'


# =====================================================================
# LINE 2: THE CODE LAYER (SELF-REPLICATION)
# =====================================================================
# We evaluate `s % s` (formatting string `s` using `s` as its own argument).
#
# HOW `s % s` EVALUATES AT RUNTIME:
# 
# 1. `%r` is replaced by `repr(s)`:
#    repr('s = %r\nprint(s %% s)') -> "'s = %r\\nprint(s %% s)'"
#    *(Notice how `repr()` dynamically added quote marks around `s`!)*
#
# 2. `\n` is evaluated as a physical newline break.
#
# 3. `%%` is evaluated as a single literal `%` character.
#
# COMBINED EVALUATION OUTPUT:
#   Line 1 generated -> s = 's = %r\nprint(s %% s)'
#   Line 2 generated -> print(s % s)
#
# The output sent to stdout matches this file's code char-for-char!
print(s % s)
