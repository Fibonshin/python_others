replaces={"s":"ら","a":"て","d":"れ","w":"る"," ":"ー","q":"え","e":"ん","f":"♪","r":"た"}

S=input()
result=""
for c in S:
    for key,val in replaces.items():
        if(c==key):
            result+=val

print(result)