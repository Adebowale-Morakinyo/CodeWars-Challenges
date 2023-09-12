def solution(args):
    if not args:
        return ""

    result = []
    current_range = [args[0]]

    for i in range(1, len(args)):
        if args[i] == args[i - 1] + 1:
            current_range.append(args[i])
        else:
            if len(current_range) >= 3:
                result.append(f"{current_range[0]}-{current_range[-1]}")
            else:
                result.extend(map(str, current_range))
            current_range = [args[i]]

    if len(current_range) >= 3:
        result.append(f"{current_range[0]}-{current_range[-1]}")
    else:
        result.extend(map(str, current_range))

    return ",".join(result)
