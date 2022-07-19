# -*- coding: utf-8 -*-
import pybel
import openbabel
import os
import sys
from pymol import cmd
import pymol
from os import path

def ligand_complex_preparation():
    directory=os.getcwd()
    result_directory="complex_PDB"
    path_result_directory=os.path.join(directory,result_directory)
    check_complex_directory=path.exists(path_result_directory)
    if check_complex_directory is True:
        pass
    else:
        #criar pasta para resultados
        os.mkdir(path_result_directory)
        print path_result_directory
        ligand_directory=directory+"/ligand/"
        target_directory=directory+"/target/"
        target=os.listdir(target_directory)[0]
        pymol.pymol_argv = ['pymol', '-qc'] + sys.argv[1:]
        pymol.finish_launching()
        cmd = pymol.cmd
        #rodar sobre todos ligantes
        for ligands in os.listdir(ligand_directory):
            ligands_ext=ligands.split(".",1)
            ligands_name=ligands_ext[0]
            cmd.reinitialize()
            cmd.load(target_directory+target) #carregar alvo
            cmd.load (ligand_directory+ligands,"ligand" ,0,"sdf" ,1,-1,0) #mol2 ou sdf, usuário deve alterar
            cmd.save("%s/%s_complex.pdb" %(path_result_directory,ligands_name), "all") #salvar resultado em pasta criada
        cmd.quit()



