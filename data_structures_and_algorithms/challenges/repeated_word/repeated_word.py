from collections import Counter  
import re
def repeat_word(input):
    arr = []
    repeat = ''
    words = re.sub(r'[^\w\s]','',input, re.UNICODE).split()
    # print('words ---->',words)
    #  ['It', 'was', 'a', 'queer', 'sultry', 'summer', 'the', 'summer', 
    # 'they', 'electrocuted', 'the', 'Rosenbergs', 'and', 'I', 'didnt', 'know', 
    # 'what', 'I', 'was', 'doing', 'in', 'New', 'York']
    for ele in words: 
        if ele in arr: 
            repeat = ele
            break
        arr.append(ele) 
    # print(arr)
    return repeat



def Repeat2(input):  
    words = input.lower().replace(',',' ').replace('.',' ').replace('?',' ').split()      
    dict = Counter(words)
    print(dict)
    print('most common', Counter.most_common(dict)[0])
    for key in words:  
        if dict[key]>1:  
            print (key, dict[key])  
            return
if __name__ == "__main__":  
    x="Once upon a time, there was a brave princess who..."
    print("🚀 ~ file: repeated_word.py ~ line 27 ~ x", repeat_word(x))
    
    y="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."	
    print("🚀 ~ file: repeated_word.py ~ line 30 ~ x", repeat_word(y))

    z="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    print("🚀 ~ file: repeated_word.py ~ line 42 ~ repeat_word ", '   ', repeat_word(z))



