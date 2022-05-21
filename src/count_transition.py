# 각 state마다의 transition count
def count_transition(transition, corpus, origin_corpus, transition_sum):

    '''
    global transition
    global corpus
    global origin_corpus
    global transition_sum
    '''
    
    transition = [[0 for col in range(len(corpus))] for row in range(len(corpus))]
    transition_sum = [0 for row in range(len(corpus))]
    previous = corpus.index("UseStart")
    current = previous
    for i in range(1, len(origin_corpus)-1):
        try:
            current = corpus.index(origin_corpus[i])
            
            transition[previous][current] += 1
            
            previous = current
        except:
            print("{}은(는) 존재하지 않습니다.".format(origin_corpus[i]))
            continue
		
    for i in range(0, len(transition)):
        for j in range(0, len(transition[i])):
            transition_sum[i] = transition_sum[i] + transition[i][j]
    
    '''
	# transition 출력
	for i in transition:
		print(i)
    '''
    return transition, transition_sum