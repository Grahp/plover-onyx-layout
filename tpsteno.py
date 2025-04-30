from plover.system.english_stenotype import *

KEYS = (
  '#-',
  "+-", 'K-', 'S-', 'P-', 'T-', 'R-', 'L-',
  'I', 'E', 'Y', 'U',
  '-*',
  '-R', '-L', '-N', '-F', '-G', '-P', '-T', '-S',
  '-D', '-Z'
)

## TODO orthography rules?
IMPLICIT_HYPHEN_KEYS = ("I", "E", "Y", "U")
## Dunno what this even means
SUFFIX_KEYS = ("-D", "-Z")
NUMBERS = {}
NUMBER_KEY = None
FERAL_NUMBER_KEY = False
UNDO_STROKE_STENO = "-*"
