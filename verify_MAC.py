import re
import json
from typing import List
from sha3 import keccak
from db_conn import create_connection
import sys

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
    try:
        # read metadata
        meta = read_metadata(filepath)
        mac = json.loads(meta).get("MAC")
        idx = json.loads(meta).get("Idx")
        print("metadata MAC:", mac)

        #read file
        file_byte = load_file(filepath)
        msg = file_byte[:idx]

        # Mengganti 1 elemen pada message
        #msg[100] = 65

        # Get key
        conn = create_connection(r"transaksi.db")
        cur = conn.cursor()
        cur.execute("SELECT private_key FROM transaksi WHERE username=? AND invoice_code=?", (str(sys.argv[1]), str(sys.argv[2]),))
        rows = cur.fetchone()
        key = rows[0]

        # Combine key + file byte
        key_bytes = key.to_bytes(len(str(key))//2, 'big')
        combined = list(key_bytes) + msg

        # Hitung SHA3
        calc_mac = keccak(bytes(combined)).hex()
        print("kalkulasi MAC:", calc_mac)

        if calc_mac == mac:
            print("Integritas terjaga!")
        else:
            print("Integritas tidak terjaga!")
    except:
        print("Input pada terminal tidak valid!")

if __name__ == '__main__':
    verifyMAC(str(sys.argv[3]))