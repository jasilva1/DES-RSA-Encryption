
import random
import math

#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a,b):
    if b == 0:
        return (1, 0, a)
    x1, y1, gcd = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a//b) * y1
    return x, y, gcd


#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################
    d, y, gcd = extended_euclid(e,z)
    while (d <0):
        d = d + z
    return d


def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################

    repeat = 0
    n= p*q
    z = (p-1)*(q-1)
    while repeat==0:
        e=input("input value for e that is coprime with "+str(z)+ " and less than "+str(n)+ " : ")
        e=int(e)
        if e>=n:
            repeat=0
        elif gcd(e,z)!=1:
            repeat=0
        else:
            repeat=1
    d = get_d(e,z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    
    e=pk[0]
    n=pk[1]
    plaintext = ord(plaintext)
    cipher = pow(plaintext,e,n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    d=pk[0]
    n=pk[1]
    plain = chr(pow(ciphertext, d, n))
    return ''.join(plain)

