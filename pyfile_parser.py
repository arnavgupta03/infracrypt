def get_lines(filename) -> list:
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def check_imports(lines) -> bool:
    return any([
        ('flask' in line or 'Flask' in line)
        for line in lines
        if (line.startswith('import') or line.startswith('from'))
    ])

def get_responses(i_lines) -> list:
    route_starts = [i for (i, line) in i_lines if line.startswith('@app.route')]
    return_lines = []
    for j, start in enumerate(route_starts[:-1]):
        return_lines.append([line for (i, line) in i_lines[start:route_starts[j + 1]] if line.startswith('return')])
    return_lines.append([line for (i, line) in i_lines[route_starts[-1]:] if line.startswith('return')])
    if len(return_lines) < 1:
        return 'No return statements found in file, file is invalid'
    return [line for line_group in return_lines for line in line_group]

def parse_and_return_responses(filename) -> list:
    lines = get_lines(filename)
    if not check_imports(lines):
        return 'No imports of flask found, file is invalid'
    indexed_lines = [(i, line) for i, line in enumerate(lines)]
    return get_responses(indexed_lines)
