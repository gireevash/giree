def reverseWordSentence(Sen):  
    wor = Sen.split(" ") 
    newWords = [wor[::-1] for wor in wor] 
    newSentence = " ".join(newWords)   
    return newSentence 
Sen = input()
print(reverseWordSentence(Sen)) 
