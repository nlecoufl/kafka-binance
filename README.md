# kafka-binance
*Fait par Nicolas MATUSIAK et Nicolas LECOUFLET*

**Repository pour le projet de NoSQL** : Application récupérant le prix de plusieurs crypto en utilisant l'API Binance, et affichant en temps réel si elles ont pris de la valeur ou non.


### Dépendences 
*Pré-requis : Git, Maven et MongoDB*

    pip install urllib kafka-python requests pymongo
    
#### Cloner le repo :
    git clone https://github.com/nlecoufl/kafka-binance

### Instructions
    
#### Lancer une instance Zookeeper :
    cd path/to/kafka
    bin/zookeeper-server-start.sh config/zookeeper.properties
      
#### Lancer le serveur :
    bin/kafka-server-start.sh config/server.properties
    
#### Création des topics : 
    ~/kafka-binance/scripts/createtopics.sh

Si `Permission non accordée` : 
    
    sudo chmod +x ~/kafka-binance/scripts/createtopics.sh
    ~/kafka-binance/scripts/createtopics.sh
    
#### Lancement du producer :
    python ~/kafka-binance/scripts/getbinance.py

#### Lancement du consumer : 
    python ~/kafka-binance/scripts/monitorbinance.py
*Infos : Affiche en temps réel si le cours d'une paire de crypto a baissé ou diminué*

#### Alimentation MongoDB :
    mongo
    python ~/kafka-binance/scripts/mongo.py

#### Lancement du Kstream :
    cd ~/kafka-binance/stream.examples
    mvn exec:java -Dexec.mainClass=myapps.Pipe
Ensuite on peut vérifier que le topic `streams-pipe-output` est bien alimenté (stream simple provenant de `streams-plaintext-input`).

    cd path/to/kafka
    bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic streams-pipe-output --from-beginning

    
