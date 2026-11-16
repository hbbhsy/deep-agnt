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
