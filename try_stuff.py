#a = [0,1,2,3,4,5,6,7,8,9,10]
#print(a)

#for i in range(10):
#    print(i)

#b = a[:5:-3]
#print(b)

word = 'Hello.txt'
print(word[1:])
print(word[:3])
print(word[3:])
print(word[:-5])
print(word[-4:])

print('Value of the __name__ : ', __name__)  

def print_number(number):
    emoji_number = ''  # 0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣
    emoji_src = '0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣'
    for n in number:
        emoji_number += emoji_src[int(n)]
        # match n:
        #    case '0':
        #        emoji_number += '0️⃣'
        #    case '1':
        #        emoji_number += '1️⃣'
        #    case '2':
        #        emoji_number += '2️⃣'
        #    case '3':
        #        emoji_number += '3️⃣'
        #    case '4':
        #        emoji_number += '4️⃣'
        #    case '5':
        #        emoji_number += '5️⃣'
        #    case '6':
        #        emoji_number += '6️⃣'
        #    case '7':
        #        emoji_number += '7️⃣'
        #    case '8':
        #        emoji_number += '8️⃣'
        #    case '9':
        #        emoji_number += '9️⃣'
        #    case _:
        #        raise
    return emoji_number
