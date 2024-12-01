import os
import sentry_sdk

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
)

sentry_sdk.capture_message('My first capture message!')
