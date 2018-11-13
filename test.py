""" Unit Testing SlackAPI app """
import unittest
import app

class TestApp(unittest.TestCase):

    def test_token(self):
        """ test Slack token """
        sc = app.SlackClient(app.os.getenv('SLACK_TOKEN'))
        self.assertTrue(sc.api_call("api.test"), 'ok')

    def test_auth(self):
        """ test authorization """
        sc = app.SlackClient(app.os.getenv('SLACK_TOKEN'))
        self.assertTrue(sc.api_call("auth.test"), 'ok')

    def test_channel_listing(self):
        """ test retrieving channel listing """
        channels_call = app.SLACK_CLIENT.api_call("channels.list")
        get_channels = channels_call.get('ok')
        self.assertTrue(get_channels,'ok')

    def test_get_channel(self):
        channel_info = app.SLACK_CLIENT.api_call("channels.info")
        self.assertTrue(channel_info.get('ok'))
        # self.assertIn(channel_info,'C8EV35W3B') # channel_info is DICT

    def main():
        """ entry point """
        test_token
        test_auth
        test_channel_listing
        test_get_channel

if __name__ == '__main__':
    unittest.main()
