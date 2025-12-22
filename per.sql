DROP DATABASE personagens_bd;
CREATE DATABASE IF NOT EXISTS personagens_bd;
USE personagens_bd;

CREATE TABLE usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    login VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE personagens (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    classe VARCHAR(100) NOT NULL,
    raca VARCHAR(100) NOT NULL,
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
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);
