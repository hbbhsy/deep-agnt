def cost_micros(input_tokens, output_tokens, price_in, price_out):
    return int(round(input_tokens * price_in + output_tokens * price_out))


class Budget:
    def __init__(self):
        self.calls = 0
        self.tokens = 0

    def record(self, input_tokens, output_tokens):
        self.calls += 1
        self.tokens += (input_tokens + output_tokens)


def exceeded(budget, max_calls=None, max_tokens=None):
    if max_calls and budget.calls > max_calls:
        return f'calls: {budget.calls} of {max_calls}'
    elif max_tokens and budget.tokens > max_tokens:
        return f'tokens: {budget.tokens} of {max_tokens}'
    else:
        return
