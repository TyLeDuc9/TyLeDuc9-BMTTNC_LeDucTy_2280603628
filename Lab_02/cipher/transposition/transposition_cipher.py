class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        n_cols = key
        n_rows = len(text) // key
        if len(text) % key != 0:
            n_rows += 1

        n_shaded_boxes = (n_cols * n_rows) - len(text)
        plaintext = ['' for _ in range(n_rows)]

        col = 0
        row = 0

        for symbol in text:
            plaintext[row] += symbol
            row += 1
            if (row == n_rows) or (row == n_rows - 1 and col >= n_cols - n_shaded_boxes):
                row = 0
                col += 1

        return ''.join(plaintext)
