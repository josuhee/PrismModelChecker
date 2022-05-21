def create_s_corpus_location(corpus, s_corpus):
	# 2차원 list 생성
	result = []
	for idx in s_corpus:
		result.append([])

	# search
	idx = 0
	for state in corpus:
		state_split = state.split("_")
		for word in state_split:
			try:
				result[s_corpus.index(word)].append(idx)
			except:
				pass
		idx = idx + 1
	
	return result