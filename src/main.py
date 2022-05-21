corpus = list()
s_corpus = list()

# 파일 출력 및 corpus, s_corpus 저장
def open_file():
	f = open("../file/sample-sequence.txt", "r")

	global corpus
	global s_corpus

	while True:
		state = f.readline()
		if not state:
			break
		state = state.strip()
		if state not in corpus:
			corpus.append(state)
			state_split = state.split("_")
			for i in state_split:
				if i not in s_corpus:
					s_corpus.append(i)

	

if __name__=='__main__':
	open_file()
	
	'''
	# corpus, s_corpus 테스트
	print("corpus!!!\n\n\n")
	print(corpus)
	print()
	print("s_corpus\n\n\n")
	print(s_corpus)
	print()
	'''