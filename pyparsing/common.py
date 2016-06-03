# common pyparsing variables

from pyparsing import Literal, LineStart, LineEnd, Word, alphas

# general
colon = Literal(":")
start = LineStart()
end   = LineEnd()
at = Literal("@")
lessthan = Literal("<")
greaterthan = Literal(">")

# word related
word = Word(alphas)
worddot = Word(alphas+".")
