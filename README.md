# kafka-python-practise

Com objetivo de praticar a utilização do serviço de mensageira Apache Kafka, esse projeto foi criado com intenção de simular diferentes cenários de utilização da ferramenta. 

A premissa geral é a existência de um e-comerce que está com as vendas a todo vapor, recebendo vários usuários interessados em comprar os produtos ofertados.
Nesse sentido, os dados gerados e enviados para o tópico do kafka visam simular a venda de produtos dentro do e-comerce, contendo informações como quantidade, comprador, número do produto, etc.

A ideia é começar com cenários mais simples e evoluir a complexidade conforme os exemplos forem sendo criados.

# Scenarios

I - Receber os dados com Script Python simples e armazena-los dentro do MongoDB

![Kafka Project1](https://user-images.githubusercontent.com/58954954/149647926-aada08ab-f921-4fc9-a6d8-b65debe8729e.png)

II - Receber os dados com o SparkStreaming e salva-los dentro de um arquivo parquet

![Kafka Project2](https://user-images.githubusercontent.com/58954954/149647900-fab30ff9-93ec-4302-9263-b1ec638ab858.png)

III - Receber os dados com o SparkStreaming e salva-los dentro de um arquivo parquet. Kafka dentro rodando dentro de uma container docker

![Kafka Project3](https://user-images.githubusercontent.com/58954954/150894530-5a01787c-e061-4ed5-bde5-23ebdd875663.png)

IV - Receber e agrupar os dados com o SparkStreaming e reenvia-los para o Kafka

![Kafka Project4](https://user-images.githubusercontent.com/58954954/150893978-a09184f5-39bf-4a08-b3b7-8864f0fee1fe.png)

V - Receber e agrupar os dados com o SparkStreaming, enriquece-los com uma base relacional e reenvia-los para o Kafka

![Kafka Project5](https://user-images.githubusercontent.com/58954954/150893989-9039d287-ea48-4ff9-ad56-027d804edaf6.png)
