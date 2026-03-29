import re


def tokenize(code):
    # Define regular expressions for all valid tokens based on the BNF grammar
    token_specification = [
        ('COMMENT', r'/\*.*?\*/'),  # Multi-line comments /* ... */
        ('KEYWORD', r'\b(int|if|then|else|endif|while|do|enddo|print)\b'),
        ('RELOP', r'==|!=|<=|>=|<|>'),  # Relational operators
        ('OPERATOR', r'[+\-*/=\[\]\(\)]'),  # Arithmetic, assignment, and brackets
        ('PUNCT', r'[;,]'),  # Punctuation (comma, semicolon)
        ('ID', r'[a-zA-Z][a-zA-Z0-9]*'),  # Identifiers
        ('CONSTANT', r'\d+'),  # Integer constants
        ('WHITESPACE', r'[ \t\n\r]+'),  # Spaces, tabs, and newlines
        ('MISMATCH', r'.'),  # Any unrecognized character
    ]
    
    # Combine all patterns into a single regular expression
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    
    tokens = []
    
    # re.DOTALL flag allows the comment regex to match across multiple lines
    for match in re.finditer(tok_regex, code, re.DOTALL):
        kind = match.lastgroup
        value = match.group()
        
        # Ignore comments and whitespace
        if kind in ['COMMENT', 'WHITESPACE']:
            continue
        elif kind == 'MISMATCH':
            print(f"Lexical Error: Unrecognized character {value!r}")
        else:
            tokens.append((kind, value))
    
    return tokens


# Test Program
if __name__ == "__main__":
    # Sample code including an array declaration and a comment
    sample_program = """
    int x = 10, a[3];
    if (x < 20) then
        print(x);
    endif
    """
    
    print("Source Code:", sample_program)
    print("Tokens Generated:")
    
    # Run the lexical analyzer
    scanned_tokens = tokenize(sample_program)
    for token_type, token_value in scanned_tokens:
        print(f"{token_type}: {token_value}")