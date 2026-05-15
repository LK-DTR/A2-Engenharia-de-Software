from models import InsumoFactory
from observers import SistemaAlertasPush, PainelCozinha

class GerenciadorEstoque:
    """O Sujeito (Subject) que monitora o estado e notifica os observadores"""
    def __init__(self):
        self._insumos = []
        self._observers = []

    def adicionar_observador(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remover_observador(self, observer):
        self._observers.remove(observer)

    def notificar_observadores(self, insumo_nome: str, mensagem: str):
        for observer in self._observers:
            observer.update(insumo_nome, mensagem)

    def cadastrar_insumo(self, tipo: str, nome: str, data_entrada: str, **kwargs):
        # Utiliza a Factory para criar o objeto correto sem conhecer sua classe concreta
        novo_insumo = InsumoFactory.criar_insumo(tipo, nome, data_entrada, **kwargs)
        self._insumos.append(novo_insumo)
        print(f"\n[SUCESSO] {nome} cadastrado com sucesso no estoque.")

        # Verifica imediatamente a regra de negócio de alta prioridade (Alerta 48h)
        if novo_insumo.precisa_de_alerta():
            msg = f"Atenção! Vence em menos de 48h ({novo_insumo.data_vencimento.strftime('%d/%m/%Y')})."
            self.notificar_observadores(nome, msg)


if __name__ == "__main__":
    # Inicializa o sistema principal (Controller)
    sistema = GerenciadorEstoque()

    # Instancia e registra os sistemas de alerta (Observers)
    alerta_gerente = SistemaAlertasPush()
    painel_fisico = PainelCozinha()
    
    sistema.adicionar_observador(alerta_gerente)
    sistema.adicionar_observador(painel_fisico)

    print("--- ECOFLOW: SIMULAÇÃO DE ENTRADA DE ESTOQUE ---")
    
    # Caso 1: Item Perecível longe do vencimento (Entrou em 14/05, vence em 19/05, hoje é 15/05)
    sistema.cadastrar_insumo(
        tipo="PERECIVEL", 
        nome="Filé de Salmão 5kg", 
        data_entrada="2026-05-14", 
        dias_validade=5
    )

    # Caso 2: Item Perecível em estado crítico (Entrou em 11/05, vence em 16/05, hoje é 15/05 - Menos de 48h!)
    # Isso acionará automaticamente os observadores acoplados ao sistema
    sistema.cadastrar_insumo(
        tipo="PERECIVEL", 
        nome="Creme de Leite Fresco Lote B", 
        data_entrada="2026-05-11", 
        dias_validade=5
    )

    # Caso 3: Item Não Perecível crítico (Entrou hoje, mas o lote do fornecedor vence amanhã: 16/05)
    sistema.cadastrar_insumo(
        tipo="NAO_PERECIVEL", 
        nome="Molho de Tomate Pelati Saboroso", 
        data_entrada="2026-05-15", 
        data_vencimento_fornecedor="2026-05-16"
    )