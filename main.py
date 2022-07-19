from inputs import * 
from ligand_complex_preparation import *
from run_plip import * 
from output import *

def main():
    array_input, array_input_index, array_index, restriction_number=inputs() #definindo as variaveis de input
    print_inputs(restriction_number,array_input_index)  #imprimindo as variaveis
    ligand_complex_preparation() #gerar PDB com alvo e ligante 
    database_result=run_plip(restriction_number, array_index, array_input) #armazenar conjunto de dados resultante das restricoes
    output(database_result,array_input_index,restriction_number) #imprimir em arquivo de txt as moleculas pos filtro

if __name__ == "__main__":
    main()
