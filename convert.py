from sys import argv
from os import path
from re import match
from dataclasses import dataclass

@dataclass
class Label:
    name: str
    input: bool
    width: int
    format: str
    
    @staticmethod
    def format_string(labels) -> str:
        return '|' + '|'.join(f'%{l.format}' for l in labels) + '|'

    @staticmethod
    def parameters(labels) -> str:
        return ', '.join(l.name for l in labels)

    @staticmethod
    def defs(labels) -> str:
        d = {l.typ():[] for l in labels}
        for l in labels:
            d[l.typ()].append(l)
        res = ''
        for (k, v) in d.items():
            names = ', '.join(l.name for l in v)
            res += indented(f'{k} {names};\n')
        return res
    
    def typ(self):
        io = 'reg' if self.input else 'wire'
        return io + f' [{self.width - 1}:0]' if self.width != 1 else io
    
    def is_time(self):
        return self.name == 'time'

    def not_time(self):
        return self.name != 'time'

    def is_input(self):
        return self.input

    def is_output(self):
        return not self.input

global_time = 1
default_time = object()
def display(labels, time = default_time, t_str = ''):
    global global_time
    if time is default_time:
        time = global_time
    print_indented(f'#{time} $display("{t_str}{Label.format_string(labels)}", {Label.parameters(labels)});')
    global_time += 1

time_field = False
def read_cmp_file(filepath: str):
    labels: list[Label] = []
    lines: list[list[str]] = []
    header_string = ""
    with open(filepath, 'r') as file:
        def split_line(line: str) -> list[str]:
            sections = map(lambda s: s.strip(), line.split('|'))
            valid_sections = filter(lambda s: len(s) > 0, sections)
            return list(valid_sections)

        header_string = file.readline().strip().replace(' ', '')
        for name in split_line(header_string):
            if name == 'time':
                global time_field
                time_field = True
                continue
            [label_type, label_width, label_basefmt] = input(f'{name} (in/out bits basefmt): ').split(' ')
            labels.append(Label(name, label_type == 'in', int(label_width) if label_basefmt != 'd' else 32, label_basefmt))
        lines = list(map(split_line, file.readlines()))
    return labels, lines, header_string

indent_level = 0
def indent(l = 2):
    global indent_level
    indent_level += l
def unindent(l = 2):
    global indent_level
    indent_level -= l
def indented(s: str) -> str:
    return ' ' * indent_level + s
def print_indented(s: str):
    print(indented(s))

input_filepath = argv[1]
input_filename_module = path.basename(input_filepath).removesuffix('.cmp')

labels, lines, header_string = read_cmp_file(input_filepath)

print_indented(f'module {input_filename_module}_test;')
indent()
print(Label.defs(labels))
print_indented(f'student_{input_filename_module} dut ({', '.join(f'.{l.name}({l.name})' for l in labels)});\n')

print_indented('initial begin')
indent()
print_indented(f'$display("{header_string}");\n')

for line in lines:
    for (i, l) in filter(lambda t: t[1].is_input(), enumerate(labels)):
        print_indented(f'{l.name} = \'{l.format}{line[i + time_field]};')

    if time_field:
        if match('\\d+\\+', line[0]):
            time = int(line[0].removesuffix('+'))
            t_str = '|' + str(time) + '+'
            display(labels, time, t_str)
        else:
            display(labels, int(line[0]), line[0])
    else:
        display(labels)
    print()

print_indented('$finish;')
unindent()
print_indented('end')
unindent()
print_indented('endmodule')
