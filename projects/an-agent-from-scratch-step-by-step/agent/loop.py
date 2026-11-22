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


def run_agent(task, model, tools, specs, max_turns=6):
    messages = [user_message(task)]
    for i in range(max_turns):
        reply = model.chat(messages, tools=specs)
        if wants_tool(reply):
            results = handle_tool_turn(reply, messages, tools)
            # return results
        else:
            return text_of(reply)
    return
