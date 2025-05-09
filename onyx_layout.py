from plover.system.english_stenotype import *

KEYS = (
  "A-", '#-',
  "+-", 'K-', 'S-', 'P-', 'T-', 'R-', 'L-',
  '^-',
  'J', 'E', 'I', 'U',
  '-V',
  '-R', '-L', '-K', '-P', '-T', '-S',
  '-D', '-Z', '-Y', '-W'
)

IMPLICIT_HYPHEN_KEYS = ("J", "E", "I", "U")
SUFFIX_KEYS = ("-V", "-D", "-Z", "-Y", "-W")
NUMBERS = {}
NUMBER_KEY = None
FERAL_NUMBER_KEY = False
UNDO_STROKE_STENO = "-V"

## Add Default keymaps
