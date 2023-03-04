def check_imports(filename):
    import_lines = []
    with open(filename) as f:
        lines = f.readlines()
        import_lines = [
            ('flask' in line or 'Flask' in line) for line in lines if (line.startswith('import') or line.startswith('from'))
        ]
    return any(import_lines)
