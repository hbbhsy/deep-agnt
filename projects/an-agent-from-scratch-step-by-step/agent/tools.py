def param_schema(kind, description):
    return {'type': kind, 'description': description}


def required_params(params):
    res = []
    for k, v in params.items():
        if v[2] == True:
            res.append(k)
    return res


def tool_spec(name, description, params):
    properties = {}
    for k,v in params.items():
        properties[k] = param_schema(v[0], v[1])

    return {'name': name, "description": description,
            'input_schema': {
                "type": 'object', 
                "properties":properties, 
                'required':required_params(params)
                }
            }


def tool_result(tool_use_id, content, is_error=False):
    res = {"type": "tool_result"}
    res['tool_use_id'] = tool_use_id
    res['content'] = str(content)
    if is_error:
        res['is_error'] = True
    return res
