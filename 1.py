salario_fixo = float(input("Insira o Valor do saLário fixo: "))
Vendas_efetuadas = float(input("Insira o valor das Vendas: "))
if Vendas_efetuadas <= 1500:
    Vendas_efetuadas = Vendas_efetuadas* 0.05
if Vendas_efetuadas >1500:
    Vendas_efetuadas = ((Vendas_efetuadas - 1500) * 0.07) + (1500 * 0.05)

salario_total = Vendas_efetuadas + salario_fixo
print (f'O salário total é de :{salario_total}')