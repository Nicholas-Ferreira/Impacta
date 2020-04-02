-- Nicholas Ferreira - 1900953
-- Leonardo Ferreira - 1901008
-- João Pedro Bello	 - 1800995

CREATE TABLE PEDIDO(
	codigo INT IDENTITY,
	data DATETIME,

	CONSTRAINT pk_pedido PRIMARY KEY (codigo)
);

CREATE TABLE PRODUTO(
	codigo INT IDENTITY, 
	nome VARCHAR(50), 
	preco SMALLMONEY,

	CONSTRAINT pk_produto PRIMARY KEY (codigo)
)

CREATE TABLE ITEM(
	numero INT NOT NULL,
	cod_pedido INT NOT NULL,
	cod_produto INT NOT NULL,
	qtd SMALLINT,
	preco MONEY,

    CONSTRAINT pk_item PRIMARY KEY (cod_pedido, cod_produto),
    CONSTRAINT fk_item_pedido FOREIGN KEY (cod_pedido) REFERENCES PEDIDO(codigo),
    CONSTRAINT fk_item_produto FOREIGN KEY (cod_produto) REFERENCES PRODUTO(codigo)
);
