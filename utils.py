from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
class aes():

    def encrypt( plaintext: str, key: str) -> str:
        key_bytes = key.encode('UTF-8')
        cipher = AES.new(key_bytes, AES.MODE_ECB)
        plaintext_bytes = plaintext.encode('UTF-8')
        plaintext_bytes_padded = pad(plaintext_bytes, AES.block_size, 'pkcs7')
        ciphertext_bytes = cipher.encrypt(plaintext_bytes_padded)
        ciphertext_base64_bytes = base64.b64encode(ciphertext_bytes)
        ciphertext = ciphertext_base64_bytes.decode('UTF-8')
        return ciphertext


    def decrypt( ciphertext: str, key: str) -> str:
        key_bytes = key.encode('UTF-8')
        decrypter = AES.new(key_bytes, AES.MODE_ECB)
        ciphertext_base64_bytes = ciphertext.encode('UTF-8')
        ciphertext_bytes = base64.b64decode(ciphertext_base64_bytes)
        plaintext_bytes_padded = decrypter.decrypt(ciphertext_bytes)
        plaintext_bytes = unpad(plaintext_bytes_padded, AES.block_size, 'pkcs7')
        plaintext = plaintext_bytes.decode('UTF-8')
        return plaintext