from sys import argv
from re import match

labels: list[str] = []
lines: list[list[str]] = []
header_string = ""
with open(argv[1], 'r') as f:
    def split_line(line: str) -> list[str]:
        sections = map(lambda s: s.strip(), line.split('|'))
        valid_sections = filter(lambda s: len(s) > 0, sections)
        return list(valid_sections)
    header_string = f.readline().strip()
    lines = list(map(split_line, f.readlines()))
    labels = split_line(header_string)

print(f'$display("{header_string}")')
print()
for (test, line) in enumerate(lines):
    for (i, label) in filter(lambda t: t[1] != 'out' and t[1] != 'time', enumerate(labels)):
        if len(line[i]) > 1:
            print(f'{label} = \'b{line[i]};')
        else:
            print(f'{label} = {line[i]};')

    def strings(labels: list[str]) -> tuple[str, str]:
        fmt_string = '|' + (' %d |' * len(labels))
        label_string = ", ".join(str(i) for i in labels)
        return (fmt_string, label_string)

    if labels[0] == 'time':
        fmt_string, label_string = strings(list(filter(lambda s: s != 'time', labels)))
        if match('\\d+\\+', line[0]):
            time = int(line[0].removesuffix('+'))
            t_str = str(time) + '+'
            print(f'#{time * 2 + 1} $display("| {t_str:<4} {fmt_string}", {label_string})')
        else:
            time = int(line[0])
            print(f'#{time * 2} $display("| {time:<4} {fmt_string}", {label_string})')
    else:
        fmt_string, label_string = strings(labels)
        print(f'#{test} $display("{fmt_string}", {label_string})')
    print()
