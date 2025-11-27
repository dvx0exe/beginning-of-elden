CREATE DATABASE personagens_bd;
USE personagens_bd;


CREATE TABLE personagens (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    classe VARCHAR(100) NOT NULL,
    raca VARCHAR(100) NOT NULL,
    sexo VARCHAR(50) NOT NULL,
    vigor INT NOT NULL,
    mente INT NOT NULL,
    fortitude INT NOT NULL,
    forca INT NOT NULL,
    destreza INT NOT NULL,
    inteligencia INT NOT NULL,
    fe INT NOT NULL,
    arcano INT NOT NULL,
    build_escolhida VARCHAR(255),
    equipamento TEXT,
    roupas TEXT,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);