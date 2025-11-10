# 🤖 BotInterface

Une interface web moderne et intuitive pour interagir avec des systèmes de chatbot, développée avec Flask.

## 📋 Table des matières

- [🤖 BotInterface](#-botinterface)
  - [📋 Table des matières](#-table-des-matières)
  - [🎯 À propos](#-à-propos)
  - [✨ Fonctionnalités](#-fonctionnalités)
  - [🏗️ Architecture](#️-architecture)
  - [📦 Prérequis](#-prérequis)
  - [🚀 Installation](#-installation)
    - [1. Cloner le repository](#1-cloner-le-repository)
    - [2. Créer un environnement virtuel](#2-créer-un-environnement-virtuel)
    - [3. Installer les dépendances](#3-installer-les-dépendances)
  - [⚙️ Configuration](#️-configuration)
    - [Variables d'environnement](#variables-denvironnement)
    - [Configuration Flask](#configuration-flask)
  - [🎮 Utilisation](#-utilisation)
    - [Démarrer l'application](#démarrer-lapplication)
    - [Endpoints disponibles](#endpoints-disponibles)
  - [📁 Structure du projet](#-structure-du-projet)
  - [📚 Documentation](#-documentation)
  - [🛠️ Technologies utilisées](#️-technologies-utilisées)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [Outils](#outils)
  - [🤝 Contribution](#-contribution)
    - [Standards de code](#standards-de-code)
  - [📝 Roadmap](#-roadmap)
  - [🐛 Bugs connus](#-bugs-connus)
  - [📄 Licence](#-licence)
  - [👤 Auteur](#-auteur)
  - [📞 Contact](#-contact)

## 🎯 À propos

BotInterface est une application web qui fournit une interface utilisateur conviviale pour communiquer avec des bots intelligents. Le projet vise à simplifier l'interaction entre les utilisateurs et les systèmes de chatbot en offrant une expérience utilisateur optimale.

## ✨ Fonctionnalités

- 💬 **Interface de chat intuitive** - Interface utilisateur moderne et responsive
- 🔄 **Communication en temps réel** - Échanges instantanés avec le bot
- 🎨 **Design personnalisable** - Interface adaptable et esthétique
- 📱 **Responsive Design** - Compatible avec tous les appareils (desktop, tablette, mobile)
- 🔌 **API REST** - Backend Flask robuste et extensible
- 📊 **Gestion des sessions** - Maintien du contexte des conversations
- 🛡️ **Sécurité** - Protection des données et des échanges

## 🏗️ Architecture

Le projet suit une architecture MVC (Model-View-Controller) avec Flask :

```
Frontend (HTML/CSS/JS) ↔ Flask Backend ↔ Bot API
```

Pour plus de détails, consultez le [diagramme d'architecture](docs/diagram/system_architecture.mmd).

## 📦 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.8+** - [Télécharger Python](https://www.python.org/downloads/)
- **pip** - Gestionnaire de paquets Python (inclus avec Python)
- **Git** - Pour cloner le repository

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/josepha237/BotInterface.git
cd BotInterface
```

### 2. Créer un environnement virtuel

**Windows (PowerShell) :**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**Linux/Mac :**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du projet :

```env
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=votre_clé_secrète_ici
BOT_API_URL=http://localhost:5001/api
```

### Configuration Flask

Ajustez les paramètres dans `app.py` selon vos besoins :

```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
app.config['BOT_API_URL'] = os.environ.get('BOT_API_URL')
```

## 🎮 Utilisation

### Démarrer l'application

```bash
python app.py
```

L'application sera accessible à l'adresse : `http://localhost:5000`

### Endpoints disponibles

- `GET /` - Page d'accueil de l'interface
- `POST /api/chat` - Envoyer un message au bot
- `GET /api/history` - Récupérer l'historique des conversations

## 📁 Structure du projet

```
BotInterface/
│
├── app.py                      # Point d'entrée de l'application Flask
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation du projet
├── .gitignore                  # Fichiers à ignorer par Git
│
├── docs/                       # Documentation
│   ├── srs.pdf                # Cahier des charges (SRS)
│   ├── diagram/               # Diagrammes
│   │   └── system_architecture.mmd  # Architecture système
│   └── ui-mockups/            # Maquettes d'interface
│
├── static/                     # Ressources statiques
│   ├── css/
│   │   └── styles.css         # Styles CSS
│   ├── js/
│   │   └── index.js           # JavaScript frontend
│   └── img/                   # Images et assets
│
└── templates/                  # Templates HTML
    └── index.html             # Page principale
```

## 📚 Documentation

- **[Cahier des charges](docs/srs.pdf)** - Spécifications détaillées du projet
- **[Architecture système](docs/diagram/system_architecture.mmd)** - Diagramme de l'architecture
- **[Maquettes UI](docs/ui-mockups/)** - Designs et wireframes de l'interface

## 🛠️ Technologies utilisées

### Backend
- **[Flask 3.0.3](https://flask.palletsprojects.com/)** - Framework web Python
- **[Requests 2.31.0](https://requests.readthedocs.io/)** - Bibliothèque HTTP

### Frontend
- **HTML5** - Structure de la page
- **CSS3** - Stylisation
- **JavaScript (Vanilla)** - Interactivité

### Outils
- **Git** - Contrôle de version
- **Python Virtual Environment** - Isolation des dépendances

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Committez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une **Pull Request**

### Standards de code

- Suivre les conventions PEP 8 pour Python
- Commenter le code de manière claire et concise
- Tester les fonctionnalités avant de soumettre

## 📝 Roadmap

- [ ] Implémentation du backend Flask complet
- [ ] Développement de l'interface utilisateur
- [ ] Intégration avec l'API du bot
- [ ] Support bilingue (français/anglais)
- [ ] Mode sombre
- [ ] Tests unitaires et d'intégration (pytest)
- [ ] Déploiement en production

## 🐛 Bugs connus

Aucun bug connu pour le moment. Si vous en trouvez, veuillez [ouvrir une issue](https://github.com/josepha237/BotInterface/issues).

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

**Joseph A.**
- GitHub: [@josepha237](https://github.com/josepha237)

## 📞 Contact

Pour toute question ou suggestion, n'hésitez pas à :
- Ouvrir une issue sur GitHub
- Contacter l'équipe de développement

---

⭐ **N'oubliez pas de mettre une étoile au projet si vous le trouvez utile !**

*Dernière mise à jour : Novembre 2025*
