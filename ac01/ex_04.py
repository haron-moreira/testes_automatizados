def fechar_conta(valor_gasto):
    taxa_servico = valor_gasto * 0.10
    valor_total = valor_gasto + taxa_servico

    return {"total":round(valor_total,2), "gorjeta":round(taxa_servico, 2)}
