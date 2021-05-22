# Rain Forecast
### Deep Learning - 2020/2

## Integrantes

| Nome               | Matrícula  | GitHub             |
|--------------------|------------|--------------------|
|João Pedro de Aquino Corrêa Martins | 16/046602  |    @jpmartins201  |
|Arthur Borges Bringel Machado       | 16/0113032 |    @arthurbbm     |
| Mateus Oliveira Patrício | 16/0015006 | @omateusp |
| Thais Rebouças de Araújo | 18/0078224 | @thais-ra |

## O Projeto

O Rain Forecast é um software que busca realizar previsões de chuva, através de redes neurais, em várias cidades do Brasil. O projeto teve sua idealização sobre uma alternativa para os modelos complexos de previsão convencionais, sobretudo tornando mais simples com a utilização de redes neurais, buscando encontrar uma correlação entre os fatores observados para realizar as estimativas.

## Modo de uso

O arquivo [83377.csv](https://github.com/deeplearningunb/Rain-forecast/blob/main/83377-2.csv) é um conjunto de dados meteorológicos contendo as seguintes colunas com valores diários de cada variável desde 28/08/1963 para a estação 83377 do INMET, localizada em Brasília.

| Precipitacao | TempBulboSeco | TempBulboUmido | TempMaxima | TempMinima | UmidadeRelativa | PressaoAtmEstacao | PressaoAtmMar | DirecaoVento | VelocidadeVento | Insolacao | Nebulosidade | Evaporacao Piche | Temp Comp Media | Umidade Relativa Media | Velocidade do Vento Media |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |

Após lido o csv, um dataframe é criado com uma coluna nova que diz se choveu ou não naquele dia baseado numa precipitação inferior ou superior a 1 mm.

Quando rodado o algoritmo do [Jupyter Notebook](https://github.com/deeplearningunb/Rain-forecast/blob/main/rain_forecast_2.ipynb), novas colunas são adicionadas com o valor de cada variável em um, dois e três dias anteriores à data de referência da linha, então as linhas que possuem valores nulos são deletadas e as colunas que referemciam as variáveis em até três dias anteriores compõem a entrada da rede neural, enquanto a coluna que diz se chove ou não compõe a saída de treinamento.

## Desenvolvimento

Foi escolhida para o treinamento dos dados de entrada uma camada com a rede neural recorrente LSTM (Long Short-Term Memory). Para as camadas ocultas foi utilizada uma rede neural artificial comum para filtragem dos dados.

## Dataset

O dataset se encontra disponível neste [link](https://drive.google.com/drive/folders/1xyxumSFZanE45D1DrVHcmUD5lT-GmhNO?usp=sharing)

## References

- [Rain Forecasting with Artificial Neural Network](https://www.kaggle.com/fatmakursun/rain-forecasting-with-artificial-neural-network#EDA)

- [Using Machine Learning to Predict the Weather: Part 1](https://stackabuse.com/using-machine-learning-to-predict-the-weather-part-1/)
