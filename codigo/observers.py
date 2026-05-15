from abc import ABC, abstractmethod

class Observer(ABC):
    """Interface do Observador"""
    @abstractmethod
    def update(self, insumo_nome: str, mensagem: str):
        pass


class SistemaAlertasPush(Observer):
    """Observador Concreto 1: Envia alertas para o app móvel do gerente"""
    def update(self, insumo_nome: str, mensagem: str):
        print(f"[ALERTA PUSH] Notificação enviada ao Gerente -> {insumo_nome}: {mensagem}")


class PainelCozinha(Observer):
    """Observador Concreto 2: Atualiza o monitor físico dentro da cozinha"""
    def update(self, insumo_nome: str, mensagem: str):
        print(f"[PAINEL COZINHA] LOG -> Item crítico detectado: {insumo_nome}. {mensagem}")