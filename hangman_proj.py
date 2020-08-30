import random
source = ['invoker','project','hangman','rain','python']


randomWord = random.choice(source)

positionArray=[]
lengthOfWord=len(randomWord)
if lengthOfWord>1 and lengthOfWord<=4:
    positionArray=[0,2]
elif lengthOfWord>4 and lengthOfWord<=8:
    positionArray=[0,2,3]
elif lengthOfWord>8 and lengthOfWord<=12:
    positionArray=[2,4,5,6]

scrWrdList=[]
objective_dict={}
hiddenWord=''
for letter in randomWord:
    scrWrdList.append(letter)

for item in positionArray:
    objective_dict.update({item:scrWrdList[item]})
    scrWrdList[item]='*'
for item in scrWrdList:
    hiddenWord=hiddenWord+item

life = 5
updatedHiddenWord=''
hiddenWord, objectives, srcWrdlist = letterRemover(randomWord)
while(life!=0):


    if updatedHiddenWord=='':
        print("\nYour Challenge Word is : "+hiddenWord)
        usrInp=input("\n\tEnter your letter : ")
    else:
        print("\nYour Challenge Word is : "+updatedHiddenWord)
        usrInp = input("\n\tEnter your letter : ")
    updatedHiddenWord=''
    if usrInp in randomWord:
        print("\nYour answer is right!")
        for key,value in objectives.items():
            if usrInp==value:
                srcWrdlist[key]=value
        for item in srcWrdlist:
            updatedHiddenWord+=item
    elif usrInp not in randomWord:
        life = life - 1
        print("\nYour Answer is incorrect Try later, Current Life : " + str(life))
    if '*' not in updatedHiddenWord:
        if updatedHiddenWord!='':
            print("\nCongratulations you won")
            break
