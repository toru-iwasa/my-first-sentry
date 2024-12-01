import os
import sentry_sdk

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
)

try:
    raise Exception("My first capture exception!")
except Exception as e:
    sentry_sdk.capture_exception(e)
