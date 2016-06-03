# upstream-status pyparsing definition

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
