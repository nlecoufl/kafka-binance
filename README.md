# kafka-binance
Repository pour le projet de NoSQL 
*Fait par Nicolas MATUSIAK et Nicolas LECOUFLET*

### Dépendences 
*Pré-requis : Git, Maven et MongoDB*

    pip install urllib kafka-python requests pymongo
    
#### Cloner le repo :
    git clone https://github.com/nlecoufl/kafka-binance

### Instructions

#### Lancer MongoDB :
    mongo
    
#### Lancer une instance Zookeeper :
    cd path/to/kafka
    bin/zookeeper-server-start.sh config/zookeeper.properties
      
#### Lancer le serveur :
    bin/kafka-server-start.sh config/server.properties
    
#### Création des topics : 
    ~/kafka-binance/scripts/createtopics.sh

Si accès refusé : 
    
    sudo chmod +x ~/kafka-binance/scripts/createtopics.sh
    
#### Lancement du producer :
    python ~/kafka-binance/scripts/getbinance.py

#### Lancement du consumer : 
    python ~/kafka-binance/scripts/monitorbinance.py
*Infos : Affiche en temps réel si le cours d'une paire de crypto a baissé ou diminué*

#### Lancement du stream :
    
