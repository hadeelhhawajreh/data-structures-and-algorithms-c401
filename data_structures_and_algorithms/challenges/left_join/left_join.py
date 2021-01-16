def left_join(dict_left,dict_right):
    output=[]
    for i in dict_left.keys():
        print(type(dict_left.keys()),i)
        if i in dict_right.keys():
            output.append([i,dict_left[i],dict_right[i]])
        else:
            output.append([i,dict_left[i],None])
    return output


if __name__ == "__main__":
    dict_left={
        'A':'Ramesh',
        'B':'Khilan',
        'C':'Chaitali',
        'D':'Komal',
    } 

    
    dict_right={
        'A':'Muffy',
        'C':'Hardik',
        'D':'Mufrdik',
        'F':'frdik',
    }
    print(left_join(dict_left,dict_right))

