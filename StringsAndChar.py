# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#          continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
#     print('Access granted.')
    
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
    
import sys
while True:
 print('Type exit to exit.')
 response = input()
 if response == 'exit':
    sys.exit()
 print('You typed ' + response + '.')