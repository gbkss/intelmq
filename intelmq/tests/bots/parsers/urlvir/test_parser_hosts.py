# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import unittest

import intelmq.lib.test as test
from intelmq.bots.parsers.urlvir.parser_hosts import URLVirHostsParserBot


EXAMPLE_REPORT = {"feed.url": "http://www.urlvir.com/export-hosts/",
                  "raw": "IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj"
                         "IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiNVUkxWaXIgQWN0"
                         "aXZlIE1hbGljaW91cyBIb3N0cwojVXBkYXRlZCBvbiBBdWd1c3Qg"
                         "MTcsIDIwMTUsIDExOjI5IGFtCiNGcmVlIGZvciBub25jb21tZXJj"
                         "aWFsIHVzZSBvbmx5LCBjb250YWN0IHVzIGZvciBtb3JlIGluZm9y"
                         "bWF0aW9uCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj"
                         "IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwpleGFt"
                         "cGxlLm5ldA==",
                  "__type": "Report",
                  "feed.name": "URLVir"}
EXAMPLE_EVENT = {"feed.url": "http://www.urlvir.com/export-hosts/",
                 "feed.name": "URLVir",
                 "__type": "Event",
                 "source.fqdn": "example.net",
                 "classification.type": "malware",
                 "raw": "ZXhhbXBsZS5uZXQ=",
                 }


class TestURLVirHostsParserBot(test.BotTestCase, unittest.TestCase):
    """
    A TestCase for a URLVirHostsParserBot.
    """

    def reset_bot(self):
        self.bot_id = 'test-bot'
        self.bot_reference = URLVirHostsParserBot
        self.input_message = json.dumps(EXAMPLE_REPORT)
        super(TestURLVirHostsParserBot, self).reset_bot()

    def test_event(self):
        """ Test if correct Event has been produced. """
        self.reset_bot()
        self.run_bot()
        self.assertEventAlmostEqual(0, EXAMPLE_EVENT)


if __name__ == '__main__':
    unittest.main()
