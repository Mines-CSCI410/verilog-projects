from sys import argv
from re import match

labels: list[tuple[str, int]] = []
lines: list[list[str]] = []
header_string = ""
with open(argv[1], 'r') as f:
    def split_line(line: str) -> list[str]:
        sections = map(lambda s: s.strip(), line.split('|'))
        valid_sections = filter(lambda s: len(s) > 0, sections)
        return list(valid_sections)
    header_string = f.readline().strip()
    lines = list(map(split_line, f.readlines()))
    widths = list(map(lambda s: len(s) - 2, filter(lambda s: len(s) > 0, header_string.split('|'))))
    l = split_line(header_string)
    labels = list(zip(l, widths))

print(f'$display("{header_string}")')
print()
for (test, line) in enumerate(lines):
    for (i, (label, _)) in filter(lambda t: t[1] != 'out' and t[1] != 'time', enumerate(labels)):
        if len(line[i]) > 1:
            print(f'{label} = \'b{line[i]};')
        else:
            print(f'{label} = {line[i]};')

    def strings(labels: list[tuple[str, int]]) -> tuple[str, str]:
        fmt_string = '|'
        for (_, w) in labels:
            fmt_string += f' {'%d':<{w+1}} |'
        label_string = ", ".join(str(l) for (l, _) in labels)
        return (fmt_string, label_string)

    if labels[0][0] == 'time':
        fmt_string, label_string = strings(list(filter(lambda s: s[0] != 'time', labels)))
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
