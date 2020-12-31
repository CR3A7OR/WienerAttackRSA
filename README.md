# WienerAttackRSA

A Python script for the Wiener attack on RSA public-key encryption scheme.
Which is a type of cryptographic attack against RSA. The attack uses the continued fraction method to expose the private key d when d is small and e is large.

# Installation
You can install the requirments.txt file with:
> pip3 install -r requirements.txt

# Features
The script can take raw inputs of n, e, c with: 
> python3 wienerAttack.py


The script can take an encrypted file and then a public key, such as:
> python3 wienerAttack.py flag.enc pubkey.pem

```diff
- DISCLAIMER: EDUCATIONAL PURPOSES ONLY. NO RESPONSIBILITY IS HELD OR ACCEPTED FOR MISUSE
```
