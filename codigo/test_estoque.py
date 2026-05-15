import unittest
from datetime import datetime, timedelta
from models import InsumoFactory, InsumoPerecivel

class TestControleValidadeEcoFlow(unittest.TestCase):
    """Conjunto de testes para a lógica de criação e alertas de insumos"""

    # --- TESTES DO MÉTODO: precisa_de_alerta() ---
    
    def test_precisa_de_alerta_sucesso_dentro_do_prazo(self):
        """Cenário de Sucesso: Item vence em exatamente 24h (dentro da janela de 48h), deve alertar."""
        # Configura um item fictício simulando entrada para que vença amanhã (16/05/2026)
        # Lembrando que a data atual fixa do sistema é 15/05/2026
        insumo = InsumoFactory.criar_insumo(
            tipo="PERECIVEL", 
            nome="Creme de Leite", 
            data_entrada="2026-05-11", # 11 + 5 dias de validade = vence 16/05
            dias_validade=5
        )
        self.assertTrue(insumo.precisa_de_alerta())

    def test_precisa_de_alerta_falha_fora_do_prazo(self):
        """Cenário de Falha/Exceção Lógica: Item com validade segura (vence em 5 dias), não deve alertar."""
        insumo = InsumoFactory.criar_insumo(
            tipo="PERECIVEL", 
            nome="Filé de Salmão", 
            data_entrada="2026-05-15", # 15 + 5 dias de validade = vence 20/05
            dias_validade=5
        )
        # Falha em acionar o alerta (retorna False), o que é o comportamento correto aqui
        self.assertFalse(insumo.precisa_de_alerta())

    def test_precisa_de_alerta_borda_limite_exato(self):
        """Cenário de Borda: Item vence exatamente no limite das 48h (daqui a dois dias), deve alertar."""
        insumo = InsumoFactory.criar_insumo(
            tipo="PERECIVEL", 
            nome="Queijo Prato", 
            data_entrada="2026-05-12", # 12 + 5 dias de validade = vence 17/05 (exatas 48h)
            dias_validade=5
        )
        self.assertTrue(insumo.precisa_de_alerta())


    # --- TESTES DO MÉTODO: InsumoFactory.criar_insumo() ---

    def test_criar_insumo_sucesso_nao_perecivel(self):
        """Cenário de Sucesso: Criar um item não perecível com os parâmetros corretos."""
        insumo = InsumoFactory.criar_insumo(
            tipo="NAO_PERECIVEL",
            nome="Arroz 5kg",
            data_entrada="2026-05-15",
            data_vencimento_fornecedor="2026-12-31"
        )
        self.assertEqual(insumo.nome, "Arroz 5kg")
        self.assertEqual(insumo.data_vencimento, datetime(2026, 12, 31))

    def test_criar_insumo_excecao_data_ausente(self):
        """Cenário de Falha/Exceção: Tentar criar não perecível sem enviar a data do fornecedor."""
        # Deve lançar um ValueError conforme implementado na Factory
        with self.assertRaises(ValueError):
            InsumoFactory.criar_insumo(
                tipo="NAO_PERECIVEL",
                nome="Feijão Preto",
                data_entrada="2026-05-15"
                # Omitindo propositalmente 'data_vencimento_fornecedor'
            )

    def test_criar_insumo_borda_tipo_case_insensitive(self):
        """Cenário de Borda: O tipo enviado está em letras minúsculas ('perecivel'). Deve tratar e criar com sucesso."""
        insumo = InsumoFactory.criar_insumo(
            tipo="perecivel",  # Entrada em minúsculo
            nome="Leite Integral",
            data_entrada="2026-05-15",
            dias_validade=3
        )
        self.assertIsInstance(insumo, InsumoPerecivel)


if __name__ == "__main__":
    unittest.main()