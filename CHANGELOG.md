# Changelog

Tous les changements notables apportés à ce projet seront documentés dans ce fichier.

## [Unreleased]

## [1.2.0] - 2024-05-25

### Ajouté
- Implémentation de la fonctionnalité d'abonnement par email, y compris le formulaire, la vue et le modèle.
- Ajout du modèle de suivi des visiteurs et affichage du nombre de visiteurs sur la page d'accueil.
- Affichage du nombre d'utilisateurs inscrits sur la page d'accueil.
- Création d'une fonction utilitaire pour l'envoi d'emails en masse.
- Intégration de la gestion des campagnes d'emailing dans l'interface d'administration.

### Modifié
- Amélioration de la section d'abonnement avec un style et des couleurs améliorés.
- Ajout de la validation du formulaire pour vérifier les abonnés existants avant d'ajouter un nouvel abonné.

## [1.1.1] - 2024-05-24

### Corrigé
- Correction de l'envoi des emails de confirmation pour inclure le domaine correct et le protocole HTTPS.
- Ajustement de la configuration de `ACCOUNT_EMAIL_VERIFICATION` à "mandatory" pour obliger la vérification de l'email des utilisateurs.


## [1.1.0] - 2024-05-23

### Ajouté
- Personnalisation des templates de connexion, d'inscription, de réinitialisation de mot de passe, et de confirmation de réinitialisation de mot de passe.
- Ajout de la fonctionnalité de partage des événements sur les réseaux sociaux.
- Mise à jour du README.md avec les instructions de configuration d'email et de la base de données PostgreSQL.

### Modifié
- Modification de la gestion des rôles dans l'application user, en utilisant une classe Profile indépendante.
- Justification des textes dans la section "À Propos".
- Réorganisation de la section "Événements à Venir" pour une meilleure visibilité.
- Fixation de la barre de navigation pour qu'elle reste en place lors du défilement.

### Corrigé
- Correction des erreurs d'importation de `decouple`.
- Correction de la configuration des emails pour permettre l'envoi via SMTP.
- Affichage des erreurs d'authentification dans le formulaire de connexion.
- Amélioration de la vue d'inscription à un événement pour afficher un message lorsque l'utilisateur est déjà inscrit.
- Modification de la section d'appel à l'action pour ne s'afficher que si l'utilisateur n'est pas connecté.
- Correction des problèmes liés à la configuration de `ALLOWED_HOSTS` et `CSRF_TRUSTED_ORIGINS`.
- Résolution du problème d'affichage des images en production.


## [1.0.0] - 2024-05-21

### Ajouté
- Initialisation du projet Django Niger.
- Mise en place de la structure de base du projet.
- Ajout des fonctionnalités de forums de discussion, workshops et formations, projets collaboratifs, événements à venir, et témoignages.
- Mise en place des pages de connexion et d'inscription.

### Modifié
- Justification des textes dans la section "À Propos".
- Réorganisation de la section "Événements à Venir" pour une meilleure visibilité.

### Corrigé
- Correction des erreurs d'importation de `decouple`.


Ce changelog suit le format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).


