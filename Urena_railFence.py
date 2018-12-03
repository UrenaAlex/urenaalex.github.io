EncOrDec = input('Hello user would you like to "Encrypt" or "Decrypt"? : ')

if (EncOrDec=="Encrypt" or EncOrDec=="encrypt"):
    print("Okay... ")
    plainText=input("Please enter a message you would like to Encrypt: ")
elif(EncOrDec=="Decrypt" or EncOrDec=="decrypt"):
    print("Okay... ")
    cipherText=input("Please enter the message you would like to Decrypt: ")
    
def Scramble2Text(plainText):
    #statement = input("Hello user please enter a statement: ")
    #I am calling the odd letters "even" and vice versa.
    even=""
    odd=""
    charCount=1
    for ch in plainText:
        charCount=charCount+1
        y=charCount
        if (y%2==0):
            even=even+ch
        elif(y%2==1):
            odd=odd+ch
    cipherText=(even+odd)
    return(even+odd)

def DecryptMessage(cipherText):
    #statement = input("Hello user please enter scrambled message: ")
    add=0
    acc=''
    bacc=''
    cacc=''
    dacc=''
    ct1=0
    ct2=0
    act1=0
    act2=0
    line=''
    x=0
    for ch in cipherText:
        add=add+1
    if (add%2==1):
        for ch in cipherText:
            ct2 = ct2+1
            if (ct2<=((.5*add)+.5)):
                cacc=cacc+ch
            elif (ct2>(.5*add)):
                dacc=dacc+ch
    elif (add%2==0):
        for ch in cipherText:
            ct1=ct1+1
            if (ct1<=(.5*add)):
                cacc= cacc+ch
            elif(ct1>(.5*add)):
                 dacc=dacc+ch
    for i in range(add):
        for ch in cacc:
            if (x==i):
                line=line+ch
            x=x+1
        x=0
        for ch in dacc:
            if(x==i):
                line=line+ch
            x=x+1
        x=0
    c=cacc
    d=dacc
    #print(cacc)
    #print(dacc)
    decryptedmessage=(line)
    return(line+"")

if (EncOrDec=="Encrypt" or EncOrDec=="encrypt"):
    cipherText=(Scramble2Text(plainText))
    print(cipherText)
elif(EncOrDec=="Decrypt" or EncOrDec=="decrypt"):
    decryptedMessage=(DecryptMessage(cipherText))
    print(decryptedMessage)

    
          
