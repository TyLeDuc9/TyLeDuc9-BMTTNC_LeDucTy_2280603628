import sys
from PIL import Image

def decode_image(encoded_image_path):
    try:
        img = Image.open(encoded_image_path)
    except FileNotFoundError:
        print(f"Error: Encoded image file not found at {encoded_image_path}")
        return ""

    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    
    message = ""
    binary_accumulator = ""
    
    DELIMITER = '1111111111111110' 
    DELIMITER_LEN = len(DELIMITER)

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for color_channel in range(3):
                binary_accumulator += format(pixel[color_channel], '08b')[-1]
                
                if len(binary_accumulator) >= DELIMITER_LEN:
                    if binary_accumulator[-DELIMITER_LEN:] == DELIMITER:
                        binary_message_without_delimiter = binary_accumulator[:-DELIMITER_LEN]
                        
                        for i in range(0, len(binary_message_without_delimiter), 8):
                            char_binary_chunk = binary_message_without_delimiter[i:i+8]
                            if len(char_binary_chunk) == 8:
                                try:
                                    char_int = int(char_binary_chunk, 2)
                                    char = chr(char_int)
                                    message += char
                                except ValueError:
                                    print(f"Warning: Could not convert binary chunk '{char_binary_chunk}' to character.")
                                    return message
                            else:
                                print("Warning: Incomplete character bits before delimiter.")
                                return message

                        return message

    print("Warning: Delimiter not found or message extends beyond image capacity.")
    
    final_message_if_no_delimiter = ""
    for i in range(0, len(binary_accumulator), 8):
        char_binary_chunk = binary_accumulator[i:i+8]
        if len(char_binary_chunk) == 8:
            try:
                char_int = int(char_binary_chunk, 2)
                final_message_if_no_delimiter += chr(char_int)
            except ValueError:
                break
        else:
            break

    return final_message_if_no_delimiter


def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    
    decoded_message = decode_image(encoded_image_path)
    
    if decoded_message is not None:
        print("Decoded message:", decoded_message)
    else:
        print("Failed to decode message.")

if __name__ == "__main__":
    main()