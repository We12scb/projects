from flask import Flask, render_template, request

app = Flask(__name__)

# -----------------------------
# Custom Alphabet Configuration
# -----------------------------
# English + Numbers + Common Arabic Characters + Symbols
ENGLISH = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
ARABIC = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي" + "آأإةؤئ" # Basic Arabic set
SYMBOLS = " !?.,;:-_()[]{}"
ALPHABET = ENGLISH + NUMBERS + ARABIC + SYMBOLS

def get_shifted_char(char, shift, alphabet=ALPHABET):
    if char in alphabet:
        idx = alphabet.index(char)
        return alphabet[(idx + shift) % len(alphabet)]
    return char

# -----------------------------
# Caesar Cipher
# -----------------------------
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        result += get_shifted_char(char, shift)
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def caesar_break(text):
    results = []
    # Try a reasonable subset of shifts if alphabet is huge, but here we try all
    # Limiting to first 100 shifts to avoid UI clutter if alphabet grows too large
    limit = min(len(ALPHABET), 100) 
    for shift in range(1, limit):
        decrypted = caesar_decrypt(text, shift)
        results.append(f"Shift {shift}: {decrypted}")
    return results

# -----------------------------
# Vigenere Cipher
# -----------------------------
def vigenere_encrypt(text, key):
    result = ""
    key_indices = [ALPHABET.index(k) for k in key if k in ALPHABET]
    if not key_indices:
        return text # Return original if key has no valid chars
        
    key_len = len(key_indices)
    key_idx = 0
    
    for char in text:
        if char in ALPHABET:
            shift = key_indices[key_idx % key_len]
            result += get_shifted_char(char, shift)
            key_idx += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key_indices = [ALPHABET.index(k) for k in key if k in ALPHABET]
    if not key_indices:
        return text
        
    key_len = len(key_indices)
    key_idx = 0
    
    for char in text:
        if char in ALPHABET:
            shift = key_indices[key_idx % key_len]
            result += get_shifted_char(char, -shift)
            key_idx += 1
        else:
            result += char
    return result

# -----------------------------
# Rail Fence Cipher
# -----------------------------
def rail_fence_encrypt(text, rails):
    if rails < 2: return text
    rail = [''] * rails
    direction_down = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)

def rail_fence_decrypt(cipher, rails):
    if rails < 2: return cipher
    # Use None as placeholder instead of '\n' to avoid conflict with actual newlines
    rail = [[None for _ in range(len(cipher))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if direction_down else -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        # Check against None placeholder
        if rail[row][col] is not None:
            result.append(rail[row][col])
            col += 1
        row += 1 if direction_down else -1

    return ''.join(result)

def rail_fence_break(text):
    results = []
    # Try rails 2 to 10
    for rails in range(2, 11):
        decrypted = rail_fence_decrypt(text, rails)
        results.append(f"Rails {rails}: {decrypted}")
    return results

# -----------------------------
# Flask Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    is_list = False
    
    if request.method == "POST":
        algo = request.form["algorithm"]
        mode = request.form["mode"]
        text = request.form["text"]
        key = request.form.get("key", "")

        try:
            if mode == "break":
                is_list = True
                if algo == "caesar":
                    result = caesar_break(text)
                elif algo == "rail":
                    result = rail_fence_break(text)
                elif algo == "vigenere":
                    result = ["Break functionality not supported for Vigenère without dictionary attack."]
            
            else: # Encrypt or Decrypt
                if algo == "caesar":
                    shift = int(key)
                    result = caesar_encrypt(text, shift) if mode == "encrypt" else caesar_decrypt(text, shift)

                elif algo == "vigenere":
                    result = vigenere_encrypt(text, key) if mode == "encrypt" else vigenere_decrypt(text, key)

                elif algo == "rail":
                    rails = int(key)
                    result = rail_fence_encrypt(text, rails) if mode == "encrypt" else rail_fence_decrypt(text, rails)
        except Exception as e:
            result = f"⚠ Error: {e}"
            is_list = False

    return render_template("index.html", result=result, is_list=is_list)

if __name__ == "__main__":
    app.run(debug=True)