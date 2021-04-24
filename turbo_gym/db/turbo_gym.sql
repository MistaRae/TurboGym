DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS slots;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY 

);

CREATE TABLE slots (
     id SERIAL PRIMARY KEY 
    
);

CREATE TABLE lessons (
     id SERIAL PRIMARY KEY 
    
);

CREATE TABLE bookings (
     id SERIAL PRIMARY KEY 
    
);