def generate_decision(label_location, s_corpus):
    
    dtmc_code = ""
    
    try:
        decision_state = set(label_location[s_corpus.index("decision")])
        roll = ["PM", "ME", "UI", "ID"]
        
        for i in range(0, len(roll)):
            roll_state = set(label_location[s_corpus.index(roll[i])])
            intersection_state = roll_state | decision_state
            dtmc_code += 'rewards "r_' + roll[i] + '_decision"\n'
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