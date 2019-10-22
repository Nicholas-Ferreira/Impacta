/*
RA 1900953 - Nicholas Ferreira
RA 1900519 - Fernando Franco
RA 1901118 - Lara A. Argento
RA 1900953 - Lucas Eduardo Ano
RA 1901008 - Leonardo Ferreira
*/

/*
Para fins de marketing é necessário um relatório contendo os cursos disponíveis.
Devem ser devolvidos os seguintes dados:
Nome do curso, tipo do curso, duração do curso, informações (coluna sobre), período,
horário e valor.
Obs.: Caso um curso tenha mais de um período, devolva uma linha para cada período.
*/
SELECT 
	nome as 'Nome do curso', 
	tipo as 'Tipo do curso', 
	duracao as 'Duração do curso',
	sobre as 'Informações', 
	periodo as 'Período',
	horario as 'Horário',
	valor as 'Valor' 
FROM 
	Periodo AS periodo
INNER JOIN 
	Curso AS curso ON periodo.id_curso = curso.id

/*
Para emissão de novas carteirinhas dos alunos do curso de SI (sigla do curso) devolva
as seguintes informações dos alunos desse curso:
Nome, registro, foto, ano, semestre da turma e letra da turma.
*/
SELECT
	usuario.nome as 'Nome', 
	registro as 'Registro', 
	foto as 'Foto',
	ano as 'Ano', 
	semestre as 'Semestre da turma',
	letra as 'Letra da turma'
FROM
	Turma AS turma
INNER JOIN 
	Curso AS curso ON turma.id_curso = curso.id
INNER JOIN 
	Aluno AS aluno ON turma.id = aluno.id_turma
INNER JOIN 
	Usuario AS usuario ON aluno.id_usuario = usuario.id
WHERE
	curso.sigla = 'SI'


/*
Faça uma consulta que gere a lista de chamada da turma SI 2B de 2019 da disciplina de
linguagem SQL. Serão devolvidos somente os registros e nomes dos alunos.
*/
SELECT 
	registro as 'Registro', 
	usuario.nome as 'Nome'
FROM 
	Turma AS turma
INNER JOIN 
	Curso AS curso ON turma.id_curso = curso.id
INNER JOIN 
	Aluno AS aluno ON turma.id = aluno.id_turma
INNER JOIN 
	Usuario AS usuario ON aluno.id_usuario = usuario.id
WHERE
	curso.sigla = 'SI' AND turma.semestre = 2 AND turma.letra = 'B' AND turma.ano = 19

/*
Para que os alunos possam solicitar matrícula, é preciso uma lista contendo o nome da
disciplina de todas as disciplinas oferecidas no 2º semestre de 2019 para o curso de
Sistemas de informação.
*/
SELECT
	disciplina.nome AS 'Nome'
FROM
	Disciplina AS disciplina
INNER JOIN
	DisciplinaOfertada AS discofertada ON disciplina.id = discofertada.id_disciplina
INNER JOIN
	Turma AS turma ON discofertada.id_turma = turma.id
INNER JOIN
	Curso AS curso ON turma.id_curso = curso.id
WHERE
	discofertada.semestre = 2 AND discofertada.ano = 19 AND curso.sigla = 'SI'

/*
Para que alunos e professores possam se comunicar, será criado um grupo de e-mails
relacionando alunos e professores de um curso. Faça uma consulta que devolva, para
cada linha:
Nomes e emails (do professor e do aluno).
Obs.: Somente linhas que o professor ministra disciplinas que o aluno está matriculado
(solicitações aceitas).
*/
SELECT
	usuprofessor.nome AS 'Nome Professor',
	usuprofessor.email AS 'E-mail Professor',
	usualuno.email AS 'Nome Aluno',
	usualuno.email AS 'E-mail Aluno'
FROM
	DisciplinaOfertada AS discofertada
INNER JOIN 
	Professor AS professor ON discofertada.id_professor = professor.id
INNER JOIN
	SolicitacaoMatricula AS solicmatricula ON solicmatricula.id_disciplina = discofertada.id
INNER JOIN 
	Aluno AS aluno ON solicmatricula.id_aluno = aluno.id
INNER JOIN 
	Usuario AS usualuno ON aluno.id_usuario = usualuno.id
INNER JOIN 
	Usuario AS usuprofessor ON professor.id_usuario = usuprofessor.id