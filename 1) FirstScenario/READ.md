# Cenário 1

## Descrição

Arquivo producer.py é responsável por enviar para o tópico "numptest" a cada 5 segundos. Para a construção dessas mensagens, utiliza a classe Transaction do arquivo producedata.py, que simula uma transação de compra de um e-comerce. Por fim, o arquivo consumer.py é responsável por receber as mensagens do Kafka e armazenar em um banco de dados MongoDB.


## Pré-Requisitos

* Python - Download & Install Python, version > 3
* MongoDB - Download & Install MongoDB, and make sure it's running on the default port (27017).
* Kafka - Download & Install Kafka, and make sure that listeners are on port 9092.

## Utilização

Abrir terminal e iniciar Zookeeper

```bash
  zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
```

Abrir um segundo terminal e iniciar Kafka
```bash
  kafka-server-start /usr/local/etc/kafka/server.properties
```

Iniciar Banco de Dados MongoDB em um terceiro terminal
```bash
  kafka-server-start /usr/local/etc/kafka/server.properties
```

Subir tópico "numtest" no Kafka 

```bash
  kafka-topics --bootstrap-server localhost:9092 --create --topic numtest --partitions 1 --replication-factor 1
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
  python3 consumer.py
```

Verificar que arquivos estão sendo escritos no banco MongoDB. Nesse caso, utilizei o próprio MongoDB Compass para realizar a leitura das mensagens recebidas.