import re


def lexical_analyzer(source_code):
    # Define the regular expressions for each token type
    token_specification = [
        ('KEYWORD', r'\b(int|if|else|while|return)\b'),  # Keywords
        ('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9]*'),  # Identifiers
        ('NUMBER', r'\b[0-9]+\b'),  # Integer numbers
        ('OPERATOR', r'[+\-*/=><]'),  # Arithmetic and relational operators
        ('DELIMITER', r'[;{}( )]'),  # Delimiters and brackets
        ('WHITESPACE', r'[ \t\n\r]+'),  # Spaces, tabs, newlines
        ('UNKNOWN', r'.'),  # Catch-all for lexical errors
    ]
    
    # Combine all patterns into one large regex
    # The (?P<NAME>pattern) syntax creates named capture groups
    combined_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    
    print(f"{'TOKEN TYPE':<15} | {'LEXEME'}")
    print("-" * 35)
    
    # Scan the source code
    for match in re.finditer(combined_regex, source_code):
        token_type = match.lastgroup
        lexeme = match.group(token_type)
        
        # Skip whitespaces as they are not valid tokens for the parser
        if token_type == 'WHITESPACE':
            continue
        elif token_type == 'UNKNOWN':
            print(f"{'LEXICAL ERROR':<15} | {lexeme}")
        else:
            print(f"{token_type:<15} | {lexeme}")


# Test the Analyzer
if __name__ == "__main__":
    cpp_code = """
    int total = sum + 25;
    if (total > 50) {
        total = total - 10;
    }
    """
    
    print("Analyzing Source Code:\n", cpp_code)
    lexical_analyzer(cpp_code)