def lines(file):
    for line in file: yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip(): #去除前后的空格
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []