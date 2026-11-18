def text_blocks(response):
    result = []
    if 'content' in response.keys():
        for i, block in enumerate(response['content']):
            if block['type'] == 'text':
                result.append(block['text'])
    return result


def text_of(response):
    text = text_blocks(response)
    res = '\n'.join(text)
    return res.strip()


def tool_uses(response):
    res = []
    if 'content' in response.keys():
        for i, b in enumerate(response['content']):
            if b['type'] == 'tool_use':
                res.append(b)
    return res


def wants_tool(response):
    if response.get('stop_reason'):
        if response['stop_reason'] == 'tool_use':
            return True
    return False


def assistant_message(response):
    res = {'role': 'assistant'}
    if response.get('content'):
        res['content'] = response['content']
    else:
        res['content'] = []
    return res
