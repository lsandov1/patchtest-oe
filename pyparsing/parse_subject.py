# subject pyparsing definition

#
# This is an oversimplified syntax of the mbox's summary
#

from pyparsing import Word, alphanums, Literal, OneOrMore, printables, Optional

prefix        = "[" + Word(alphanums+"/,") + "]"
target        = Word(alphanums+"/_-.")
colon         = Literal(":")
summary       = OneOrMore(Word(printables))
subject       = Optional(prefix) + target + colon + summary
