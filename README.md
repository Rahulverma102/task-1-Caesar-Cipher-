TASK-1 BY PRODIGY INFOTECH 

"Caesar-Cipher"  
This tool is used to encrypt and decrypt text in alphabet order 
Explanation of this tool 
Explanation of the Program



1. The caesar_cipher Function
This is the core function that performs the encryption or decryption.

Parameters:

text: The input string to be transformed

shift: The number of positions to shift each letter

mode: Either 'encrypt' or 'decrypt' to specify the operation

How it works:

If the mode is 'decrypt', it inverts the shift value (decryption is just encryption with a negative shift)

For each character in the input text:

If it's an uppercase letter (A-Z):

Convert to its ASCII value with ord(char)

Subtract ASCII value of 'A' to get a 0-based position (A=0, B=1, etc.)

Apply the shift and use modulo 26 to wrap around if needed

Convert back to a character with chr()

If it's a lowercase letter (a-z), same process but using 'a' as the base

Non-alphabetic characters are left unchanged

2. The main Function
This handles user interaction and program flow.

User Input:

First asks whether to encrypt, decrypt, or quit

Then gets the message to transform

Finally gets the shift value (validated to be between 1-25)

Processing:

Calls caesar_cipher with the appropriate parameters

Displays the original and transformed text

3. How the Caesar Cipher Works
The Caesar Cipher is one of the simplest encryption techniques:

Each letter in the plaintext is shifted a fixed number of positions down or up the alphabet

For example, with a shift of 3:

A → D

B → E

...

X → A (wraps around)

Y → B

Z → C

4. Key Points in the Implementation
Case Sensitivity: The program preserves case by handling uppercase and lowercase separately

Non-alphabetic Characters: These are left unchanged (spaces, numbers, punctuation)

Modulo Operation: The % 26 ensures the shift wraps around the alphabet correctly

Shift Validation: The shift must be between 1-25 (shifting by 0 or 26 would do nothing)

Example Usage
Encryption:

Message: "Hello World"

Shift: 3

Result: "Khoor Zruog"

Decryption:

Message: "Khoor Zruog"

Shift: 3

Result: "Hello World"
