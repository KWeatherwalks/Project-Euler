"""<p>Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code 
    for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.</p>

<p>A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
 taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
  restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.</p>

<p>For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of 
    random bytes. The user would keep the encrypted message and the encryption key in different locations, and 
    without both "halves", it is impossible to decrypt the message.</p>

<p>Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.</p>

<p>Your task has been made easy, as the encryption key consists of three lower case characters. 
Using <a href="project/resources/p059_cipher.txt">p059_cipher.txt</a> (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.</p>
"""

from itertools import permutations
from string import ascii_lowercase

# ASCII value of lowercase alphabet range from 97 to 122

# -----------------------------------------------------------------
## Method
##### Find the 3 most frequently used characters
##### These are likely to be either spaces or e,t,a,i,n,o,s,...

##### c: ciphertext character
##### m: message character
##### p: password character
##### c ^ p must be between 97 and 122 inclusive

#####  Calculate each of the top 3
#####  Find characters that result in spaces when xored
#####  Test each of the 6 permutations
#####  Use password that results in readable text

# -----------------------------------------------------------------
with open("data/p059_cipher.txt", "r") as file:
    data = [int(c) for c in file.readline().split(",")]

ciphertext = [chr(n) for n in data]

# frequency_counter = dict()
# for n in data:
#     if n in frequency_counter.keys():
#         frequency_counter[n] += 1
#     else:
#         frequency_counter[n] = 1

# top_freqs = sorted(frequency_counter.items(), key=lambda x: x[1], reverse=True)[:3]
# print(top_freqs)
# for f in top_freqs:
#     for c in ascii_lowercase:
#         print(c, chr(ord(c) ^ f[0])) # find one(s) that results in a common english character


for password in permutations("pex"):

    pass_dict = {i: password[i] for i in range(3)}
    message = [chr(n ^ ord(pass_dict[i % 3])) for i, n in enumerate(data)]
    print(password, "".join(message), end="\n" + "-" * 40 + "\n")


## Password is "exp"
# Calculate sum of ascii characters
print(sum([n ^ ord({0: "e", 1: "x", 2: "p"}[i % 3]) for i, n in enumerate(data)]))
