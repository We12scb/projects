# ProCipher - Advanced Encryption Tool 🔐

ProCipher is a modern, secure, and user-friendly web application for encryption and decryption. It supports multiple algorithms and features a premium "Soft Dark" UI designed for comfort and aesthetics.

## 🌟 Features

-   **Multiple Algorithms**:
    -   **Caesar Cipher**: Classic shift cipher.
    -   **Vigenère Cipher**: Polyalphabetic substitution.
    -   **Rail Fence Cipher**: Transposition cipher.
-   **Advanced Character Support**:
    -   Supports **English (A-Z)**, **Numbers (0-9)**, and **Arabic Characters**.
    -   Custom alphabet handling ensures robust encryption for mixed inputs.
-   **"Break" Mode (Brute Force)**:
    -   Automatically attempts to crack **Caesar** and **Rail Fence** ciphers without a key.
    -   Displays all possible variations for easy recovery of messages.
-   **Modern UI**:
    -   **Soft Dark Theme**: Easy on the eyes, perfect for long usage.
    -   **Responsive Design**: Works beautifully on all devices.
    -   **One-Click Copy**: Easily copy results to clipboard.

## 🚀 How to Run

0.create folder
. cipher_webapp/

│
├── app.py

├── static/

│   └── style.css

└── templates/

    └── index.html
    

1.  **Prerequisites**:
    -   Python 3.x
    -   Flask (`pip install flask`)

2.  **Installation**:
    ```bash
    # Clone or download the repository
    cd cipher_webapp
    
    # Install dependencies
    pip install flask
    ```

3.  **Start the Server**:
    ```bash
    python app.py
    ```

4.  **Access the App**:
    -   Open your browser and go to: `http://127.0.0.1:5000`


## 🛠️ Usage

1.  Select an **Algorithm** (Caesar, Vigenère, or Rail Fence).
2.  Choose a **Mode**:
    -   **Encrypt**: Turn plain text into cipher text.
    -   **Decrypt**: Turn cipher text back to plain text.
    -   **Break**: Attempt to crack the code without a key (Caesar/Rail Fence only).
3.  Enter your **Text**.
4.  Enter a **Key** (if encrypting/decrypting).
5.  Click **Process Request**.

## 📝 License

This project is open-source and available for educational purposes.
