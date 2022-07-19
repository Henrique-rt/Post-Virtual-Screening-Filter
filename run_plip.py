# -*- coding: utf-8 -*-
import os
import pandas as pd
import re

def run_plip(restriction_number, array_index, array_input):
    directory=os.getcwd()
    directory_complex=directory+"/complex_PDB/"
    array_result=[] 
    for restriction in range(restriction_number): #criar um vetor nulo do com o numero de restricoes
        array_result.append([])
    #rodar sobre todos arquivos complexados da pasta criada
    for filenames in os.listdir(directory_complex):
        os.system('python2.7 /home/henrique/pliptool/plip/plipcmd.py -f %s%s -t ' %(directory_complex, filenames)) #caminhho para plipcmd, deve ser alterada pelo usuario
        print("Running PLIP with %s as ligand" %filenames)
        for i in range(restriction_number): #separar cada subunidadade do vetor inputs_var=> inputs_var=[[lig1,res1,res_nmbr1],[lig2,res2,res_nmbr2],...]
            bond=array_input[i][0]
            residue=array_input[i][1]
            residue_number=array_input[i][2]
            with open("report.txt") as report:
                report_informartion=report.read()
                bond_finder=report_informartion.find("%s" %bond)#procurar ligacao definida
                if bond_finder !=-1: 
                    bond_report_index=report_informartion.index("%s" %bond)#index da ligacao no arquivo report.txt
                    end_bond_report_information=report_informartion.find("+\n\n\n", bond_report_index)
                    between=(report_informartion[bond_report_index:end_bond_report_information])#cria um intervalo do arquivo report.txt contendo as informacoes da ligacao
                    if re.search("%s\s*\W\s%s" %(residue_number, residue), between):
                        array_result[i].append(filenames)
                    else:
                        continue
                else:
                    continue
    #criar um dataframe com nome pvs
    pvs=pd.DataFrame(array_result, index=array_index)
    pvs=pvs.T
    print pvs
    return pvs
