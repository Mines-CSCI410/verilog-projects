from sys import argv
from os import path
from re import match

input_filepath = argv[1]
input_filename_module = path.basename(input_filepath).removesuffix('.cmp')

labels: list[str] = []
lines: list[list[str]] = []
header_string = ""
with open(input_filepath, 'r') as f:
    def split_line(line: str) -> list[str]:
        sections = map(lambda s: s.strip(), line.split('|'))
        valid_sections = filter(lambda s: len(s) > 0, sections)
        return list(valid_sections)
    header_string = f.readline().strip()
    lines = list(map(split_line, f.readlines()))
    labels = split_line(header_string)

def strings(labels: list[str]) -> tuple[str, str]:
    fmt_string = '|'
    for _ in labels:
        fmt_string += f'%b|'
    label_string = ', '.join(str(l) for l in labels)
    return (fmt_string, label_string)

timeless = lambda l: list(filter(lambda s: s != 'time', l))
outless = lambda l: list(filter(lambda s: s != 'out', l))

print(f'module {input_filename_module}_test;')
print(f'  reg {', '.join(str(l) for l in timeless(outless(labels)))};')
print(f'  wire out;\n')
print(f'  student_{input_filename_module} dut ({', '.join(f'.{l}({l})' for l in timeless(labels))});\n')

print('  initial begin')
print(f'    $display("{header_string.replace(' ', '')}");\n')

for (test, line) in enumerate(lines):
    for (i, label) in filter(lambda t: t[1] != 'out' and t[1] != 'time', enumerate(labels)):
        if len(line[i]) > 1:
            print(f'    {label} = \'b{line[i]};')
        else:
            print(f'    {label} = {line[i]};')

    if labels[0] == 'time':
        fmt_string, label_string = strings(timeless(labels))
        if match('\\d+\\+', line[0]):
            time = int(line[0].removesuffix('+'))
            t_str = str(time) + '+'
            print(f'    #{time * 2 + 1} $display("|{t_str}{fmt_string}", {label_string})')
        else:
            time = int(line[0])
            print(f'    #{time * 2} $display("|{time}{fmt_string}", {label_string})')
    else:
        fmt_string, label_string = strings(labels)
        print(f'    #{test + 1} $display("{fmt_string}", {label_string});')
    print()

print('    $finish;')
print('  end')
print('endmodule')
