#-*- coding: utf-8 -*-

from p import Problem

class p59(Problem):

    """

        Each character on a computer is assigned a unique code and 
        the preferred standard is ASCII (American Standard Code for 
        Information Interchange). For example, uppercase A = 65,
         asterisk (*) = 42, and lowercase k = 107.
       
        A modern encryption method is to take a text file, convert 
        the bytes to ASCII, then XOR each byte with a given value, 
        taken from a secret key.The advantage with the XOR function 
        is that using the same encryption key on the cipher text, 
        restores the plain text; for example, 65 XOR 42 = 107, 
        then 107 XOR 42 = 65.
       
        For unbreakable encryption, the key is the same length as 
        the plain text message, and the key is made up of random 
        bytes. The user would keep the encrypted message and the 
        encryption key in different locations,and without both 
        "halves", it is impossible to decrypt the message.
       
        Unfortunately, this method is impractical for most users, 
        so the modified method is to use a password as a key. 
        If the password is shorter than the message, which is likely, 
        the key is repeated cyclically throughout the message. 
        The balance for this method is using a sufficiently long 
        password key for security, but short enough to be memorable.
        Your task has been made easy, as the encryption key consists 
        of three lower case characters. 
        
        Using cipher.txt (right click and 'Save Link/Target As...'), 
        a file containing the encrypted ASCII codes, and the knowledge 
        that the plain text must contain common English words, decrypt 
        the message and find the sum of the ASCII values in the original 
        text.

    """

    def cipher_parse(self, file_name):
        output = ""
        with open(file_name, 'r') as f:
            content = f.readline()
            for c in content.split(','):
                output += chr(int(c)) 
        return output

    def decipher(self, cipher, key):
        l = len(key)
        tmp_output = list(cipher)
        output=""
        for i in xrange(len(output)):
            tmp_output[i]=chr(ord(output[i])^ord(key[i%l]))
        for c in tmp_output:
            output+=c
        return output

    def occur(self, text, dico):
        count = 0
        for i in xrange(len(dico)):
            index = 0
            while(text.find(dico[i], index)>=0):
                index = text.find(dico[i], index) +1
                count +=1
        return count

    def solve(self):
        cipher = self.cipher_parse("src/p59_cipher.txt")
        dico = ["the", "that", "this", "are", "is", "were", "was", "has", "have", "had", "out", "in", "off"]
        plaintext = ""
        potential_plaintext = ""
        occur = 0
        tmp_occur = 0
        key_result = ""
        for c1 in xrange(128):
            for c2 in xrange(128):
                for c3 in xrange(128):
                    key = str(c1)+str(c2)+str(c3)
                    potential_plaintext = self.decipher(cipher, key)
                    occur = self.occur(potential_plaintext, dico)
                    if tmp_occur < occur:
                        plaintext = potential_plaintext
                        key_result = key
        with open('src/p59_plaintext.txt', 'w') as f:
            f.write(plaintext)
        return key
