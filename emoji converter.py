message=input('Enter message:')
words=message.split(' ')
emojis={
    ':)':'😊',
    '<3':'❤',
    ':(':'😔'
}
output=''
for i in words:
    output+=emojis.get(i,i)
print(output)


