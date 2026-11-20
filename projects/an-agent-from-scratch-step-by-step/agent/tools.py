def param_schema(kind, description):
    return {'type': kind, 'description': description}


def required_params(params):
    res = []
    for k, v in params.items():
        if v[2] == True:
            res.append(k)
    return res
