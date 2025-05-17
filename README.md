
# 🔐 Password Manager CLI

A simple Command Line Interface (CLI) based Password Manager built with Python. This app securely stores, retrieves, and deletes your passwords using encryption with the `cryptography` library.

---

## 🚀 Features

- 🔑 Store passwords securely using symmetric encryption (`Fernet`)
- 🕵️ Retrieve stored passwords by website name
- 🗑️ Delete saved passwords
- 🔐 Password-protected access to the app
- 💾 Encrypted password storage in a local `db.txt` file
- 🧾 JSON-formatted, human-readable structure (after decryption)

---

## 📂 File Structure

- `main.py` - The main application logic
- `secret_test.key` - The key file used for encryption/decryption (auto-generated)
- `db.txt` - The encrypted storage file for all passwords

---

## 🔧 Requirements

- Python 3.6+
- `cryptography` library

Install dependencies:

```bash
pip install cryptography
```

---

## 🛠 How to Use

1. Clone the repository:

```bash
git clone https://github.com/yourusername/password-manager-cli.git
cd password-manager-cli
```

2. Make sure `secret_test.key` is present (or generate one using `Fernet.generate_key()`).

3. Run the script:

```bash
python main.py
```

4. Use the menu to:
   - Start storing new passwords
   - Retrieve previously saved passwords
   - Delete a saved password
   - Exit the app

---

## 🔐 Security Note

- This app uses symmetric encryption (Fernet), so the **`secret_test.key`** must be protected.
- The current access system is a hardcoded password (`1234`) — **update this before using in real environments.**

---

## 📌 TODOs & Improvements

- Add a GUI interface with Tkinter or PyQt
- Store the encryption key more securely
- Replace hardcoded access password with hashed login system
- Allow master password changes
- Backup/restore functionality

---

## 🧑‍💻 Author

Zayed0099  
GitHub: [github.com/zayed0099](https://github.com/zayed0099)

---

## 📄 License

This project is licensed under the MIT License.
