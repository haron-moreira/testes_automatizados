def salario_liquido(valor_hora_aula, num_aulas, percentual_inss):
    valor_bruto = valor_hora_aula*num_aulas
    return round(valor_bruto - (((valor_bruto) * percentual_inss) / 100),2)

