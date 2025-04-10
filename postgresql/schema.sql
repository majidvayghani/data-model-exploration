-- postgresql/schema.sql
-- SQL statements based on the 'Money-diagram.png'

CREATE TYPE transaction_type AS ENUM ('INCOME', 'EXPENSE');

-- Create the Users table
CREATE TABLE Users (
    Id UUID PRIMARY KEY,
    UserName VARCHAR(20) UNIQUE NOT NULL,
    Password UUID NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(40) NOT NULL,
    Email VARCHAR(250) UNIQUE NOT NULL,
    Is_Active BOOLEAN NOT NULL DEFAULT TRUE,
    Is_Superuser BOOLEAN NOT NULL DEFAULT FALSE,
    Created_at TIMESTAMP,
    Updated_at TIMESTAMP,
    SoftDeleted_at TIMESTAMP,
    HardDeleted_at TIMESTAMP 
);

-- Create the Transactions table with a Foreign Key to Users
CREATE TABLE Transactions (
    Id UUID PRIMARY KEY,
    _User UUID NOT NULL,
    Type transaction_type NOT NULL, 
    Date DATE NOT NULL,
    Amount DECIMAL(11, 2) NOT NULL,
    Category VARCHAR(25) NOT NULL,
    Description VARCHAR(100) NULL,
    Tag VARCHAR(15) NULL,
    Created_at TIMESTAMP,
    Updated_at TIMESTAMP,
    SoftDeleted_at TIMESTAMP,
    HardDeleted_at TIMESTAMP,

    CONSTRAINT fk_user
        FOREIGN KEY(_User)
        REFERENCES Users(Id)
);

-- Create the Token table with a Foreign Key to Users
CREATE TABLE Token (
    Id UUID PRIMARY KEY,
    _User UUID NOT NULL,
    Token VARCHAR(255) UNIQUE NOT NULL,
    Is_Active BOOLEAN NOT NULL DEFAULT TRUE,
    Created_at TIMESTAMP,
    SoftDeleted_at TIMESTAMP,
    HardDeleted_at TIMESTAMP,

    CONSTRAINT fk_user
        FOREIGN KEY(_User)
        REFERENCES Users(Id)
);

-- Optional: Add indexes for frequently queried columns, especially Foreign Keys