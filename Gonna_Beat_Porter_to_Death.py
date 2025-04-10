#dimitri Workman
#steps to look up
#amount of collsions
#length of hash
import random
import string

# Initialize list with lowercase alphabets
#a = list(string.ascii_lowercase)
#print(a)

# Initialize list with uppercase alphabets
#b = list(string.ascii_uppercase)
#print(b)
global coll
global memoryUssage
global lookups
class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Relational methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        if other!=None:
            return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        if other!=None:
            return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'
    def increase(self):
        self.count+=1


        

        
def buckets(poem):
    length=192
  

    #print("")
   # print("calling add")
    collide=0
    mods=createHashs()
    megaList=[]
    keyList=[]
    indexList=[]
    
    for x in poem:
        #global randon
        key=find_key(x)
        keyList.append(key)
  
   
   # print(keyList,len(keyList))
   # for x in mods:
        
    tracker=0
    newlist=[None]*length
    p=[]
    for z in keyList:
            index=z%192
            
            value=poem[tracker]                
            tracker+=1
            item=Pair(value)
        
            #print(index)
            #print(newlist)
            #print(len(newlist))
           # print(z)
            if newlist[index]==None:
                newlist[index]=item
                #newlist.insert(index,item)
            elif newlist[index].letter==item.letter:
               # print("Index:",index)
                Temp=newlist[index]
                Temp.increase()
            else:
                collide+=1
                tempMove=index
                tempMove+=1
                if tempMove>=length:
                    newlist.append(item)
                    length+=1
                    pass
                if newlist[tempMove]==None:
                    newlist[tempMove]=item
                  #  print("added: ",item)
                elif newlist[tempMove].letter==item.letter:
                    temp=newlist[tempMove]
                    temp.increase()
                
                    
                else:
                    added=True
                    print("Is it adding:",item)
                    while added:
                        tempMove+1
                        
                        if tempMove>=len(newlist)-1:
                            added=False
                            newlist.append(item)
                            print("Did it append: ",item)
                            
                        if newlist[tempMove]==None:
                            newlist[tempMove]=item
                            added=False
                            print("did it add: ",item)
                        elif newlist[tempMove].letter==item.letter:
                            temp=newlist[tempMove]
                            temp.increase()
                            print("did it increase: ", item)
                            added=False
                        

    
                    
                
                
                
      #  megaList.append(newlist)
    print(newlist)
    #print(p)
    return length,collide,newlist
        
# bucket exit it out of score once reach as the other min keep leaving
#def bucketScorer(hash):
def searching(word,array):

    
    lookups=0
    key=find_key(word)
    index=key%192
    
    item=Pair(word)
    
    print(array[index])
    print(key)
    print(word)

    if array[index].letter==item.letter:
        lookups+=1
        print("The item was found at index %f"%(index))
        print(array[index])
        return(array[index].count,lookups)
   
    elif index>=0 and index<len(array):
        tempMove=index
        lookups+=1
        for x in range(0,10):
            tempMove+=1
            if array[tempMove].letter==item.letter:
                print("The item was found at index %f."%(tempMove))
                print(array[tempMove])
                lookups+=1
                return(array[tempMove],lookups)
            else:    
                break
        

    
def words_in(thingy):
    
    return buckets(thingy)
def lookup_word_count(word,hash):
    return searching(word,hash)



def createHashs():
    theValues=[]
    for x in range(10,100):
        theValues.append(x)
    return theValues





def find_key(word):
    mapThe={}
    alph=list(string.ascii_letters)
    tempkey=0
    for x in alph:
            tempkey+=13
            mapThe[x]=tempkey
    key=0
   # print(rand)
    #print(word)
   # print("Gives keys vaule",end=": ")
    for x in word:
        #if x.isalpha()!=True:
            #return key
        temp=mapThe[x]
        key+=temp
    #print(key)
    return key        



def main():
    hashy=[]
    rand=[]
    usedvaluesInfo=[]
    mapThe={}
    alph=list(string.ascii_letters)
    tempkey=0
   
    #call add
    global randon; mapThe
    #tub=(words_in(mapThe,"When he was suprised it come as quite a shock to he e a b c d e f g h i j k l apple bannana try again filler words more fillest fller yada bebop try lets ago",50))
    #
    #print(tub)
    #print(len(tub))
    #searching(mapThe,"he", tub)
        



    
if __name__ =="__main__":
    main()

#order buckets 
#thin binary search

