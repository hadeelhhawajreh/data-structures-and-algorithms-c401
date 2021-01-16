from data_structures_and_algorithms.challenges.left_join.left_join import left_join
def test_case1():
    dict_left={
        'A':'Ramesh',
        'B':'Khilan',
        'C':'Chaitali',
        'D':'Komal',} 
    dict_right={
        'A':'Muffy',
        'C':'Hardik',
        'D':'Mufrdik',
        'F':'frdik',}
    assert left_join(dict_left,dict_right)==[['A', 'Ramesh', 'Muffy'], ['B', 'Khilan', None], ['C', 'Chaitali', 'Hardik'], ['D', 'Komal', 'Mufrdik']]

def test_case_len():
    dict_left={
        'A':'Ramesh',
        'B':'Khilan',
        'C':'Chaitali',
        'D':'Komal',}

     
    dict_right={
        'A':'Muffy',
        'C':'Hardik',
        'D':'Mufrdik',
        'F':'frdik',}
    assert len(left_join(dict_left,dict_right))==4
