from data_structures_and_algorithms.data_structures.queue_with_stacks.queue_with_stacks import *

def test_PseudoQueue():
    q=PseudoQueue()
    q.stackEnqueue(20)
    # q.stackEnqueue(15)
    # q.stackEnqueue(10)
    actual= q.stackDequeue()
    # print(q.stackDequeue())
    # print(q.stackDequeue())
    assert actual==20

def test_PseudoQueue_two():
    q=PseudoQueue()
    q.stackEnqueue(15)
    q.stackEnqueue(10)
    actual= q.stackDequeue()
    # print(q.stackDequeue())
    assert actual==15

def test_PseudoQueue_three():
    q=PseudoQueue()
    q.stackEnqueue(15)
    q.stackEnqueue(10)
    q.stackEnqueue(20)
    q.stackDequeue()
    q.stackDequeue()
    actual= q.stackDequeue()
    assert actual==20