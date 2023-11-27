class Cpf:
    def __init__(self, cpf_cliente):
        cpf = str(cpf_cliente)
        if self.valida_tamanho(cpf):
            self.cpf = cpf
            print(cpf_cliente)
        else:
            raise ValueError("CPF INVÁLIDO")

    def __str__(self):
        return self.formatar_cpf()

    def valida_tamanho(self, cpf):
        if len(cpf) == 11:
            return True
        else:
            return False

    def formatar_cpf(self):
        grupo_um = self.cpf[:3]
        grupo_dois = self.cpf[3:6]
        grupo_tres = self.cpf[6:9]
        grupo_quatro = self.cpf[9:]
        return ("{}.{}.{}-{}".format(grupo_um, grupo_dois, grupo_tres, grupo_quatro)

        )
