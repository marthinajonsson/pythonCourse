with open('files/words') as f:
    for line in f:
        line = line.rstrip()
        if len(line) == 1:
            continue
        if line[::-1] == line:
            print(line)