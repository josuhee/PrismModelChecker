def generate_label(corpus):
	label = ''
	for i in range(0, 269):
		label = label + 'label ' + '\"' + corpus[i] + '\" = (y=' + str(i) + ');\n'
	return label