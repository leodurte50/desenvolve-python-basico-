idade_juliana = int (input())
idade_cris = int (input())

#prosessamento 
#true se ambos forem maior de idade
#<exp1> Juliana é maior de idade
#<exp2> Cris é maior de idade
#<exp1> and <exp2>
#false sem qualquer outro caso
pode_entrar = idade_juliana>= 18 and idade_cris>= 18
print (pode_entrar)