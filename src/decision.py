import word as w

def generate_decision(corpus, s_corpus):
	dtmc_code = ""
	label_location = w.create_s_corpus_location(corpus, s_corpus)

	try:
		decision_state = set(label_location[s_corpus.index("decision")])
		role = ["PM", "ME", "UI", "ID"]
		
		for i in range(0, len(role)):
			role_state = set(label_location[s_corpus.index(role[i])])
			intersection_state = role_state | decision_state
			dtmc_code += 'rewards "r_' + role[i] + '_decision"\n'
			intersection_state = list(intersection_state)
			intersection_state.sort()

			dtmc_code += "  ("
			status = False
			for j in range(0, len(intersection_state)):
				if status:
					dtmc_code += " | "
				dtmc_code += "(y = {})".format(intersection_state[j])
				status = True
			dtmc_code += ") : 1;\n"
			dtmc_code += "endrewards\n\n"

	except:
		pass

	return dtmc_code