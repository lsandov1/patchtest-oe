import sys, os

# New test cases should inherit from OEbase
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from oebase import OEBase, info

class Sample(OEBase):

    def test_mbox(self):
        """Sample code demonstrating data extraction from mbox data"""

        # Sample.mbox is an object containing the mbox data
        # Check https://docs.python.org/2/library/mailbox.html#mbox

        # loop through all messages and print keys/values
        # https://docs.python.org/2/library/email.message.html#module-email.message
        for message in Sample.mbox:
            for k,v in message.items():
                info('%s = %s' % (k,v))
            else:
                info('')

        # loop through all messages in the series and print the payload length
        # https://docs.python.org/2/library/email.message.html#module-email.message
        for message in Sample.mbox:
            payload = message.get_payload()
            info('%s %s' % (message['Message-Id'], len(payload)))
        else:
            info('')

        # Use any TestCase assertion method that fit to your needs
        self.fail('Sample code, failing intentionally')

    def test_patchset(self):
        """Sample code demonstrating data extraction from diff data"""

        # Sample.patchset is an object containing diff data
        # Check https://pypi.python.org/pypi/unidiff

        # Loop through all patches and print path and number of additions/deletions
        for patch in Sample.patchset:
            info('%s %s %s' % (patch.path, patch.added, patch.removed))
        else:
            info('')

        # Loop through all patches and print length
        for patch in Sample.patchset:
            diffdata = str(patch)
            info('%s %s' % (patch.path, len(diffdata)))
        else:
            info('')

        # Use any TestCase assertion method that fit to your needs
        self.fail('Sample code, failing intentionally')

