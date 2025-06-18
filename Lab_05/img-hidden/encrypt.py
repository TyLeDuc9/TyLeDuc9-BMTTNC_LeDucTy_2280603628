import sys
from PIL import Image

def encode_image(image_path, message):
    """
    Encodes a secret message into an image using the Least Significant Bit (LSB) method.

    Args:
        image_path (str): The path to the input image file.
        message (str): The message to be hidden in the image.
    """
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return

    # Ensure the image is in RGB mode for consistent channel access
    # Convert if it's RGBA or grayscale
    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    
    # Convert the message into a binary string
    # Each character is converted to its 8-bit binary representation
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Add a unique delimiter to mark the end of the message
    # This is crucial for the decoding process to know when to stop reading
    binary_message += '1111111111111110' # Đánh dấu kết thúc thông điệp (End of message marker)

    data_index = 0 # Keeps track of the current bit from binary_message to embed

    # Iterate through each pixel of the image
    for row in range(height):
        for col in range(width):
            # Convert pixel tuple to a list to make it mutable
            pixel = list(img.getpixel((col, row)))

            # Iterate through each color channel (R, G, B)
            for color_channel in range(3): # 0 for Red, 1 for Green, 2 for Blue
                if data_index < len(binary_message):
                    # Get the current channel's value (e.g., 255 for Red)
                    # Convert it to an 8-bit binary string (e.g., '11111111')
                    # Take all bits except the last one (LSB)
                    # Append the current bit from the binary_message
                    # Convert the new binary string back to an integer
                    pixel[color_channel] = int(
                        format(pixel[color_channel], '08b')[:-1] + binary_message[data_index],
                        2
                    )
                    data_index += 1
                else:
                    # If all message bits are embedded, no need to modify further channels
                    # This 'else' block ensures that if the message fits perfectly
                    # within the channels of a pixel, it doesn't break prematurely,
                    # but rather handles the remaining channels for that pixel.
                    pass # Or you could break this inner loop if you want to optimize slightly

            # Update the pixel in the image with the modified channel values
            # Convert the pixel list back to a tuple before putting it
            img.putpixel((col, row), tuple(pixel))

            # If all message bits have been embedded, break out of the loops
            if data_index >= len(binary_message):
                break # Breaks out of the inner (col) loop
        
        # If all message bits have been embedded, break out of the outer (row) loop as well
        if data_index >= len(binary_message):
            break

    # Define the path for the output encoded image
    encoded_image_path = 'encoded_image.png'
    
    # Save the modified image
    try:
        img.save(encoded_image_path)
        print("Steganography complete. Encoded image saved as", encoded_image_path)
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    """
    Main function to handle command-line arguments and initiate the encoding process.
    Expected usage: python your_script_name.py <image_path> <message>
    """
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    
    # Call the encode_image function with the provided arguments
    encode_image(image_path, message)

if __name__ == "__main__":
    main()