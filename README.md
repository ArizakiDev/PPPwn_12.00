# PS4 Firmware 12.00 Exploit (PPPwn)

Une exploitation semi-complète pour la PlayStation 4 sous firmware 12.00, utilisant des vulnérabilités du protocole PPPoE pour obtenir une exécution de code à distance et injecter GoldHEN.

## Vue d'ensemble

Le projet PPPwn est un framework d'exploitation qui cible plusieurs vulnérabilités critiques découvertes dans l'implémentation du protocole PPPoE sur PS4 12.00. L'objectif est de fournir une solution fiable et robuste pour l'installation de GoldHEN, permettant ainsi l'exécution de homebrews.

### Vulnérabilités ciblées

- Dépassement de tampon dans les fonctions `sppp_lcp_RCR` et `sppp_ipcp_RCR`
- Débordement de lecture dans le traitement des paquets PPPoE
- Débordement arithmétique dans `sppp_pap_input`
- Conditions de concurrence potentielles dans la gestion des sessions PPPoE

## État du développement

### Fonctionnalités implémentées
- Détection automatique de la PS4 sur le réseau local
- Génération de payloads adaptés au firmware 12.00
- Interface en ligne de commande pour le contrôle de l'exploitation
- Mécanisme de base pour l'injection de GoldHEN

### En cours de développement
- Amélioration de la stabilité de l'exploitation
- Support des différents modèles de PS4
- Interface graphique utilisateur
- Documentation détaillée du processus d'exploitation

## Guide d'installation

### Prérequis
- Python 3.8 ou supérieur
- Bibliothèque Scapy 2.4+
- Connexion réseau directe à la PS4 cible
- Privilèges administrateur sur la machine hôte

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/ArizakiDev/PPPwn_12.00.git
cd ps4-pppwn

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ou
.\venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

1. Connectez votre PS4 au même réseau que votre machine
2. Désactivez temporairement le pare-feu sur la machine hôte
3. Exécutez l'exploit :

```bash
sudo python main.py --target-ip <PS4_IP> --mode auto
```

### Options disponibles

- `--target-ip` : Adresse IP de la PS4 cible
- `--mode` : Mode d'exploitation (auto/manual)
- `--payload` : Chemin vers un payload personnalisé
- `--debug` : Active les logs détaillés

## Contribution

Nous encourageons activement les contributions de la communauté. Voici les domaines prioritaires :

### Axes de recherche
- Optimisation de la fiabilité de l'exploitation
- Développement de nouveaux payloads
- Amélioration de la compatibilité entre modèles
- Documentation et tutoriels

### Processus de contribution

1. Fork du dépôt
2. Création d'une branche dédiée
3. Développement et tests
4. Soumission d'une Pull Request documentée

### Bonnes pratiques
- Suivre les conventions de code Python (PEP 8)
- Documenter exhaustivement les modifications
- Inclure des tests unitaires
- Maintenir la compatibilité avec les versions précédentes

## Avertissement

Ce projet est fourni à des fins de recherche uniquement. Les utilisateurs sont seuls responsables de son utilisation dans le respect des lois en vigueur. Merci à TheFlow pour ses recherches
