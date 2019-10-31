-- relatório 1
SELECT
    curso.sigla + ' ' + turma.semestre + turma.letra AS Curso,
    COUNT(*) AS Total
FROM
    DisciplinaOfertada as disciplinaOfer INNER JOIN
    Disciplina AS disc ON disciplinaOfer.id_disciplina = disc.id INNER JOIN
    SolicitacaoMatricula AS disciplinaSoli ON disciplinaOfer.id = disciplinaSoli.id_disciplina INNER JOIN
    Turma AS turma ON disciplinaOfer.id_turma = turma.id INNER JOIN
    Curso AS curso ON turma.id_curso = curso.id
WHERE
    disciplinaOfer.ano = 2019 AND
    disciplinaOfer.semestre = 2 AND
    disciplinaSoli.data_aprovacao IS NOT NULL
GROUP BY
    curso.sigla + ' ' + turma.semestre + turma.letra


-- relatório 2
SELECT
    curso.sigla + ' ' + turma.semestre + turma.letra AS Curso,
    COUNT(*) AS Total
FROM
    DisciplinaOfertada as disciplinaOfer INNER JOIN
    Disciplina AS disc ON disciplinaOfer.id_disciplina = disc.id INNER JOIN
    SolicitacaoMatricula AS disciplinaSoli ON disciplinaOfer.id = disciplinaSoli.id_disciplina INNER JOIN
    Turma AS turma ON disciplinaOfer.id_turma = turma.id INNER JOIN
    Curso AS curso ON turma.id_curso = curso.id
WHERE
    disciplinaOfer.ano = 2019 AND
    disciplinaOfer.semestre = 2 AND
    disciplinaSoli.data_aprovacao IS NOT NULL
GROUP BY
    curso.sigla + ' ' + turma.semestre + turma.letra
HAVING
    COUNT(*) > 30


-- relatório 3
SELECT
    curso.sigla + ' ' + turma.semestre + turma.letra AS Curso,
    usuarioProf.nome AS 'Professor',
    usuarioProfResp.nome AS 'Professor Responsavel',
    disciplina.bibliografia_basica AS Bibliografia
FROM
    DisciplinaOfertada as disciplinaOfer INNER JOIN
    Disciplina AS disciplina ON disciplinaOfer.id_disciplina = disciplina.id INNER JOIN
    Turma AS turma ON disciplinaOfer.id_turma = turma.id INNER JOIN
    Curso AS curso ON turma.id_curso = curso.id INNER JOIN

    Professor AS professorResp ON disciplina.id_professor_responsavel = professorResp.id INNER JOIN
    Usuario AS usuarioProfResp ON professorResp.id_usuario = usuarioProfResp.id INNER JOIN

    Professor AS professor ON disciplinaOfer.id_professor = professor.id INNER JOIN
    Usuario AS usuarioProf ON professor.id_usuario = usuarioProf.id
WHERE
    disciplina.bibliografia_basica like '%SQL%'


-- relatório 4
SELECT
    curso.sigla + ' ' + turma.semestre + turma.letra AS Curso,
    COUNT(*) AS Total,
    usuarioCoor.nome AS Coordenador
FROM
    DisciplinaOfertada as DO INNER JOIN
    SolicitacaoMatricula AS SM ON DO.id = SM.id_disciplina INNER JOIN
    Turma AS turma ON DO.id_turma = turma.id INNER JOIN
    Curso AS curso ON turma.id_curso = curso.id INNER JOIN
    Coordenador AS coordenador ON SM.id_coordenador =  coordenador.id INNER JOIN
    Usuario AS usuarioCoor ON coordenador.id_usuario = usuarioCoor.id
WHERE
    SM.data_aprovacao IS NULL
GROUP BY
    usuarioCoor.nome,
    curso.sigla + ' ' + turma.semestre + turma.letra

