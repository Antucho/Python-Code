# Token counters
keyword_count = 0
identifier_count = 0
operator_count = 0
integer_count = 0
invalid_identifier_count = 0

# Helper functions
def is_valid_delimiter(ch):
    return ch in [' ', '+', '-', '*', '/', ',', ';', '>', '<', '=', '(', ')', '[', ']', '{', '}']

def is_valid_operator(ch):
    return ch in ['+', '-', '*', '/', '>', '<', '=']

def is_valid_identifier(string):
    if string[0].isdigit() or is_valid_delimiter(string[0]):
        return False
    return True

def is_valid_keyword(string):
    keywords = ["if", "else", "while", "do", "break", "continue", "int", "double", "float", 
                "return", "char", "case", "sizeof", "long", "short", "typedef", "switch", 
                "unsigned", "void", "static", "struct", "goto"]
    return string in keywords

def is_valid_integer(string):
    if len(string) == 0:
        return False
    return string.isdigit()

def is_real_number(string):
    try:
        float(string)
        return '.' in string
    except ValueError:
        return False

def sub_string(string, left, right):
    return string[left:right+1]

# Function to detect tokens and count them
def detect_tokens(string):
    global keyword_count, identifier_count, operator_count, integer_count, invalid_identifier_count

    left = 0
    right = 0
    length = len(string)

    while right <= length and left <= right:
        if not is_valid_delimiter(string[right:right+1]):
            right += 1

        if is_valid_delimiter(string[right:right+1]) and left == right:
            if is_valid_operator(string[right]):
                print(f"Valid operator : '{string[right]}'")
                operator_count += 1
            right += 1
            left = right
        elif (is_valid_delimiter(string[right:right+1]) and left != right) or (right == length and left != right):
            sub_str = sub_string(string, left, right - 1)

            if is_valid_keyword(sub_str):
                print(f"Valid keyword : '{sub_str}'")
                keyword_count += 1
            elif is_valid_integer(sub_str):
                print(f"Valid Integer : '{sub_str}'")
                integer_count += 1
            elif is_valid_identifier(sub_str) and not is_valid_delimiter(string[right-1]):
                print(f"Valid Identifier : '{sub_str}'")
                identifier_count += 1
            else:
                print(f"Invalid Identifier : '{sub_str}'")
                invalid_identifier_count += 1

            left = right

# Main program
if __name__ == "__main__":
    print("Enter your code (press Enter on an empty line to finish):")

    # Initialize an empty string to collect multiple lines
    multiline_input = ""
    while True:
        # Take input line by line
        line = input()
        if line == "":
            break
        multiline_input += line + " "

    print(f"\nThe Program is : '{multiline_input.strip()}'")
    print("All Tokens are :\n")

    # Detect tokens in the multi-line input
    detect_tokens(multiline_input)

    # Print summary of token counts
    print("\nSummary:")
    print(f"Keywords: {keyword_count}")
    print(f"Identifiers: {identifier_count}")
    print(f"Operators: {operator_count}")
    print(f"Integers: {integer_count}")
    print(f"Invalid Identifiers: {invalid_identifier_count}")
