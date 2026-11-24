def parse_trace_line(line):
    if not line.startswith('['):
        return
    
    n, rest = line.split(']', 1)
    n = int(n[1:])
    rest = rest.strip()

    return n, rest



def turn_stats(summary):
    res = []
    turns = {}

    for line in summary.splitlines():
        parsed = parse_trace_line(line)

        if parsed is None:
            continue

        n, rest = parsed

        if n not in turns:
            turns[n] = {
                "turn": n,
                "stop": None,
                "in": None,
                "out": None,
                "errors": 0
            }

        if rest.startswith("> tool_result error"):
            turns[n]["errors"] += 1

        elif rest.startswith("stop="):
            result = dict(
                item.split("=", 1)
                for item in rest.split()
            )

            turns[n]["stop"] = result["stop"]
            turns[n]["in"] = int(result["in"])
            turns[n]["out"] = int(result["out"])

    for n in sorted(turns):
        res.append(turns[n])

    return res


def first_error_turn(summary):
    traces = turn_stats(summary)
    for t in traces:
        if t['errors'] > 0:
            return t['turn']
        else:
            continue
    return


def total_calls(summary):
    if summary == "":
        return 0

    lines = summary.splitlines()
    for line in lines:
        if line.startswith('total calls='):
            res = line.split('=')[1]
            return int(res.split()[0])
    return 0
