import os
import hashlib

def find_duplicates(directory):
    hashes = {}
    duplicates = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
            if filehash in hashes:
                duplicates.append(filepath)
            else:
                hashes[filehash] = filepath
        elif os.path.isdir(filepath):
            duplicates += find_duplicates(filepath)
    return duplicates

duplicates = find_duplicates(r'C:\Users\Arthur\Desktop\1')  # chemin vers le dossier a rechercher
for duplicate in duplicates:
    os.remove(duplicate)
