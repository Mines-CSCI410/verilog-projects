from sys import argv

labels: list[str] = []
lines: list[list[str]] = []
with open(argv[1], 'r') as f:
    def split_line(line: str) -> list[str]:
        sections = map(lambda s: s.strip(), line.split('|'))
        valid_sections = filter(lambda s: len(s) > 0, sections)
        return list(valid_sections)
    lines = list(map(split_line, f.readlines()))
    labels = lines.pop(0)

for (test, line) in enumerate(lines):
    for (i, label) in filter(lambda t: t[1] != 'out' and t[1] != 'time', enumerate(labels)):
        if len(line[i]) > 1:
            print(f'{label} = \'b{line[i]};')
        else:
            print(f'{label} = {line[i]};')
    fmt_string = '|' + (' %d |' * len(labels))
    label_string = ", ".join(str(i) for i in labels)
    print(f'#{test} $display("{fmt_string}", {label_string})')
