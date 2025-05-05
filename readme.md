# Análise de Dados de Lutas do UFC

Este repositório contém uma análise exploratória de um conjunto de dados de lutas do Ultimate Fighting Championship (UFC). O objetivo desta análise é entender melhor os padrões e tendências nas lutas do UFC ao longo do tempo, incluindo a distribuição dos métodos de vitória, a ocorrência de finalizações por round e a evolução dos tipos de vitória ao longo dos anos.

## Conteúdo

* **`data/`**: Contém o arquivo de dados principal `ufc-master.csv`.
* **`images/`**: Contém as visualizações geradas durante a análise
* **`requirements.txt`**: Lista das bibliotecas Python necessárias para executar o código.

## Análise Realizada

A análise exploratória abordou os seguintes aspectos:

* **Distribuição Geral dos Métodos de Vitória:** Uma visão geral de como as lutas terminam (Nocaute, Finalização, Decisão, etc.).
* **Comparação entre Nocautes e Finalizações:** Uma comparação direta do número de lutas que terminaram por KO/TKO versus Submissão.
* **Vitórias por Método de Vitória em Cada Categoria de Peso:** Análise de como os diferentes métodos de vitória se distribuem entre as diversas categorias de peso do UFC.
* **Métodos de Vitória por Ano:** A evolução dos diferentes métodos de vitória ao longo dos anos.
* **Distribuição dos Rounds de KO/TKO e Submissão:** Em quais rounds as lutas que terminam por nocaute ou finalização tendem a ocorrer.
* **Tendência de Tipos de Vitória ao Longo dos Anos:** A tendência de longo prazo dos principais métodos de vitória (KO/TKO, Submissão, Decisão).

## Visualizações

As seguintes visualizações foram geradas durante a análise e estão disponíveis no diretório `images/`:

* `metodos_vitoria.png`: Gráfico de barras mostrando a distribuição geral dos métodos de vitória.
* `vitorias_por_peso.png`: Gráfico de barras mostrando as vitórias por método em cada categoria de peso.
* `comparacao_nocautes_finalizacoes.png`: Gráfico de barras comparando o número de nocautes e finalizações.
* `metodos_por_ano.png`: Gráfico de barras empilhadas mostrando os métodos de vitória por ano.
* `rounds_ko_sub.png`: Gráfico de barras mostrando a distribuição de nocautes e finalizações por round.
* `tendencia_metodos_ano.png`: Gráfico de linhas mostrando a tendência dos tipos de vitória ao longo dos anos.

## Fonte dos Dados
Os dados utilizados nesta análise foram obtidos do [Ultimate UFC Dataset disponível na](https://www.kaggle.com/datasets/mdabbert/ultimate-ufc-dataset) [Kaggle](https://www.kaggle.com/) O conjunto reúne informações detalhadas de diversas lutas realizadas na história do UFC.
