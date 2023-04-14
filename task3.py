from nltk.tokenize import word_tokenize,sent_tokenize 
from nltk.stem import PorterStemmer,SnowballStemmer 
ps=PorterStemmer() 
sb=SnowballStemmer(language='english') 
text=input("inter your text") 
print("1: tokenize words 2: tokenize sentence 3: original text 4:stemming 4.1:porter Stemmer 4.2:Snowball Stemmer" ) 
 
 
choice=input("choose your number") 
if choice=="1": 
    print(word_tokenize(text)) 
elif choice == "2": 
    print(sent_tokenize(text)) 
elif choice =="3": 
    print(text) 
elif choice =="4.1": 
    print( ps.stem(text)) 
elif choice =="4.2":    
     print( sb.stem(text)) 
 
else: 
    print("wrong choice")