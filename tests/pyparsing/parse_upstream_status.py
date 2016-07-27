#!/usr/bin/python

# upstream-status pyparsing definition
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


from common import start, end, colon
from pyparsing import Or, Literal

upstream_status_valid_status = Or([Literal(status) for status in ["Pending",
                                                                  "Submitted",
                                                                  "Accepted",
                                                                  "Backport",
                                                                  "Denied",
                                                                  "Inappropriate"]])
upstream_status_mark         = Literal("Upstream-Status")
upstream_status              = start + upstream_status_mark + colon + upstream_status_valid_status + end
