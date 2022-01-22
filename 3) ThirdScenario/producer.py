from time import sleep
from json import dumps
from kafka import KafkaProducer

from producedata import Transaction

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(1000):
    Transaction(e).get_info()
    data = Transaction(e).get_info()
    producer.send('numtest', value=data)
    sleep(1)
    print(data)
