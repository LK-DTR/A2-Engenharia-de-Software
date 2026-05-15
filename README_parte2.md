# Parte 2: Projeto e Desenvolvimento

## Tarefa 2.1: Definição da Arquitetura

- **Padrão escolhido:** MVC (Model-View-Controller)

- **Justificativa:** Separa a lógica de cálculo de validade (Model) da interface de alertas (View) e da lógica de entrada de dados via scanner (Controller). Isso facilita futuras mudanças, como trocar a interface de texto por um app mobile sem mexer nas regras de negócio.

- **Componentes e Responsabilidades:**

    Model (Estoque): Gerencia os dados dos insumos e verifica datas de validade.

    View (InterfaceAlerta): Exibe as notificações e relatórios para o usuário.

    Controller (GerenciadorEstoque): Recebe os inputs do scanner e decide quais Models e Views acionar.

- **Trade-off:** O MVC pode adicionar uma complexidade desnecessária para um protótipo muito pequeno, exigindo mais arquivos e "código de ligação" do que um script único.

- **Reflexão:** O padrão MVC possibilita a escalabilidade no futuro do projeto. Por exemplo, se decidirmos integrar o EcoFlow com balanças inteligentes no futuro, precisaremos apenas criar um novo Controller, mantendo a lógica de estoque intacta.

## Tarefa 2.2: Implementação com Padrões de Projeto 
Implementação para atender às histórias de usuário 1 e 2 do README_parte1

**Factory Method:**   

Diagrama Mental/Estrutural: InsumoFactory -> criar_insumo -> InsumoPerecivel ou InsumoNaoPerecivel.


Onde foi aplicado: No arquivo models.py dentro da classe estática InsumoFactory e consumido no método cadastrar_insumo em main.py.  


**Observer:** 

Diagrama Mental/Estrutural: GerenciadorEstoque (Subject) notifica -> classes derivadas de Observer (SistemaAlertasPush, PainelCozinha).


Onde foi aplicado: No arquivo observers.py (estrutura das interfaces) e disparado em main.py através do método notificar_observadores()

**Revisão Crítica:**
A classe InsumoFactory pode se tornar um gargalo caso o restaurante exija no futuro dezenas de novas categorias customizadas de alimentos, transformando o arquivo em um bloco de if/else difícil de manter.
  

## Tarefa 2.3: Testes

**Estratégia de Teste Adotada:**

A estratégia adotada focou em Testes de Unidade isolados usando o ecossistema padrão unittest do Python. O objetivo foi blindar as regras de negócio mais críticas do EcoFlow: a fábrica geradora de objetos (InsumoFactory) e o motor de cálculo de datas de expiração (precisa_de_alerta). Essa abordagem é altamente adequada para o atual estágio do protótipo, pois garante a integridade dos dados e evita falsos positivos/negativos nos alertas de desperdício antes de construirmos qualquer interface gráfica complexa.  

**O que não foi coberto e por quê:**

Não foram testados o fluxo de escrita no console das classes observadoras (SistemaAlertasPush e PainelCozinha) nem a execução do laço principal em main.py. Como essas classes apenas simulam saídas de I/O (Input/Output) via print, testá-las exigiria capturar a saída do sistema (stdout), o que adicionaria complexidade de infraestrutura de teste sem validar regras de negócio reais neste momento do protótipo.

**Revisão crítica:**
Todos os testes passam perfeitamente.
