"""
Here's a one-line regex replacement:

re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % val)
Works only for inegral outputs:

import re
val = 1234567890
re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % val)
# Returns: '1,234,567,890'

val = 1234567890.1234567890
# Returns: '1,234,567,890'
Or for floats with less than 4 digits, change the format specifier to %.3f:

re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%.3f" % val)
# Returns: '1,234,567,890.123'
NB: Doesn't work correctly with more than three decimal digits as it will attempt to group the decimal part:

re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%.5f" % val)
# Returns: '1,234,567,890.12,346'


-----------------------------------------------------------------------------------------------------------------


re.sub(pattern, repl, string)

pattern = \
    "(\d)           # Find one digit...
     (?=            # that is followed by...
         (\d{3})+   # one or more groups of three digits...
         (?!\d)     # which are not followed by any more digits.
     )",

repl = \
    r"\1,",         # Replace that one digit by itself, followed by a comma,
                    # and continue looking for more matches later in the string.
                    # (re.sub() replaces all matches it finds in the input)

string = \
    "%d" % val      # Format the string as a decimal to begin with
"""

import re

s = "12345678"
print(re.sub('(\d)(?=(\d{3})+(?!\d))', r'\1,', s))