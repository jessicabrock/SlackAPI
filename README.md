# SlackAPI

Flask app to learn how to use the Slack API.

## Requirements
1. Python 3.x
2. A free Slack account with API access
3. Slack testing token
4. Flask web framework

### Want to use this project?

Get a Slack API testing token from here:
https://api.slack.com/slack-apps

$ pip install pipenv
$ pipenv install slackclient
$ pipenv shell
$ export SLACK_TOKEN="<your token goes here>"
$ pipenv run python app.py



## Basics

1. Fork/Clone git repo
2. Follow instructions above

## Testing Your Token

Open Python at the command prompt:
$ python
>>> from slackclient import SlackClient
>>> sc = SlackClient('enter test token here')
>>> sc.api_call("api.test")
{'ok': True,...}

If you get False check your testing token.

Next check for authorization to the Slack account:
>>> sc.api_call("auth.test")
{'ok': True, 'url': 'https://pygirls.slack.com/', 'team': 'PyGirls', 'user':  'jessicabrock03', 'team_id': 'T8FCP5E8K',...}

