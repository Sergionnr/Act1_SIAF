from cryptography.fernet import Fernet

def decrypt_message(token, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(token)
    return decrypted_message.decode()

# Example usage
token = b'gAAAAABluwmvSSEwdXCwthKvxx6_fVFg40AjzEenPD7v1Sl6_A2yZIfsY1ygLJryFh2oq-Ga9xkFWlZcgAySMvweUbKjNrY-zw=='
key = b'ZtXs_q3FZeUzaew4OSRrMhAoOYZcrEjU3FsV2qHn4ro='
decrypted_message = decrypt_message(token, key)
print(decrypted_message)
