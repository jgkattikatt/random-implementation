#STRING REVERSAL IN PYTHON
#jgkattikatt@gmail.com

original_string = "Hello world"

def reverse_string(string):
    string = list(string)
    first = 0
    last = len(string) - 1

    while first <= last:
        string[first], string[last] = string[last], string[first]
        first += 1
        last -= 1
 
    string = ''.join((string))

    return string


if __name__ == '__main__':
    print reverse_string(original_string)
