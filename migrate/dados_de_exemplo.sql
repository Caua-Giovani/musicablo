USE Musicablo;

INSERT INTO `musicablo`.`genero`
(`genero`,
`icone`,
`cor`)
VALUES
("Rock","","red"),
("Pop","","blue"),
("MPB","","#FACADA"),
("Indie","","#d058db");

INSERT INTO `musicablo`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_capa`,
`nome_genero`,
stats)
VALUES
("System of a Down","00:02:34","Sugar","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8hKmOIzwnrZkgNhEduMN_qCNUIhLi1g73yQ&s","Rock","ATIVO"),
("System of a Down","00:04:09","Radio/Video","https://cdn-images.dzcdn.net/images/cover/4954f43cc6033ddfa0fa3ee5514a26ca/500x500.jpg","Rock","ATIVO"),
("System of a Down","00:02:47","Lonely Day","https://upload.wikimedia.org/wikipedia/pt/5/50/220px-System_Of_A_Down-Hypnotize.jpg","Rock","ATIVO"),
("System of a Down","00:03:45","Psycho","https://upload.wikimedia.org/wikipedia/pt/1/18/220px-SystemofaDownToxicityalbumcover.jpg","Rock","ATIVO"),
("Chico Buarque","00:04:01","Cálice","https://upload.wikimedia.org/wikipedia/pt/5/59/Chico_buarque_1978.jpg","MPB","ATIVO"),
("Cássia Eller","00:04:11","O Segundo Sol","https://cdn-images.dzcdn.net/images/cover/9222d5c4c7e488199b0134531dc8328c/1900x1900-000000-80-0-0.jpg","Pop","ATIVO"),
("Arctic Monkeys","00:04:13","505","https://cdn-images.dzcdn.net/images/cover/d7a4f9f1af8736457de34f28d50ef496/1900x1900-000000-80-0-0.jpg","Indie","ATIVO");

