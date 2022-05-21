corpus = list()
s_corpus = list()
origin_corpus = list()
transition = list()

# 파일 출력 및 corpus, s_corpus 저장
def open_file():
	f = open("../file/sample-sequence.txt", "r")

	global corpus
	global s_corpus
	global origin_corpus

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

# 각 state마다의 transition count
def count_transition():
	global transition
	global corpus
	global s_corpus
	global origin_corpus
	
	transition = [[0 for col in range(len(corpus))] for row in range(len(corpus))]
	previous = corpus.index("UseStart")
	current = previous
	for i in range(1, len(origin_corpus)-1):
		try:
			current = corpus.index(origin_corpus[i])
		except:
			print("{}은(는) 존재하지 않습니다.".format(origin_corpus[i]))
			continue
		transition[previous][current] += 1
		
		previous = current
	
	'''
	# transition 출력
	for i in transition:
		print(i)
	'''


if __name__=='__main__':
	open_file()
	count_transition()
	
	'''
	# corpus 개수 test
	print(len(corpus))
	print(len(s_corpus))
	for i in range(0, 10):
		print(origin_corpus[i])
	'''
	'''
	# corpus, s_corpus 테스트
	print("corpus!!!\n\n\n")
	print(corpus)
	print()
	print("s_corpus\n\n\n")
	print(s_corpus)
	print()
	'''