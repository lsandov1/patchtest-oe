# signed-off-by pyparsing definition

from pyparsing import Word, alphas, Literal, OneOrMore

word = Word(alphas)
name = OneOrMore(word)

worddot = Word(alphas+".")
username = OneOrMore(worddot)
domain = OneOrMore(worddot)
at = Literal("@")
lessthan = Literal("<")
greaterthan = Literal(">")
email = lessthan + username + at + domain + greaterthan

signed_off_by_mark = Literal("Signed-off-by")
colon = Literal(":")
signed_off_by = signed_off_by_mark + colon + name + email
