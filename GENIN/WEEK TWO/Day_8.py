#Day_8
def greet():
   print("hello")
   print("how do you do?")
   print("is`nt the weather nice today?")
greet()

#function that allows for input

def greet_with_name(name):
   print(f"hello{name}")
   print(f"how do you do{name}?")

greet_with_name("Angela")

   #funtion with more than 1 input
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}?")

greet_with("jack Bauer", "nowhere")
greet_with("nowhere", "jack Baeur")
greet_with(location="london", name="Angela")

#paint calculation

import math
def paint_calc(height, width, cover):
   area=height*width
   num_of_cans=math.ceil(area/cover)
   print(f"you`ll need 5 cans of paint.")


test_h=int(input("height of wall: "))
test_w=int(input("width of wall: "))
coverage=5
paint_calc(height=test_h, width=test_w, cover=coverage)



#prime number checker
def prime_checker(number):
    is_prime=True
    for i in range(2, number-1):
        if number % i==0:
            is_prime==False
    if is_prime:
        print("it is a prime number.")





#Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o',
            'p','q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p','q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']
direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))
#create a funtion calle 'encrypt
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"the encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)
#create a funtion to 'decode'
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"he decoded text is {plain_text}")
if direction == "encoded":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
