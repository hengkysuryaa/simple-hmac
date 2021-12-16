from typing import List
from sha3 import keccak
import json
from db_conn import create_connection
import sys

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
    try:
        file_byte = load_file(filepath)
        # Get key
        conn = create_connection(r"transaksi.db")
        cur = conn.cursor()
        cur.execute("SELECT private_key FROM transaksi WHERE username=? AND invoice_code=?", (str(sys.argv[1]), str(sys.argv[2]),))
        rows = cur.fetchone()
        key = rows[0]

        # Combine key + file byte
        key_bytes = key.to_bytes(len(str(key))//2, 'big')
        combined = list(key_bytes) + file_byte

        # Hitung SHA3
        mac = keccak(bytes(combined)).hex()
        print("kode MAC:", mac)

        # masukkan idx peletakan dan MAC ke file byte
        add_metadata(filepath, {'MAC':mac, 'Idx':len(file_byte)})
    except:
        print("Input pada terminal tidak valid!")

if __name__ == '__main__':
    embedMAC(str(sys.argv[3]))