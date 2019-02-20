
import rsa

m = '86584afb2a8d053ff3bbe054c628521334b40a1e9f0a33308fc95fe8eea227d822a5ea45cfad9bd1c5f89fdb46c5180bfc20f44202fa2d474260e6bca9ffa2d221365f142cd7a022fa8aead20a33f3991447fb085d84b144154f3f728a69166320b3c23745ac464b081add448753f0c8a8c0afe0ef9fbcb7a10710339421c0d7'
e = '10001'

message = '12345678'

dist = '5d6f2b45d89f530e6270c77a2823dbb00bd588a76a9ea872ec8251a4ac32be28102365e9fdde9c1f23f2065ce3baf8bb2a3f84d9a78567752bada6a8e34f0c88d469f2b17f21af50112afd8933d86246bc3a3d8e8e9c441047254999e81c6e1dd9140384e24002a68057328c9123dafe49d74e05afdadba92c4e960883ca777f'


class Encrypt(object):
    def __init__(self,e,m):
        self.e = e
        self.m = m

    def encrypt(self,message):
        mm = int(self.m, 16)
        ee = int(self.e, 16)
        rsa_pubkey = rsa.PublicKey(mm, ee)
        crypto = self._encrypt(message.encode(), rsa_pubkey)
        return crypto.hex()

    def _pad_for_encryption(self, message, target_length):
        message = message[::-1]
        max_msglength = target_length - 11
        msglength = len(message)

        padding = b''
        padding_length = target_length - msglength - 3

        for i in range(padding_length):
            padding += b'\x00'

        return b''.join([b'\x00\x00',padding,b'\x00',message])

    def _encrypt(self, message, pub_key):
        keylength = rsa.common.byte_size(pub_key.n)
        padded = self._pad_for_encryption(message, keylength)

        payload = rsa.transform.bytes2int(padded)
        encrypted = rsa.core.encrypt_int(payload, pub_key.e, pub_key.n)
        block = rsa.transform.int2bytes(encrypted, keylength)

        return block

en = Encrypt(e,m)
print(en.encrypt(message))



