def encode_message(message, shift):
    encoded = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encoded += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encoded += char
    return encoded

def decode_message(encoded_message, shift):
    return encode_message(encoded_message, -shift)

def main():
    while True:
        print("-"*50)
        print("Secret Code Generator Menu:")
        print("-"*50)
        print("\t 1. Encode a message")
        print("\t 2. Decode a message")
        print("\t 3. Exit")
        print("-"*50)
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            message = input("Enter the message to encode: ")
            shift = int(input("Enter the shift number: "))
            print("Encoded message:", encode_message(message, shift))
        elif choice == '2':
            encoded_message = input("Enter the message to decode: ")
            shift = int(input("Enter the shift number: "))
            print("Decoded message:", decode_message(encoded_message, shift))
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
