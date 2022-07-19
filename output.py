from inputs import * 

def  output(pvs,array_input_index, restriction_number):
#    tabular=print_inputs(restriction_number,array_input_index)
    print ("&-------> AND\n|-------> OR")
    (teste, teste_raw)=((list(input("set(pvs.Restr0) & set(pvs.Restr1)\n"))),raw_input("Write again to confirm"))
    print teste_raw
    txt_result=open("resultPOSVS.txt", "w") 
    txt_result.write("-----Results----- \n")
    #write table in txt file
    txt_result.write("\n-----------------------------------------------------------------------------\n")
    txt_result.write("{:<20} {:<15} {:<10} {:<10}".format("Restr number","Bond", "Aminoacid","Number"))
    txt_result.write("\n-----------------------------------------------------------------------------\n")
    for index in range(restriction_number):
        restriction=array_input_index[index][0]
        array_input=array_input_index[index][1]
        #print data
        txt_result.write("{:<20} {:<15}".format(restriction,array_input))
    txt_result.write("\n\n\n\n----------------------Restriction choosed: %s----------------------\n" %teste_raw)
    txt_result.write("\n\n&-------> AND\n|-------> OR")
    for i in teste:
        txt_result.write("\n %s\n" %i)




   
