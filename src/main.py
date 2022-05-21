import io_file as io
import count_transition as init_trans
import transition as trans
import word as w
import label as l
import rewards as r
import decision as d

if __name__=='__main__':
	corpus = list()
	s_corpus = list()
	origin_corpus = list()
	transition = list()
	transition_sum = 0
	result = ""

	corpus, s_corpus, origin_corpus = io.open_file(corpus, s_corpus, origin_corpus)
	transition, transition_sum = init_trans.count_transition(transition, corpus, origin_corpus, transition_sum)
	
	result += trans.generate_transition(transition, corpus, transition_sum)
	result += l.generate_label(corpus) + '\n'
	result += r.generate_rewards(corpus) + '\n'
	result += w.generate_word(corpus, s_corpus) + '\n'
	result += d.generate_decision(corpus, s_corpus)

	io.write_file(result)