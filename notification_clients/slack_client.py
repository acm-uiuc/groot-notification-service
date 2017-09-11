from slackclient import SlackClient as SlackAPIClient


class SlackClient:
    def __init__(self, slack_token):
        self.client = SlackAPIClient(slack_token)

    def send(self, message, recipients=None):
        for recipient in recipients:
            self.client.api_call(
                'chat.postMessage',
                channel=recipient,
                text=message
            )
