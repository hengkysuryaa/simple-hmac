# simple-hmac

## Add MAC Code to a file
`python embed_MAC.py <username> <invoice_code> <input_doc_path>`

## Verify MAC Code from a file
`python verify_MAC.py <username> <invoice_code> <input_doc_path>`

## DB scheme
Table name: transaksi
- `id` - integer PRIMARY KEY
- `username` - text NOT NULL
- `invoice_code` - text NOT NULL
- `private_key` - integer NOT NULL
