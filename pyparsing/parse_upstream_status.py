# upstream-status pyparsing definition

from pyparsing import Literal, Or

colon                        = Literal(":")
upstream_status_valid_status = Or([Literal(status) for status in ["Pending",
                                                                  "Submitted",
                                                                  "Accepted",
                                                                  "Backport",
                                                                  "Denied",
                                                                  "Inappropriate"]])
upstream_status_mark         = Literal("Upstream-Status")
upstream_status              = upstream_status_mark + colon + status
