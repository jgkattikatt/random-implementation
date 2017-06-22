#MY IMPLEMENTATION OF PYTHON STRING IN OPERATOR
#jgkattikatt@gmail.com

string = "Hello world, how are you ?"
pattern = "how"
len_pattern = len(pattern) - 1

def check_pattern():
    result = False
    first_char_match = False
    current_pattern_index = 0
    
    for char in string:
        if first_char_match:
            if char == pattern[current_pattern_index]:
                if first_char_match == len_pattern:
                    print 'Pattern Matched'
                    result = True
                    first_char_match = 0
                    first_char_match = False
                else: 
                    first_char_match += 1
        elif char == pattern[current_pattern_index]:
            first_char_match = True
            current_pattern_index += 1
    return result
       

if __name__ == '__main__':
    print check_pattern()

