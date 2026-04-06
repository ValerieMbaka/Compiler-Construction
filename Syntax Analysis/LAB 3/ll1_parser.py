def ll1_parser(input_string):
    # Ensure the input string ends with the end-of-input marker '$'
    if not input_string.endswith('$'):
        input_string += '$'
    
    # Initialize the stack with '$' and the start symbol 'S'
    stack = ['$', 'S']
    i = 0  # Pointer for the input string
    
    # Print the table header
    print(f"\n{'Stack':<20}{'Input':<20}{'Action'}")
    print("-" * 60)
    
    # Parsing Loop
    while len(stack) > 0:
        top_symbol = stack.pop()
        current = input_string[i]
        
        # Formatting for the print output
        stack_str = "".join(stack + [top_symbol])
        input_str = input_string[i:]
        
        # If Top of Stack is a Terminal that matches the current input
        if top_symbol == current:
            if current == '$':
                print(f"{stack_str:<20}{input_str:<20}Accept")
                return
            print(f"{stack_str:<20}{input_str:<20}Match {current}")
            i += 1
        
        # Grammar Rules for S
        elif top_symbol == 'S':
            if current in ['a', 'b', '$']:
                print(f"{stack_str:<20}{input_str:<20}S -> AB")
                # Push in reverse order: B then A
                stack.extend(['B', 'A'])
            else:
                print(f"{stack_str:<20}{input_str:<20}Error")
                return
        
        # Grammar Rules for A
        elif top_symbol == 'A':
            if current == 'a':
                print(f"{stack_str:<20}{input_str:<20}A -> aA")
                stack.extend(['A', 'a'])
            elif current in ['b', '$']:
                print(f"{stack_str:<20}{input_str:<20}A -> \u03B5 (epsilon)")
            else:
                print(f"{stack_str:<20}{input_str:<20}Error")
                return
        
        # Grammar Rules for B
        elif top_symbol == 'B':
            if current == 'b':
                print(f"{stack_str:<20}{input_str:<20}B -> bB")
                stack.extend(['B', 'b'])
            elif current == '$':
                print(f"{stack_str:<20}{input_str:<20}B -> \u03B5 (epsilon)")
            else:
                print(f"{stack_str:<20}{input_str:<20}Error")
                return
        
        # Invalid Symbol
        else:
            print(f"{stack_str:<20}{input_str:<20}Error: Unrecognized symbol")
            return
    
    print("Reject")


if __name__ == "__main__":
    # Test strings
    test_strings = ["aaabbb", "abbb", "aaa", "bba"]
    
    for test in test_strings:
        print(f"\n\nTesting string: '{test}'")
        ll1_parser(test)