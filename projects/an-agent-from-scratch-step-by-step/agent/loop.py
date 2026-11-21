def user_message(text):
    return {'role': 'user', 'content': text}


def results_message(results):
    return user_message(results)
