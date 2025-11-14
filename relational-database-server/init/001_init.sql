CREATE DATABASE IF NOT EXISTS minicloud;
USE minicloud;
CREATE TABLE IF NOT EXISTS notes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO notes(title) VALUES ('Hello from MariaDB!');

CREATE DATABASE IF NOT EXISTS studentdb;
USE studentdb;
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    mssv VARCHAR(10) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    major VARCHAR(50),
    email VARCHAR(100)
);
INSERT INTO students (mssv, full_name, major, email) VALUES
('52200243', 'Ho Bao Ngan', 'Cloud Computing', '52200243@student.tdtu.edu.vn'),
('52200199', 'Nguyen Thanh Phat', 'Information System', '522001993@student.tdtu.edu.vn');