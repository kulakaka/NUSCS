word_dic={
   "A":'00',
   "B":'01',
    'C':'02',
    'D':'03',
    'E':'04',
    'F':'05',
    'G':'06',
    'H':'07',
    'I':'08',
    'J':'09',
    'K':'10',
    'L':'11',
    'M':'12',
    'N':'13',
    'O':'14',
    'P':'15',
    'Q':'16',
    'R':'17',
    'S':'18',
    'T':'19',
    'U':'20',
    'V':'21',
    'W':'22',
    'X':'23',
    'Y':'24',
    'Z':'25',
    ' ':'99'
}
n_word_dic={
   "A":00,
   "B":1,
    'C':2,
    'D':3,
    'E':4,
    'F':5,
    'G':6,
    'H':7,
    'I':8,
    'J':9,
    'K':0,
    'L':11,
    'M':12,
    'N':13,
    'O':14,
    'P':15,
    'Q':16,
    'R':17,
    'S':18,
    'T':19,
    'U':20,
    'V':21,
    'W':22,
    'X':23,
    'Y':24,
    'Z':25,
    ' ':99
}


def encode_I(word):
    # alp= "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    # lialp =[]
    wordli = []
    nm = ''
    # for i in alp:
    #     lialp.append(i)
    for x in word:
        wordli.append(x)
    for i in wordli:
        nm += word_dic.get(i)
    return nm
# print(encode_I('I MISS YOU'))


def encoding_R(word):
    if not word:
        return ''
    else:
        n = word_dic.get(word[0])
        return n+encoding_R(word[len(word)-(len(word)-1):])

alp= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nm = ['00','01','02','03','04','05','06','07','08','09','10','11',
      '12','13','14','15','16','17','18','19','20','21','22','23',
      '24','25']


                

def decode(msg, offset):
    decoded_msg = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in msg:
        if char.isdigit():
            num = int(char)
            if num == 9:  # '9' represents a space
                decoded_char = ' '
            else:
                decoded_char = alphabet[(num - offset) % 26]
        else:
            decoded_char = char
        
        decoded_msg += decoded_char

    return decoded_msg



print(decode('1213992305161603', 5))