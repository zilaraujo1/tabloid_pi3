-- phpMyAdmin SQL Dump
-- version 5.2.0-1.fc36
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 10/11/2022 às 01:59
-- Versão do servidor: 10.5.16-MariaDB
-- Versão do PHP: 8.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `tabloid`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `comercios_item`
--

CREATE TABLE `comercios_item` (
  `item_id` int(11) NOT NULL,
  `tipo` varchar(240) NOT NULL,
  `nome` varchar(240) NOT NULL,
  `marca` varchar(20) NOT NULL,
  `quantidade` varchar(10) NOT NULL,
  `peso` varchar(10) NOT NULL,
  `valor` varchar(10) NOT NULL,
  `fim_promo` varchar(10) NOT NULL,
  `foto` varchar(120) DEFAULT NULL,
  `data` date NOT NULL,
  `atualizado` date DEFAULT NULL,
  `estab_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `comercios_item`
--

INSERT INTO `comercios_item` (`item_id`, `tipo`, `nome`, `marca`, `quantidade`, `peso`, `valor`, `fim_promo`, `foto`, `data`, `atualizado`, `estab_fk`) VALUES
(5, 'Higiene', 'Papel higiênico', 'Babbel', '12 unidade', '30 m', '16,00', '09/11/22', 'papel.png', '2022-11-09', NULL, 5),
(6, 'Bebida', 'Cerveja', 'Skoll', '8 unidades', '300 ml', '32,00', '09/11/22', 'cerveja.png', '2022-11-09', NULL, 5);

-- --------------------------------------------------------

--
-- Estrutura para tabela `estabelecimentos`
--

CREATE TABLE `estabelecimentos` (
  `id` int(11) NOT NULL,
  `nome` varchar(240) NOT NULL,
  `endereco` varchar(240) NOT NULL,
  `telefone` varchar(20) NOT NULL,
  `hora_func` varchar(20) NOT NULL,
  `descricao` varchar(240) NOT NULL,
  `imagem` varchar(200) NOT NULL,
  `user_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `estabelecimentos`
--

INSERT INTO `estabelecimentos` (`id`, `nome`, `endereco`, `telefone`, `hora_func`, `descricao`, `imagem`, `user_fk`) VALUES
(5, 'Mercado do Alencar', 'Av. Marechal Simões 405', '(11)95656-5656', '08:30 - 19:00', 'Mercado e padaria', 'mercado.png', 7),
(6, 'Stillus Hair', 'r: Maria Da Glória 45', '(11)96565-6565', '10:00 - 15:30 ', 'A Stillus Hair realiza cortes de cabelos modernos femininos, permanentes, coloração, entre outros serviços.', 'stillus.png', 8);

-- --------------------------------------------------------

--
-- Estrutura para tabela `servicos`
--

CREATE TABLE `servicos` (
  `id` int(11) NOT NULL,
  `tipo` varchar(240) NOT NULL,
  `descricao` tinytext NOT NULL,
  `valor` varchar(240) NOT NULL,
  `horario_func` varchar(240) NOT NULL,
  `foto` varchar(120) NOT NULL,
  `data` date NOT NULL,
  `atualizado` date DEFAULT NULL,
  `estab_fk` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `servicos`
--

INSERT INTO `servicos` (`id`, `tipo`, `descricao`, `valor`, `horario_func`, `foto`, `data`, `atualizado`, `estab_fk`) VALUES
(4, 'corte afro', 'Corte afro moderno', '32,00', '10:30 - 12:30 aos sábados', 'corte01.png', '2022-11-09', NULL, 6),
(5, 'Manicure', 'Faz pés e mãos, aplica design de unhas e tira cutículas', '25,00', '14:30 às 17:00 somente sábado', 'mani.png', '2022-11-09', NULL, 6);

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nome` varchar(200) NOT NULL,
  `cnpj` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `telefone` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `cnpj`, `email`, `telefone`) VALUES
(7, 'José De Alencar', '258963145', 'josealencar@test.com', '1178968574'),
(8, 'Barbara Gonçalves', '54789685212', 'barbara@test.com', '1123654789');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `comercios_item`
--
ALTER TABLE `comercios_item`
  ADD PRIMARY KEY (`item_id`),
  ADD KEY `comercios_item_ibfk_1` (`estab_fk`);

--
-- Índices de tabela `estabelecimentos`
--
ALTER TABLE `estabelecimentos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estabelecimentos_ibfk_1` (`user_fk`);

--
-- Índices de tabela `servicos`
--
ALTER TABLE `servicos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `servicos_ibfk_1` (`estab_fk`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `comercios_item`
--
ALTER TABLE `comercios_item`
  MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `estabelecimentos`
--
ALTER TABLE `estabelecimentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de tabela `servicos`
--
ALTER TABLE `servicos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `comercios_item`
--
ALTER TABLE `comercios_item`
  ADD CONSTRAINT `comercios_item_ibfk_1` FOREIGN KEY (`estab_fk`) REFERENCES `estabelecimentos` (`id`);

--
-- Restrições para tabelas `estabelecimentos`
--
ALTER TABLE `estabelecimentos`
  ADD CONSTRAINT `estabelecimentos_ibfk_1` FOREIGN KEY (`user_fk`) REFERENCES `usuario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Restrições para tabelas `servicos`
--
ALTER TABLE `servicos`
  ADD CONSTRAINT `servicos_ibfk_1` FOREIGN KEY (`estab_fk`) REFERENCES `estabelecimentos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
