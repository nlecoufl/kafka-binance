# kafka-binance
Repository pour le projet de NoSQL 
*Fait par Nicolas MATUSIAK et Nicolas LECOUFLET*

### Dépendences & Installations
    pip install urllib kafka-python requests pymongo
    
#### Cloner le repo :
    git clone https://github.com/nlecoufl/kafka-binance
    
#### Télécharger kafka :
    wget https://www-eu.apache.org/dist/kafka/2.2.1/kafka_2.12-2.2.1.tgz
    tar -xvf kafka_2.12-2.2.1.tgz
    export KAFKA_HOME=$(pwd)/kafka_2.12-2.2.1

### Instructions
####
    cd kafka-binance
    
#### Lancer MongoDB :
    mongo
    
#### Lancer une instance Zookeeper :
    cd 
    bin/zookeeper-server-start.sh config/zookeeper.properties
      
#### Lancer le serveur :
    bin/kafka-server-start.sh config/server.properties
    
#### Création des topics : 
    chmod +x scripts/createtopics.sh
    scripts/createtopics.sh
    
#### Lancement du producer :
    python getbinance.py

#### Lancement du consumer : 
    python monitorbinance.py
*Infos : Affiche en temps réel si le cours d'une paire de crypto a baissé ou diminué*

#### Lancement du stream :
