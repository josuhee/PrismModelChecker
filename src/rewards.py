def generate_rewards(corpus):
	rewards = ''
	for i in range(0, 269):
		r_corpus = 'r_' + corpus[i]
		rewards = rewards + 'rewards \"' + r_corpus + '\"\n' + '  (y=' + str(i) + ') : 1;\n' + 'endrewards\n\n'
		
	rewards = rewards + 'rewards \"r_Steps\"\n' + '\t[] true : 1;\n' + 'endrewards\n'
	return rewards