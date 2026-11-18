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
