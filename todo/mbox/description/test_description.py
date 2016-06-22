import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from oembox import OEMBox
import mboxmsg as msg

class OEDescription(OEMBox):

    def test_description_presence(self):
        raise self.fail(self.formaterror(msg.test_description_presence.reason,
                                         msg.test_description_presence.error,
                                         msg.test_description_presence.fix,
                                         status='TODO'))


