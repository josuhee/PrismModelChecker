# 파일 출력 및 corpus, s_corpus 저장
def open_file(corpus, s_corpus, origin_corpus):
    '''
    global corpus
    global s_corpus
    global origin_corpus
    '''

    f = open("../file/sample-sequence.txt", "r")
    
    while True:
        state = f.readline()
        if not state:
            break
        state = state.strip()
        origin_corpus.append(state)
        if state not in corpus:
            corpus.append(state)
            state_split = state.split("_")
            for i in state_split:
                if i not in s_corpus:
                    s_corpus.append(i)
    
    return corpus, s_corpus, origin_corpus