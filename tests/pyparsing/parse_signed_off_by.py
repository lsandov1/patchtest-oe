#!/usr/bin/python

# signed-off-by pyparsing definition
#
# Copyright (C) 2016 Intel Corporation
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from pyparsing import Literal, OneOrMore, Regex
from common import word, worddot, at, lessthan, greaterthan, start, end, colon

name = Regex('\S+.*(?= <)')
username = OneOrMore(worddot)
domain = OneOrMore(worddot)

# taken from https://pyparsing-public.wikispaces.com/Helpful+Expressions
email = Regex(r"(?P<user>[A-Za-z0-9._%+-]+)@(?P<hostname>[A-Za-z0-9.-]+)\.(?P<domain>[A-Za-z]{2,})")

email_enclosed = lessthan + email + greaterthan

signed_off_by_mark = Literal("Signed-off-by")
signed_off_by = start + signed_off_by_mark + colon + name + email_enclosed + end
