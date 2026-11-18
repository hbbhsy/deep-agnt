def is_retryable(error):
    if getattr(error, 'status', None):
        if error.status in [429, 529]:
            return True
    return False
