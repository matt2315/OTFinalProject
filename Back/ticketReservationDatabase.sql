Create Database ticketReservation;
use ticketReservation;

CREATE TABLE userAccount (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    accountUsername VARCHAR(50) NOT NULL,
    accountPassword VARCHAR(255) NOT NULL
);


CREATE TABLE ticket (
    ticketId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    movieTitle VARCHAR(70) NOT NULL,
    ticketDatePurchased  DATE NOT NULL,
    ticketPrice INT NOT NULL,
    ticketQuantity INT NOT NUll
);

select * from userAccount;

select * from ticket;