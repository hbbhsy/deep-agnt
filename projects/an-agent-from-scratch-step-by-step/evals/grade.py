def parse_trace_line(line):
    if not line.startswith('['):
        return
    
    n, rest = line.split(']', 1)
    n = int(n[1:])
    rest = rest.strip()

    return n, rest
