def ducci(input):
    if any(i != 0 for i in input):
        yield input
        new_input = []
        length = len(input)
        for i in range(length):
            new_input.append(abs(input[i]-input[(i+1)%length]))
        yield from ducci(new_input)
    else:
        yield [0]*len(input)

if __name__ == "__main__":
    try:
        x = ducci([10, 12, 41, 62, 31])
        steps = 0
        for i in x:
            print(i)
            steps += 1
        print(steps)
    except RecursionError:
        print('Repeating Pattern')


