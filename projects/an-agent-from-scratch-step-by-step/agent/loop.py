def user_message(text):
    return {'role': 'user', 'content': text}


def results_message(results):
    return user_message(results)


def handle_tool_turn(reply, messages, tools):
    messages.append(assistant_message(reply))
    results = []

    for b in tool_uses(reply):
        result = run_tool(b, tools)
        results.append(result)

    messages.append(results_message(results))

    return results
