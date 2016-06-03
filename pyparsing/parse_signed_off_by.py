# signed-off-by pyparsing definition

from pyparsing import Literal, OneOrMore
from common import word, worddot, at, lessthan, greaterthan, start, end, colon

name = OneOrMore(word)

username = OneOrMore(worddot)
domain = OneOrMore(worddot)
email = username + at + domain
email_enclosed = lessthan + email + greaterthan

signed_off_by_mark = Literal("Signed-off-by")
signed_off_by = start + signed_off_by_mark + colon + name + email_enclosed + end
