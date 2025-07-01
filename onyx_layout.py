from plover.system.english_stenotype import *

KEYS = (
  "A-", "+-",
  "*-", "T-", "S-", "P-", "K-", "L-", "R-",
  "Y", "E", "I", "U", "^",
  "-L", "-R", "-P", "-K", "-T", "-S", "*",
  "-r", "-d", "-s"
)

IMPLICIT_HYPHEN_KEYS = ("Y", "E", "I", "U", "^")
SUFFIX_KEYS = ("+", "A", "A+", "-r", "-d", "-s", "-rs", "-rd", "-ds", "-rds", "+-r", "+-d", "+-s", "+-rs", "+-rd", "+-ds", "+-rds", "A-r", "A-d", "A-s", "A-rs", "A-rd", "A-ds", "A-rds", "A+-r", "A+-d", "A+-s", "A+-rs", "A+-rd", "A+-ds", "A+-rds")
NUMBERS = {}
NUMBER_KEY = None
FERAL_NUMBER_KEY = False
UNDO_STROKE_STENO = "-R"

## Add Default keymaps
