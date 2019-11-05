/* Arquivo de referência para modelagem das classes da AC09. */

create table Usuario
(
	idUsuario smallint identity(1,1)
	, idLogin varchar(30) unique not null
	, Senha varchar(30)
	, DtExpiracao date constraint defExpiracao default ('19000101') 
	, constraint pkUsuario primary key (idUsuario)
)

create table Coordenador
 (
     idCoordenador smallint not null identity(1,1)
    , idUsuario smallint not null
    , Nome varchar(30) not null
    , Email varchar(50) not null
    , Celular varchar(14) not null
    , constraint pkCoordenador primary key (idCoordenador)
    , constraint fkUsuarioCoordenador foreign key (idUsuario) references Usuario 
    , constraint uqEmailCoordenador unique (Email)
    , constraint uqCelularCoordenador unique (Celular)
)

create table Aluno
(
	 idAluno smallint not null identity(1,1)
    , idUsuario smallint not null
    , Nome varchar(100) not null
    , Email varchar(50) not null
    , Celular varchar(14) not null
	, RA smallint not null
    , constraint pkAluno primary key (idAluno)
    , constraint fkUsuarioAluno foreign key (idUsuario) references Usuario
    , constraint uqEmailAluno unique (Email)
    , constraint uqCelularAluno unique (Celular)
)

create table Professor
(
	idProfessor smallint not null identity(1,1)
	, idUsuario smallint not null
    , Email varchar(50) not null
	, Celular varchar(14) not null
	, Apelido varchar(15) not null
	, constraint pkProfessor primary key (idProfessor)
	, constraint fkUsuarioProfessor foreign key(idUsuario) references Usuario
	, constraint uqEmailProfessor unique (Email)
    , constraint uqCelularProfessor unique (Celular)
)

create table Disciplina
(
	idDisciplina smallint not null identity(1,1)
	, Nome varchar(50) not null
	, DataDisciplina datetime constraint defDataDisciplina default getdate()
	, StatusDisciplina varchar(8) constraint defStatusDisciplina default ('Aberta')
	, PlanoDeEnsino varchar(500)
	, CargaHoraria tinyint not null
	, Competencias varchar(500)
	, Habilidades varchar(500)
	, Ementa varchar(500)
	, idCoordenador smallint not null
	, ConteudoProgramatico varchar(500)
	, BibliografiaBasica varchar(500)
	, BibliografiaComplementar varchar(500)
	, PercentualPratico tinyint not null 
	, PercentualTeorico tinyint not null
	, constraint pkidDisciplina primary key (idDisciplina)
	, constraint fkCoordenadorDisciplina foreign key (idCoordenador) references Coordenador
	, constraint uqNomeDisciplina unique (Nome)
	, constraint ckStatusDisciplina check (StatusDisciplina = 'Aberta' or StatusDisciplina = 'Fechada')
	, constraint ckCargaHoraria check (CargaHoraria = 40 or CargaHoraria = 80)
	, constraint ckPercentualTeorico check (PercentualTeorico between 0 and 100)
	, constraint ckPercentualPratico check (PercentualPratico between 0 and 100)
)

create table Curso
(
	idCurso smallint not null identity(1,1)
	, Nome varchar(50) not null
	, constraint uqNomeCurso unique (Nome)
	, constraint pkidCurso primary key (idCurso)
)

