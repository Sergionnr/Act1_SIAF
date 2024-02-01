from cryptography.fernet import Fernet

clave = Fernet.generate_key()
print("clave: ", clave)
print()

f = Fernet(clave)
print("El Fernet: ", f)
print()

token = f.encrypt(b"Hola es mi mensaje secreto")

print("token: ", token)
print()

mensaje = f.decrypt(token)

print(mensaje)