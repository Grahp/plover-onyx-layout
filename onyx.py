from plover.system.english_stenotype import *

KEYS = (
  "A-", '#-',
  "+-", 'K-', 'S-', 'P-', 'T-', 'R-', 'L-',
  '^-',
  'J', 'E', 'I', 'U',
  '-V',
  '-R', '-L', '-N', '-F', '-G', '-P', '-T', '-S',
  '-D', '-Z'
)

IMPLICIT_HYPHEN_KEYS = ("J", "E", "I", "U")
## Dunno what this even means
SUFFIX_KEYS = ("-D", "-Z")
NUMBERS = {}
NUMBER_KEY = None
FERAL_NUMBER_KEY = False
UNDO_STROKE_STENO = "-V"

## Add Default keymaps
