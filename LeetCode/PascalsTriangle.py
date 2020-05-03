

def triangle(num_rows):

    def generate_next(prev_row):
        next_row = [0] *(len(prev_row) + 1)
        next_row[0] = next_row[-1] = 1

        for i in range(1, len(prev_row)-1):
            next_val = prev_row[i] + prev_row[i - 1]
            next_row[i] = next_val
        return next_row

    output = []
    prev_row = []

    while len(output) < num_rows:
        next_row = generate_next(prev_row)
        output.append(next_row)
        prev_row = output[-1]
    return output

returned= triangle(5)
print(*returned, sep ="\n")

'''
i wanted to print the answer like a triangle and without None in the output.
and if i directly print the triangle function, you would get None in the output

time complexity : O(n)
space complexity : O(n)
'''