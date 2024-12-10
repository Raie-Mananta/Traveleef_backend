-- Création du schéma voyage
DROP SCHEMA IF EXISTS voyage CASCADE;
CREATE SCHEMA voyage;
SET search_path to voyage,public;

 

-- Création de la table utilisateur
CREATE TABLE utilisateur (
    idUtilisateur SERIAL,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    CONSTRAINT pk_utilisateur PRIMARY KEY (idUtilisateur)
);

 

-- Création de la table voyage
CREATE TABLE voyage (
    idVoyage SERIAL,
    depart VARCHAR(100) NOT NULL,
    arrivee VARCHAR(100) NOT NULL,
    date_depart DATE NOT NULL,
    date_retour DATE NOT NULL,
    prix NUMERIC NOT NULL,
    CONSTRAINT pk_voyage PRIMARY KEY (idVoyage)
);

 

-- Création de la table transport
CREATE TABLE transport (
    idTransport SERIAL,
    type_transport VARCHAR(50) NOT NULL,
    capacite INT NOT NULL,
    marque VARCHAR(50),
    CONSTRAINT pk_transport PRIMARY KEY (idTransport)
);

 

-- Création de la table passager
CREATE TABLE passager (
    idPassager SERIAL,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    CONSTRAINT pk_passager PRIMARY KEY (idPassager)
);

 

-- Création de la table reservation
CREATE TABLE reservation (
    idReservation SERIAL,
    idUtilisateur INT NOT NULL,
    idVoyage INT NOT NULL,
    idTransport INT NOT NULL,
    CONSTRAINT pk_reservation PRIMARY KEY (idReservation),
    CONSTRAINT fk_reservation_utilisateur FOREIGN KEY (idUtilisateur) REFERENCES utilisateur (idUtilisateur),
    CONSTRAINT fk_reservation_voyage FOREIGN KEY (idVoyage) REFERENCES voyage (idVoyage),
    CONSTRAINT fk_reservation_transport FOREIGN KEY (idTransport) REFERENCES transport (idTransport)
);

 

-- Création de la table passager_reservation pour lier les passagers aux réservations
CREATE TABLE passager_reservation (
    idPassager INT NOT NULL,
    idReservation INT NOT NULL,
    CONSTRAINT pk_passager_reservation PRIMARY KEY (idPassager, idReservation),
    CONSTRAINT fk_passager_reservation_passager FOREIGN KEY (idPassager) REFERENCES passager (idPassager),
    CONSTRAINT fk_passager_reservation_reservation FOREIGN KEY (idReservation) REFERENCES reservation (idReservation)
);
