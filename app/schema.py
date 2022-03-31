instructions = [
    'DROP TABLE IF EXISTS colonia;',
    'DROP TABLE IF EXISTS municipio;',
    'DROP TABLE IF EXISTS estado;'
]

instructions1 = [
    'CREATE TABLE estado(id_estado INT PRIMARY KEY AUTO_INCREMENT NOT NULL, estado TEXT NOT NULL);',
    """
    CREATE TABLE municipio (
        id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
        id_municipio INT NOT NULL,
        municipio TEXT NOT NULL,
        id_estado INT NOT NULL);
    """,
    """
    CREATE TABLE colonia (
        id_colonia INT PRIMARY KEY NOT NULL,
        cp int NOT NULL,
        asentamiento TEXT NOT NULL,
        tipo_asentamiento TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        id_municipio INT NOT NULL);
    """,
    'ALTER TABLE municipio ADD FOREIGN KEY(id_estado) REFERENCES estado(id_estado);',
    'ALTER TABLE colonia ADD FOREIGN KEY(id_municipio) REFERENCES municipio(id);'
]

instructions2 = [
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('1', 'Aguascalientes');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('2', 'Baja California');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('3', 'Baja California Sur');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('4', 'Campeche');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('5', 'Chiapas');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('6', 'Chihuahua');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('7', 'Ciudad de Mexico');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('8', 'Coahuila');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('9', 'Colima');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('10', 'Durango');",
    "INSERT INTO `sepomex`.`estado` (`id_estado`, `estado`) VALUES ('11', 'Estado de Mexico');",

    "INSERT INTO `sepomex`.`municipio` (`id`, `id_municipio`, `municipio`, `id_estado`) VALUES ('1', '003', 'Asientos', '1');",
    "INSERT INTO `sepomex`.`municipio` (`id`, `id_municipio`, `municipio`, `id_estado`) VALUES ('2', '003', 'Calvillo', '1');",
    "INSERT INTO `sepomex`.`municipio` (`id`, `id_municipio`, `municipio`, `id_estado`) VALUES ('3', '001', 'Ensenada', '2');",
    "INSERT INTO `sepomex`.`municipio` (`id`, `id_municipio`, `municipio`, `id_estado`) VALUES ('4', '002', 'Mexicali', '2');",
    "INSERT INTO `sepomex`.`municipio` (`id`, `id_municipio`, `municipio`, `id_estado`) VALUES ('5', '001', 'Calkini', '4');",
    "INSERT INTO `sepomex`.`municipio` (`id`, `id_municipio`, `municipio`, `id_estado`) VALUES ('6', '003', 'Carmen', '4');",

    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('1', '20742', 'El fenix', 'Rancheria', ' ', '1');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('2', '20744', 'San antonio', 'Ejido', ' ', '1');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('3', '20802', 'El mirador', 'Fraccionamiento', ' ', '2');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('4', '22753', 'Tierra santa', 'Rancho', ' ', '3');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('5', '22753', 'Parcela 32', 'Rancheria', ' ', '3');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('6', '21254', 'Real del sol', 'Fraccionamiento', 'Mexicali', '4');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('7', '21255', 'Antares Residencial	', 'Fraccionamiento', 'Mexicali', '4');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('8', '24902', 'San Isidro', 'Barrio', 'Calkini', '5');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('9', '24910', 'San Román', 'Colonia', 'Calkini', '5');",
    "INSERT INTO `sepomex`.`colonia` (`id_colonia`, `cp`, `asentamiento`, `tipo_asentamiento`, `ciudad`, `id_municipio`) VALUES ('10', '24110', 'Fátima', 'Colonia', 'Carmen', '6');"
]