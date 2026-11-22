def cost_micros(input_tokens, output_tokens, price_in, price_out):
    return int(round(input_tokens * price_in + output_tokens * price_out))
