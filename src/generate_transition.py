# prism Transition 파트 생성
def generate_transition(transition, corpus, transition_sum):

    '''
    global transition
    global corpus
    global transition_sum
    print(transition)
    '''

    dtmc_code = ""
    
    dtmc_code += "dtmc\n\n"
    dtmc_code += "const init_y=0\n\n"
    dtmc_code += "module DTMC\n"
    dtmc_code += "  y:[0..{}] init init_y;\n\n".format(len(corpus)-1)
    
    for i in range(0, len(transition)):
        status = False
        dtmc_code += "  [] (y={}) -> ".format(i)
        for j in range(0, len(transition[i])):
            if transition[i][j] != 0:
                if status:
                    dtmc_code += " + "
                    
                dtmc_code += "{}:(y'={})".format(int(transition[i][j]/transition_sum[i]) if transition[i][j]/transition_sum[i] == 1.0 else transition[i][j]/transition_sum[i], j)
                status = True
        dtmc_code += ";\n"
    dtmc_code += "endmodule\n\n"
    
    print(dtmc_code)
    return dtmc_code