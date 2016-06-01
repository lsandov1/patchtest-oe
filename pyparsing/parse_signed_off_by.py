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

mark = Literal("Signed-off-by")
colon = Literal(":")
signed_off_by = mark + colon + name + email
