def is_retryable(error):
    if getattr(error, 'status', None):
        if error.status in [429, 529]:
            return True
    return False


def backoff_delay(attempt, base=0.5):
    return base * 2 ** attempt
