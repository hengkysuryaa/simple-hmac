from typing import List
from sha3 import keccak
import json

def add_metadata(filepath, metadata):
    with open(filepath, 'a+b') as f:
        f.write(json.dumps(metadata).encode('utf-8'))

def load_file(filepath: str):
    # return list of bytes
    file_byte = []
    with open(filepath, "rb") as f:
        file_byte += f.read()
    return file_byte


def write_file(filepath: str, content: List[int]):
    with open(filepath, "wb") as f:
        f.write(content)

def embedMAC(filepath: str):
    file_byte = load_file(filepath)
    # TODO: Get key
    key = 123456789
    # Combine key + file byte
    key_bytes = key.to_bytes(len(str(key))//2, 'big')
    combined = list(key_bytes) + file_byte
    # Hitung SHA3
    mac = keccak(bytes(combined)).hex()
    print("kode MAC:", mac)
    # masukkan idx peletakan dan MAC ke file byte
    add_metadata(filepath, {'MAC':mac, 'Idx':len(file_byte)})

embedMAC("Tugas-Makalah-(2021) - Copy.pdf")