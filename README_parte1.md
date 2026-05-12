# Parte 1: Engenharia de Requisitos

## Tarefa 1.1: Proposta de Tema

### Sistema de Gestão de Resíduos para Pequenos Restaurantes

- **Problema:** Restaurantes desperdiçam matéria-prima por falta de controle de validade e descarte incorreto.

- **Usuários:** Gerentes de cozinha e donos de restaurante.

- **Por que é relevante:** Redução de custos e melhora do controle de qualidade do estabelecimento.

## Tarefa 1.2: Planejamento de Entrevista

- **Objetivo:** Compreender como o gerente ou demais funcionários identifica o desperdício hoje e quais os pontos cegos no estoque que levam ao descarte de insumos.

- **Perguntas:**

    1. (Aberta) Como é feito o registro da entrada de insumos e como você acompanha a validade deles hoje?

    2. (Aberta) Qual o critério usado para decidir que um alimento não serve mais para o preparo e deve ir para o lixo?

    3. (Aberta) Se você pudesse eliminar uma tarefa manual no fechamento do estoque, qual seria?

    4. (Fluxo) Quando um fornecedor entrega uma carga, quais informações você anota e onde as armazena?

    5. (Fluxo) Descreva o passo a passo de como a equipe de cozinha reporta que um ingrediente estragou.

    6. (Frustração) Qual a maior dificuldade em manter planilhas ou sistemas de estoque atualizados em tempo real?

    7. (Frustração) Qual foi a maior perda de estoque no último mês e por que ela não foi prevista ou evitada?

    8. (Encerramento) Se o sistema gerasse um alerta agora, qual informação seria vital para você agir antes de perder um produto?

> Minha reflexão: Todas as perguntas cumprem os requisitos e juntas ajudam a entender melhor o problema e como melhor aplicar uma solução ideal.

## Tarefa 1.3: Historias de Usuario

1. Como gerente de cozinha, quero registrar insumos com data de validade via leitura de código de barras ou etiqueta, para que o sistema monitore o frescor automaticamente.

    Critérios de Aceitação:
    1. O sistema deve ler códigos padrão EAN-13.
    2. Deve permitir inserção manual da data de validade.
    3. Deve emitir confirmação sonora de item registrado.

    Prioridade: Alta (Base de dados para tudo o que segue).

2. Como gerente, quero receber alertas no celular 48h antes de um insumo vencer, para que eu possa priorizar o uso dele no cardápio do dia.

    Critérios de Aceitação:
    1. Notificação push configurável.
    2. Lista de itens próximos ao vencimento na tela inicial.
    3. Opção de marcar insumo como usado.

    Prioridade: Alta (Principal valor do sistema).

3. Como cozinheiro, quero registrar o motivo de um descarte (vencimento, erro de preparo, queda), para ajudar o dono a entender onde estão as perdas.

    Critérios de Aceitação:
    1. Botão de "Registro de Perda" rápido.
    2. Lista suspensa com motivos pré-definidos.
    3. Campo opcional para foto do descarte.

    Prioridade: Média (Gera dados valiosos, mas o sistema funciona sem isso).

4. Como dono do restaurante, quero ver um relatório mensal do valor financeiro jogado no lixo, para ajustar as quantidades de compra com os fornecedores.

    Critérios de Aceitação:
    1. Gráfico de perdas por categoria.
    2. Comparativo com o mês anterior.
    3. Exportação em PDF/Excel.

    Prioridade: Média (Essencial para o ROI a longo prazo).

5. Como gerente de cozinha, quero gerar uma lista de compras automática baseada nos itens descartados, para repor o estoque rapidamente sem erros.

    Critérios de Aceitação:
    1. Integração com o saldo atual.
    2. Sugestão de quantidade baseada na média de uso.
    3. Botão de compartilhamento da lista via WhatsApp.

    Prioridade: Baixa (Conveniência, não resolve o problema do desperdício diretamente).

> Minha reflexão: A escrita das histórias revelou que o sistema precisa ser rápido e prático, pois na rotina corrida o gerente de cozinha não tem tempo de sentar em um computador durante o turno.