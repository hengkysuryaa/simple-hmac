import re
import json
from typing import List
from sha3 import keccak

def read_metadata(filepath):
    with open(filepath, 'rb') as f:
        data = str(f.read())
    meta = re.findall(r'xff.*({.*})\'\Z', data)[-1]
    return meta

def load_file(filepath: str):
    # return list of bytes
    file_byte = []
    with open(filepath, "rb") as f:
        file_byte += f.read()
    return file_byte

def verifyMAC(filepath):
    meta = read_metadata(filepath)
    mac = json.loads(meta).get("MAC")
    idx = json.loads(meta).get("Idx")
    print("metadata", mac, idx)

    #read file
    file_byte = load_file(filepath)
    msg = file_byte[:idx]

    # TODO: Get key
    key = 123456789
    # Combine key + file byte
    key_bytes = key.to_bytes(len(str(key))//2, 'big')
    combined = list(key_bytes) + msg
    # Hitung SHA3
    calc_mac = keccak(bytes(combined)).hex()
    print("kalkulasi MAC:", mac)
    if calc_mac == mac:
        print("Integritas terjaga!")

verifyMAC("Tugas-Makalah-(2021) - Copy.pdf")