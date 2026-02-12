USE Musicablo;

INSERT INTO `musicablo`.`genero`
(`genero`,
`icone`,
`cor`)
VALUES
("Rock","","red"),
("Pop","","blue"),
("MPB","","#FACADA");

INSERT INTO `musicablo`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_capa`,
`nome_genero`)
VALUES
("System of a Down","04:15","B.Y.O.B","https://cdn-images.dzcdn.net/images/cover/4954f43cc6033ddfa0fa3ee5514a26ca/500x500.jpg","Rock"),
("System of a Down","02:34","Sugar","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWqOlJZxENcQgz8lMLSFPNXykipt0lrCLPPg&s","Rock");
