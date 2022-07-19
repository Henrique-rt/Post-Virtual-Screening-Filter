# -*- coding: utf-8 -*-

def inputs():
    #definindo inputs do programa
    array_input=[]
    restriction_dictionary={} #dicionario para mudar o index
    array_index=[]
    array_input_index=[]
    #numero de ligacoes que deseja restringir
    try:
        restriction_number=int(raw_input("Escolha o numero de restricoes q desejafazer \n"))
    except ValueError:
        print ("Deve ser um numero")
    #definindo as restricoes dada o numero de restricoes
    for restriction in range(restriction_number):
        bond_restriction_options=['Hydrophobic Interactions','Hydrogen Bonds', 'Water Bridges','Salt Bridges','pi-Stacking', 'pi-Cation Interactions','Halogen Bonds','Metal Complexes']
        bond_restriction_index=int(input("Escolha uma ligação:\n[0]=>Hydrophobic Interactions\n[1]=>Hydrogen Bonds\n[2]=>Water Bridges\n[3]=>Salt Bridges\n[4]=>pi-Stacking\n[5]=>pi-Cation Interactions\n[6]=>Halogen Bonds\n[7]=>Metal Complexes\n"))
        #index da restricao escolhida
        bond_restriction=bond_restriction_options[bond_restriction_index]
        residue=raw_input("Escolha um ligante no seguinte formato: ALA\n")
        if type(residue) is not str:
            print ("Deve ser um aminoácido")
        residue_number=int(raw_input("Escolha o numero ligante de acordo com sua enumeracao correta\n"))
        array_input.append((bond_restriction, residue, residue_number))
        restriction_dictionary["Restr{0}".format(restriction)]=array_input[restriction]
    for new_index in restriction_dictionary:
        array_index.append(new_index)
    array_index=sorted(array_index)
    array_input_index=zip(array_index, array_input)
    return array_input, array_input_index, array_index, restriction_number
    
    
def print_inputs(restriction_number,array_input_index):
    print("-----------------------------------------------------------------------------")
    print ("{:<20} {:<15} {:<10} {:<10}".format("Restr number","Bond", "Aminoacid","Number"))
    print("-----------------------------------------------------------------------------")
    for index in range(restriction_number):
        restriction=array_input_index[index][0]
        array_input=array_input_index[index][1]
        #print data
        print ("{:<20} {:<15}".format(restriction,array_input))



