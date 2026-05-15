from datetime import datetime, timedelta

class Insumo:
    """Classe base (Produto)"""
    def __init__(self, nome: str, data_entrada: str):
        self.nome = nome
        self.data_entrada = datetime.strptime(data_entrada, "%Y-%m-%d")
        self.data_vencimento = None

    def precisa_de_alerta(self) -> bool:
        if not self.data_vencimento:
            return False
        # Simula a verificação com base em uma data "atual" fictícia (ex: 15/05/2026)
        data_atual = datetime(2026, 5, 15)
        prazo_limite = data_atual + timedelta(days=2)
        return data_atual <= self.data_vencimento <= prazo_limite


class InsumoPerecivel(Insumo):
    """Produto Concreto para itens de rápida deterioração (ex: carnes, laticínios)"""
    def __init__(self, nome: str, data_entrada: str, dias_validade: int = 5):
        super().__init__(nome, data_entrada)
        # Perecíveis definem o vencimento estrito a partir da entrada
        self.data_vencimento = self.data_entrada + timedelta(days=dias_validade)


class InsumoNaoPerecivel(Insumo):
    """Produto Concreto para itens de longa validade (ex: enlatados, grãos)"""
    def __init__(self, nome: str, data_entrada: str, data_vencimento_fornecedor: str):
        super().__init__(nome, data_entrada)
        # Não perecíveis adotam a data gravada pelo fornecedor na embalagem
        self.data_vencimento = datetime.strptime(data_vencimento_fornecedor, "%Y-%m-%d")


class InsumoFactory:
    """A Factory (Criador) que encapsula a lógica de instanciação"""
    @staticmethod
    def criar_insumo(tipo: str, nome: str, data_entrada: str, **kwargs) -> Insumo:
        tipo = tipo.upper()
        if tipo == "PERECIVEL":
            dias = kwargs.get("dias_validade", 5)
            return InsumoPerecivel(nome, data_entrada, dias_validade=dias)
        elif tipo == "NAO_PERECIVEL":
            dt_venc = kwargs.get("data_vencimento_fornecedor")
            if not dt_venc:
                raise ValueError("Insumos não perecíveis exigem a data do fornecedor.")
            return InsumoNaoPerecivel(nome, data_entrada, dt_venc)
        else:
            raise ValueError(f"Tipo de insumo '{tipo}' é desconhecido.")