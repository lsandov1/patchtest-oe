# signed-off-by pyparsing definition

from pyparsing import Literal, OneOrMore, Regex
from common import word, worddot, at, lessthan, greaterthan, start, end, colon

name = OneOrMore(worddot)

username = OneOrMore(worddot)
domain = OneOrMore(worddot)

# taken from https://pyparsing-public.wikispaces.com/Helpful+Expressions
email = Regex(r"(?P<user>[A-Za-z0-9._%+-]+)@(?P<hostname>[A-Za-z0-9.-]+)\.(?P<domain>[A-Za-z]{2,4})")

email_enclosed = lessthan + email + greaterthan

signed_off_by_mark = Literal("Signed-off-by")
signed_off_by = start + signed_off_by_mark + colon + name + email_enclosed + end
