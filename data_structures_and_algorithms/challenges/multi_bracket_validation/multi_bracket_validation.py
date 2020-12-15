list1=['{','(','[']
list2=['}',')',']']
def multibracketvalidation(str):#{[]}
    stack=[] #{[

    for i in str:
        if i in list1:
            stack.append(i) 
        elif i in list2:
            index=list2.index(i) #index=2
            if len(stack)>0 and list1[index]==stack[len(stack)-1]:
                stack.pop()
            else:
                return False
            
    if len(stack)==0:
        return True
    else:
        return False

print(multibracketvalidation('()[[Extra Characters]]'))
print(multibracketvalidation('{[]{(])}}'))
