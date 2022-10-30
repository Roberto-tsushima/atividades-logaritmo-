ano = 1
pop_a = 15000*1.1
pop_b = 45000*1.05
while pop_a < pop_b:
    pop_a = pop_a * 1.1
    pop_b = pop_b * 1.05
    ano = ano + 1
print (f"A quantidade de anos é : {ano}")

ano = 1
pop_a = 15000*1.1
pop_c = 65000*1.025
while ((pop_a - pop_c)/pop_c) <= 0.23:
    pop_a = pop_a * 1.1
    pop_c = pop_c * 1.025
    ano = ano + 1
print (f"A quantidade de anos é : {ano}")
print(f'{pop_a:.0f}')
print(f'{pop_c:.0f}')