def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    
    Parameters:
        text (str): The input text to be encrypted or decrypted
        shift (int): The number of positions to shift each character
        mode (str): 'encrypt' or 'decrypt' to specify the operation
    
    Returns:
        str: The transformed text
    """
    result = ""
    
    # Determine the direction of the shift based on mode
    if mode == 'decrypt':
        shift = -shift
    
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around if necessary
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += shifted
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around if necessary
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += shifted
        else:
            # If it's not a letter, leave it unchanged
            result += char
    
    return result

def main():
    print("Caesar Cipher Program")
    print("---------------------")
    
    while True:
        # Get user input for mode selection
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? (or 'q' to quit): ").lower()
        
        if mode == 'q':
            print("Goodbye!")
            break
        elif mode not in ['e', 'd']:
            print("Invalid option. Please enter 'e', 'd', or 'q'.")
            continue
        
        # Get the message from the user
        message = input("Enter your message: ")
        
        # Get the shift value from the user
        while True:
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Shift must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Determine the full mode name for display
        full_mode = 'encrypt' if mode == 'e' else 'decrypt'
        
        # Perform the encryption/decryption
        transformed_text = caesar_cipher(message, shift, full_mode)
        
        # Display the results
        print(f"\nOriginal text: {message}")
        print(f"Mode: {full_mode}")
        print(f"Shift value: {shift}")
        print(f"Transformed text: {transformed_text}\n")

if __name__ == "__main__":
    main()