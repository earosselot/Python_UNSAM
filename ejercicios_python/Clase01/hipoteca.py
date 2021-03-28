# hipoteca.py

# Ejercicio 1.7

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0

# while saldo > 0:
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual

# print('Total pagado', round(total_pagado, 2))

#-------------------------------
# Ejercicio 1.8

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses = 0

# while saldo > 0:
#     if meses < 12:
#         pago_mensual = 2684.11 + 1000
#     else:
#         pago_mensual = 2684.11
#     meses += 1
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual

# print('Total pagado', round(total_pagado, 2), 'en', meses, 'meses.')

#-------------------------------
# Ejercicio 1.9

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses = 0
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000

# while saldo > 0:
#     meses += 1

#     if pago_extra_mes_comienzo <= meses <= pago_extra_mes_fin:
#         pago_mensual = 2684.11 + pago_extra
#     else:
#         pago_mensual = 2684.11
    
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual

# print('Total pagado', round(total_pagado, 2), 'en', meses, 'meses.')


#-------------------------------
# Ejercicio 1.10

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses = 0
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000

# while saldo > 0:
#     meses += 1

#     if pago_extra_mes_comienzo <= meses <= pago_extra_mes_fin:
#         pago_mensual = 2684.11 + pago_extra
#     else:
#         pago_mensual = 2684.11
    
#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual
#     print(meses, round(total_pagado, 2), round(saldo, 2))

# print('Total pagado: ', round(total_pagado, 2), '\n Meses: ', meses)


#-------------------------------
# Ejercicio 1.11

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    meses += 1

    if pago_extra_mes_comienzo <= meses <= pago_extra_mes_fin:
        pago_mensual = 2684.11 + pago_extra
    else:
        pago_mensual = 2684.11
    
    if saldo < pago_mensual:
        pago_mensual = saldo * (1+tasa/12)

    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

    print(meses, round(total_pagado, 2), round(saldo, 2))

print('Total pagado: ', round(total_pagado, 2), '\n Meses: ', meses)


# -------------------------------------------------------------------------


# Ejercicio 1.20
# f-strings

# saldo = 500000.0
# tasa = 0.05
# pago_mensual = 2684.11
# total_pagado = 0.0
# meses = 0
# pago_extra_mes_comienzo = 61
# pago_extra_mes_fin = 108
# pago_extra = 1000

# print ('mes\ttotal pagado\tsaldo')

# while saldo > 0:
#     meses += 1

#     if pago_extra_mes_comienzo <= meses <= pago_extra_mes_fin:
#         pago_mensual = 2684.11 + pago_extra
#     else:
#         pago_mensual = 2684.11
    
#     if saldo < pago_mensual:
#         pago_mensual = saldo * (1+tasa/12)

#     saldo = saldo * (1+tasa/12) - pago_mensual
#     total_pagado = total_pagado + pago_mensual

#     print(f'{meses}\t{round(total_pagado, 2)}\t{round(saldo, 2)}')

# print(f'\nTotal pagado: {round(total_pagado, 2)}\nMeses: {meses}')
