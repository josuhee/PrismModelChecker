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

def generate_get_state(states):
	result = ""
	for state in states:
		result += '(y = {})'.format(state)
		if states[-1] != state:
			result += " | "
	
	return result

def generate_word(corpus, s_corpus):
	word_lists = create_s_corpus_location(corpus, s_corpus)

	result = ""
	idx = 0
	for word_list in word_lists:
		if s_corpus[idx] == 'UseStart' or s_corpus[idx] == 'UseStop':
			idx += 1
			continue
		result += "label \"{}\" = {};".format(s_corpus[idx], generate_get_state(word_list))
		result += "\n\n"
		result += "rewards \"r_{}\"\n  {} : 1;\n".format(s_corpus[idx], generate_get_state(word_list))
		result += "endrewards\n\n"
		idx += 1
	
	return result