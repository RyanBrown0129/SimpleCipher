cipher = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:',',27:'.',28:'-',29:'_'}
convert = {'A':0,'a':0,'B':1,'b':1,'C':2,'c':2,'D':3,'d':3,'E':4,'e':4,'F':5,'f':5,'G':6,'g':6,'H':7,'h':7,'I':8,'i':8,'J':9,'j':9,'K':10,'k':10,'L':11,'l':11,'M':12,'m':12,'N':13,'n':13,'O':14,'o':14,'P':15,'p':15,'Q':16,'q':16,'R':17,'r':17,'S':18,'s':18,'T':19,'t':19,'U':20,'u':20,'V':21,'v':21,'W':22,'w':22,'X':23,'x':23,'Y':24,'y':24,'Z':25,'z':25,',':26,'.':27,'-':28,'_':29}

key = input("Enter in the key: ")
#k = input("Enter in the k length: ")
k = len(key)
message = input("Now enter in your message: ")

codenum = ""

for i in range(0,len(message)):
  codenum = codenum + (cipher[((int(convert[message[i]]) + int(convert[key[i % len(key)]]))  % 30)])
  temp = ''
  for x in range(0,int(k)):
    if(x == i % int(k)):
      temp = temp + codenum[i]
    else:
      if(x < len(key)):
        temp = temp + key[x]
      else:
        temp = temp + "_"
        print("k is longer than the key, substituting _ for the missing character")
  key = temp
  #print(key) #for testing
print("the cipher text is:")
print(codenum)
input("press enter to quit")

#  ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-_
#                                
#A ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-_
#B BCDEFGHIJKLMNOPQRSTUVWXYZ,.-_A
#C CDEFGHIJKLMNOPQRSTUVWXYZ,.-_AB
#D DEFGHIJKLMNOPQRSTUVWXYZ,.-_ABC
#E EFGHIJKLMNOPQRSTUVWXYZ,.-_ABCD
#F FGHIJKLMNOPQRSTUVWXYZ,.-_ABCDE
#G GHIJKLMNOPQRSTUVWXYZ,.-_ABCDEf
#H HIJKLMNOPQRSTUVWXYZ,.-_ABCDEFG
#I IJKLMNOPQRSTUVWXYZ,.-_ABCDEFGH
#J JKLMNOPQRSTUVWXYZ,.-_ABCDEFGHI
#K KLMNOPQRSTUVWXYZ,.-_ABCDEFGHIJ
#L LMNOPQRSTUVWXYZ,.-_ABCDEFGHIJK
#M MNOPQRSTUVWXYZ,.-_ABCDEFGHIJKL
#N NOPQRSTUVWXYZ,.-_ABCDEFGHIJKLM
#O OPQRSTUVWXYZ,.-_ABCDEFGHIJKLMN
#P PQRSTUVWXYZ,.-_ABCDEFGHIJKLMNO
#Q QRSTUVWXYZ,.-_ABCDEFGHIJKLMNOP
#R RSTUVWXYZ,.-_ABCDEFGHIJKLMNOPQ
#S STUVWXYZ,.-_ABCDEFGHIJKLMNOPQR
#T TUVWXYZ,.-_ABCDEFGHIJKLMNOPQRS
#U UVWXYZ,.-_ABCDEFGHIJKLMNOPQRST
#V VWXYZ,.-_ABCDEFGHIJKLMNOPQRSTU
#W WXYZ,.-_ABCDEFGHIJKLMNOPQRSTUV
#X XYZ,.-_ABCDEFGHIJKLMNOPQRSTUVW
#Y YZ,.-_ABCDEFGHIJKLMNOPQRSTUVWX
#Z Z,.-_ABCDEFGHIJKLMNOPQRSTUVWXY
#, ,.-_ABCDEFGHIJKLMNOPQRSTUVWXYZ
#. .-_ABCDEFGHIJKLMNOPQRSTUVWXYZ,
#- -_ABCDEFGHIJKLMNOPQRSTUVWXYZ,.
#_ _ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-