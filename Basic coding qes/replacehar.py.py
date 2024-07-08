my_string=input('Enter your string:')
new_char=input('Enter your charcter:')
vowels=('a,e,i,o,u,A,E,I,O,U')
new_string=''
for i in my_string:
    if i in vowels:
       new_string +=new_char
    else:
        new_string +=i
print(new_string)
