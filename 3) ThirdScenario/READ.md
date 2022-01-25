# Cenário 3

## Descrição

Arquivo producer.py é responsável por enviar para o tópico "numptest" a cada 5 segundos. Para a construção dessas mensagens, utiliza a classe Transaction do arquivo producedata.py, que simula uma transação de compra de um e-comerce. Por fim, o arquivo consumer.py é responsável por receber as mensagens do Kafka, construir dataframe spark e salvar dados em um arquivo parquet. Apache Kafka está dentro de um container Docker.


## Pré-Requisitos

* Python - Download & Install Python, version => 3.6
* Kafka - Download & Install Kafka, and make sure that listeners are on port 9092
* Spark - Download & Install Spark, version => 3.2
* Java - Download & Install Java, version == 1.8

## Utilização

Iniciar container Kafka utilizando comando docker-compose:

```bash
  cd docker 
  docker-compose up -d
```

Verificar criação de Zookeper e Kafka
```bash
  nc -zv localhost 29092
  nc -zv localhost 22181
```

Subir tópico "numtest" no Kafka 

```bash
  kafka-topics --bootstrap-server localhost:29092 --create --topic numtest --partitions 1 --replication-factor 1
```

Verificar os testes unitários

```bash
  pytest
```
Iniciar Script de producer de mensagens

```bash
  python3 producer.py
```

Iniciar Script de consumer de mensagens

```bash
  spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0 consumer.py
```

Verificar que arquivos estão sendo escritos no banco Parquet. Nesse caso, abrir Spark e ler arquivo Parquet.

```bash
  pyspark
  spark.read.parquet("outcome").show()
```