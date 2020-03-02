use AC09

/* Script de criação do banco de dados do LMS */
begin tran
	CREATE TABLE Usuario (
		id INT,
		registro INT NOT NULL,
		nome VARCHAR(120) NOT NULL,
		email VARCHAR(60) NOT NULL,
		celular CHAR(16) NOT NULL, --(11) 91234-1234
		login VARCHAR(20) NOT NULL,
		senha VARCHAR(255) NOT NULL,
		data_expiracao DATE NOT NULL CONSTRAINT dfUsuarioDataExpiracao DEFAULT '1900-01-01' --Regra 2 ,
		CONSTRAINT pkUsuario PRIMARY KEY (id), --PK
		CONSTRAINT uqUsuarioRegistro UNIQUE (registro), --UQ1
		CONSTRAINT uqUsuarioEmail UNIQUE (email), --UQ2
		CONSTRAINT uqUsuarioLogin UNIQUE (login) --UQ3
	);
	
	CREATE TABLE Coordenador (
		id INT NOT NULL,
		id_usuario INT NOT NULL,
		CONSTRAINT pkCoordenador PRIMARY KEY (id),
		CONSTRAINT fkCoordenadorUsuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id), --FK1
		CONSTRAINT uqCoordenadorUsuario UNIQUE (id_usuario) -- Faltava no diagrama
	);
	
	CREATE TABLE Professor (
		id INT NOT NULL,
		id_usuario INT NOT NULL,
		apelido VARCHAR(40),
		CONSTRAINT pkProfessor PRIMARY KEY (id), --PK
		CONSTRAINT fkProfessorUsuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id), --FK1
		CONSTRAINT uqProfessorUsuario UNIQUE (id_usuario) -- Faltava no diagrama
	);
	
	CREATE TABLE Curso (
		id INT NOT NULL,
		nome VARCHAR(60) NOT NULL,
		sigla VARCHAR(10) NOT NULL,
		tipo VARCHAR(20) NOT NULL,
		duracao TINYINT NOT NULL,
		sobre TEXT NOT NULL,
		id_coordenador INT,
		CONSTRAINT pkCurso PRIMARY KEY (id),  --PK
		CONSTRAINT uqCursoNome UNIQUE (nome), --UQ1
		CONSTRAINT uqCursoSigla UNIQUE(sigla),--UQ2
		CONSTRAINT fkCursoCoordenador FOREIGN KEY (id_coordenador) REFERENCES Coordenador(id) --FK1
	);
	
	CREATE TABLE Periodo (
		id INT NOT NULL,
		id_curso INT NOT NULL,
		periodo VARCHAR(15) NOT NULL,
		horario CHAR(13) NOT NULL, --19:00 - 22:00
		valor NUMERIC(7,2) NOT NULL,
		CONSTRAINT pkPeriodo PRIMARY KEY (id), --PK
		CONSTRAINT fkPeriodoCurso FOREIGN KEY (id_curso) REFERENCES Curso(id), --FK1
		CONSTRAINT uqPeriodo UNIQUE (id_curso, periodo), --UQ1
		CONSTRAINT ckPeriodoPeriodo CHECK (periodo IN ('matutino', 'vespertino', 'integral', 'noturno')) --Regra 5
	);
	
	CREATE TABLE Turma (
		id INT NOT NULL,
		id_curso INT NOT NULL,
		ano TINYINT NOT NULL, --Adicionado!
		semestre TINYINT NOT NULL,
		letra CHAR(1) NOT NULL,
		periodo VARCHAR(15) NOT NULL,
		CONSTRAINT pkTurma PRIMARY KEY (id), --PK
		CONSTRAINT fkTurmaCurso FOREIGN KEY (id_curso) REFERENCES Curso(id), --FK1
		CONSTRAINT uqTurma UNIQUE (id_curso, ano, semestre, letra), --UQ1
		CONSTRAINT ckTurmaSemestre CHECK (semestre IN (1,2)), --Regra 6
		CONSTRAINT ckTurmaLetra CHECK (letra LIKE '[A-Z]'), --Regra 7
		CONSTRAINT ckTurmaPeriodo CHECK (periodo IN ('matutino', 'vespertino', 'integral', 'noturno')) --Regra 8
	);
	
	CREATE TABLE Aluno (
		id INT NOT NULL,
		id_usuario INT NOT NULL,
		foto VARCHAR(255), --Regra 1
		id_turma INT NOT NULL,
		CONSTRAINT pkAluno PRIMARY KEY (id), --PK
		CONSTRAINT fkAlunoUsuario FOREIGN KEY (id_usuario) REFERENCES Usuario(id), --FK1
		CONSTRAINT fkAlunoTurma FOREIGN KEY (id_turma) REFERENCES Turma(id), --FK2
		CONSTRAINT uqAlunoUsuario UNIQUE (id_usuario) -- Faltava no diagrama
	);
	
	CREATE TABLE Disciplina (
		id INT NOT NULL,
		nome VARCHAR(100) NOT NULL,
		slug VARCHAR(100) NOT NULL,
		plano_ensino TEXT NOT NULL,
		carga_horaria TINYINT NOT NULL,
		competencias TEXT NOT NULL,
		habilidades TEXT NOT NULL,
		conteudo_programatico TEXT NOT NULL,
		bibliografia_basica TEXT NOT NULL,
		bibliografia_complementar TEXT NOT NULL,
		percentual_pratico TINYINT NOT NULL,
		percentual_teorico TINYINT NOT NULL,
		id_professor_responsavel INT,
		CONSTRAINT pkDisciplina PRIMARY KEY (id), --PK
		CONSTRAINT uqDisciplinaNome UNIQUE (nome), --UQ1
		CONSTRAINT uqDisciplinaSlug UNIQUE (slug), --UQ2
		CONSTRAINT fkDisciplinaResponsavel FOREIGN KEY (id_professor_responsavel) REFERENCES Professor(id), --FK1
		CONSTRAINT ckDisciplinaCargaHoraria CHECK (carga_horaria IN (40, 80)), --Regra 3
		CONSTRAINT ckDisciplinaPercentualPratico CHECK (percentual_pratico BETWEEN 0 AND 100), --Regra 4 (1)
		CONSTRAINT ckDisciplinaPercentualTeorico CHECK (percentual_teorico BETWEEN 0 AND 100), --Regra 4 (2)
		CONSTRAINT ckDisciplinaSomaPercentuais CHECK (percentual_pratico + percentual_teorico = 100) --Regra 4 (3)
	);
	
	CREATE TABLE DisciplinaOfertada (
		id INT NOT NULL,
		id_turma INT NOT NULL,
		id_disciplina INT NOT NULL,
		ano SMALLINT NOT NULL,
		semestre TINYINT NOT NULL,
		id_professor INT,
		metodologia TEXT NOT NULL,
		recursos TEXT NOT NULL,
		criterio_avaliacao TEXT NOT NULL, 
		CONSTRAINT pkDisciplinaOfertada PRIMARY KEY (id), --PK
		CONSTRAINT uqDisciplinaOfertadaTurma UNIQUE (id_turma, id_disciplina, ano, semestre), --UQ1
		CONSTRAINT fkDisciplinaOfertadaTurma FOREIGN KEY (id_turma) REFERENCES Turma(id), --FK1
		CONSTRAINT fkDisciplinaOfertadaDisciplina FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id), --FK2
		CONSTRAINT fkDisciplinaOfertadaProfessor FOREIGN KEY (id_professor) REFERENCES Professor(id), --FK3
		CONSTRAINT ckDisciplinaOfertadaSemestre CHECK (semestre IN (1,2)), --Regra 9
		CONSTRAINT ckDisciplinaOfertadaAno CHECK (ano BETWEEN 1900 AND 2100) --Regra 10
	);
	
	CREATE TABLE SolicitacaoMatricula (
		id INT NOT NULL,
		id_aluno INT NOT NULL,
		id_disciplina INT NOT NULL,
		numero INT NOT NULL IDENTITY (1,1), --Regra 11
		data DATE NOT NULL CONSTRAINT dfSolicitacaoMatricula DEFAULT getdate(), --Regra 12
		id_coordenador INT,
		data_aprovacao DATE,
		CONSTRAINT pkSolicitacaoMatricula PRIMARY KEY (id), --PK
		CONSTRAINT fkSolicitacaoMatriculaAluno FOREIGN KEY (id_aluno) REFERENCES Aluno(id), --FK1
		CONSTRAINT fkSolicitacaoMatriculaDisciplina FOREIGN KEY (id_disciplina) REFERENCES DisciplinaOfertada(id), --FK2
		CONSTRAINT fkSolicitacaoMatriculaCoordenador FOREIGN KEY (id_coordenador) REFERENCES Coordenador(id), --FK3
		CONSTRAINT uqSolicitacaoMatriculaAluno UNIQUE (id_aluno, id_disciplina), --UQ1
		CONSTRAINT uqSolicitacaoMatriculaNumero UNIQUE (numero) --UQ2
	);
commit