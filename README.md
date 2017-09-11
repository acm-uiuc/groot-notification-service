# groot-notification-service 📣
Notification service for Twitter, Email and Slack Endpoints

[![Build Status](https://travis-ci.org/acm-uiuc/groot-notification-service.svg?branch=master)](https://travis-ci.org/acm-uiuc/groot-notification-service)

[![Join the chat at https://acm-uiuc.slack.com/messages/C6XGZD212/](https://img.shields.io/badge/slack-groot-724D71.svg)](https://acm-uiuc.slack.com/messages/C6XGZD212/)

## Install / Setup
1. Clone repo:

    ```
    git clone https://github.com/acm-uiuc/groot-notification-service
    cd groot-notification-service
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Copy settings template:

    ```
    cd groot_notification_service
    cp settings.template.py settings.py
    ```

4. Add your DB credentials to settings.py.

## Run Application
```
python app.py
```

## Routes

### POST /notification

Sends a message to the provided list of services / recipients

*Body Params:*

* `services` - List of services to send the notification to
    * Required
* `message` - The message to be sent in the body of the notification
    * Required

*Service Schemas:*

- **Slack**

    ```
    {
        "name": "slack",
        "recipients": [<LIST_OF_CHANNELS_OR_USERS>]
    }
    ```

- **Email**

    ```
    {
        "name": "slack",
        "sender": "<SENDER_EMAIL_ADDRESS>",
        "subject": "<EMAIL_SUBJECT>",
        "recipients": [<LIST_OF_RECIPIENT_EMAIL_ADDRESSES>]
    }
    ```

- **Twitter**

    ```
    {
        "name": "twitter"
    }
    ```

*Example Request:*
```
{
    "services": [
        {
            "name": "twitter"
        },
        {
            "name": "slack",
            "recipients": ["#general"]
        },
        {
            "name": "email",
            "recipients": ["foo@illinois.edu"],
            "sender": "admin@acm.illinois.edu",
            "subject": "Urgent Message"
        }
    ],
    "message": "Come clean up the office at 2pm today!" 
}
```

## Contributing

Contributions to `groot-notification-service` are welcomed!

1. Fork the repo.
2. Create a new feature branch.
3. Add your feature / make your changes.
4. Install [pep8](https://pypi.python.org/pypi/pep8) and run `pep8 *.py` in the root project directory to lint your changes. Fix any linting errors.
5. Create a PR.
6. ???
7. Profit.
