def is_retryable(error):
    if getattr(error, 'status', None):
        if error.status in [429, 529]:
            return True
    return False


def backoff_delay(attempt, base=0.5):
    return base * 2 ** attempt


def retry_after(headers):
    if headers is not None:
        if headers.get('Retry-After'):
            if headers['Retry-After'].isdigit():
                return headers['Retry-After']
    return
