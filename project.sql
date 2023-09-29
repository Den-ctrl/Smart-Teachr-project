-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 29, 2023 at 03:40 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `body` text NOT NULL,
  `author` varchar(100) NOT NULL,
  `dateCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`id`, `title`, `body`, `author`, `dateCreated`) VALUES
(30, 'What is Lorem Ipsum?', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', 'user1', '2023-09-25 04:07:45'),
(31, 'Where does it come from?', 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.\n\nThe standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.', 'user1', '2023-09-25 04:07:59'),
(32, 'Why do we use it?', 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for \'lorem ipsum\' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).', 'user1', '2023-09-25 04:08:15'),
(34, 'Where can I get some?', 'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don\'t look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn\'t anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.', 'user2', '2023-09-25 04:11:09');

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `video` blob NOT NULL,
  `author` varchar(100) NOT NULL,
  `dateCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `author` text NOT NULL,
  `dateCreated` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `title`, `author`, `dateCreated`) VALUES
(23, 'Where can I get some?', 'user2', '2023-09-29 11:13:17'),
(24, 'Why do we use it?', 'user1', '2023-09-29 11:13:19'),
(25, 'What is Lorem Ipsum?', 'user1', '2023-09-29 11:14:04'),
(26, 'Where does it come from?', 'user1', '2023-09-29 11:14:06'),
(27, 'Where can I get some?', 'user2', '2023-09-29 12:28:40'),
(28, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:28:43'),
(29, 'Where does it come from?', 'user1', '2023-09-29 12:28:44'),
(30, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:28:45'),
(31, 'Why do we use it?', 'user1', '2023-09-29 12:28:47'),
(32, 'Where can I get some?', 'user2', '2023-09-29 12:28:48'),
(33, 'Why do we use it?', 'user1', '2023-09-29 12:28:56'),
(34, 'Where does it come from?', 'user1', '2023-09-29 12:28:58'),
(35, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:28:59'),
(36, 'Where can I get some?', 'user2', '2023-09-29 12:29:01'),
(37, 'Where can I get some?', 'user2', '2023-09-29 12:31:10'),
(38, 'Why do we use it?', 'user1', '2023-09-29 12:31:11'),
(39, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:31:13'),
(40, 'Where does it come from?', 'user1', '2023-09-29 12:31:14'),
(41, 'Why do we use it?', 'user1', '2023-09-29 12:31:15'),
(42, 'Where can I get some?', 'user2', '2023-09-29 12:31:17'),
(43, 'Where can I get some?', 'user2', '2023-09-29 12:31:20'),
(44, 'Why do we use it?', 'user1', '2023-09-29 12:31:20'),
(45, 'Where does it come from?', 'user1', '2023-09-29 12:31:22'),
(46, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:31:23'),
(47, 'Where does it come from?', 'user1', '2023-09-29 12:31:24'),
(48, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:31:25'),
(49, 'Why do we use it?', 'user1', '2023-09-29 12:31:26'),
(50, 'Where can I get some?', 'user2', '2023-09-29 12:31:28'),
(51, 'Why do we use it?', 'user1', '2023-09-29 12:31:29'),
(52, 'Why do we use it?', 'user1', '2023-09-29 12:31:32'),
(53, 'Where does it come from?', 'user1', '2023-09-29 12:31:33'),
(54, 'Where does it come from?', 'user1', '2023-09-29 12:31:34'),
(55, 'Why do we use it?', 'user1', '2023-09-29 12:33:49'),
(56, 'What is Lorem Ipsum?', 'user1', '2023-09-29 12:34:02'),
(57, 'Where can I get some?', 'user2', '2023-09-29 12:41:33'),
(58, 'Where can I get some?', 'user2', '2023-09-29 12:43:25'),
(59, 'Where can I get some?', 'user2', '2023-09-29 13:38:46');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'user1', 'pass1'),
(2, 'user2', 'pass2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `history`
--
ALTER TABLE `history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `history`
--
ALTER TABLE `history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
