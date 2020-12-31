#PACKAGES NEEDED TO RUN CODE
################################
#pip3 install pycryptodome
#python3 -m pip install owiener
#################################
from Crypto.PublicKey import RSA
import owiener
import sys
try:
	encryptedFile = sys.argv[1]
	pubFile = sys.argv[2]
	type = "file"
except NameError:
	print("Please Enter the encrypted file and the public key directories in that order")
	exit()
except:
    while True:
        try:
            print("Input n")
            n = int(input())
            print("Input e:")
            e = int(input())
            print("Input c:")
            c = int(input())
            type = "text"
        except ValueError:
            print("Please Input an Integer")
            continue
        else:
            break

#GET EXPONENT AND MODULUS
if type == "file":
    pubkey = RSA.importKey(open(pubFile).read())
    e = pubkey.e
    n = pubkey.n
print("Exponent = ", e, "\n")
print("Modulus = ", n, "\n")

#GET DECRYPTION EXPONENT
d = owiener.attack(e, n)

if d is None:
    print("Failed")
    exit()
else:
    print("DECRYPTION EXPONENT = {}".format(d), "\n")

#CONVERT FLAG TO INT
if type == "file":
    with open(encryptedFile, "rb") as file:
        bytes = file.read()
        c = int.from_bytes(bytes, "big")
print("INT VALUE = ", c, "\n")

#NOW DO (c^d) MOD N
# (c ^ d) % n
value = pow(c, d, n) 
print ("UNENCRYPTED AS INT = ", value, "\n") 


flag = value.to_bytes(1024,byteorder="big")
print(flag)


