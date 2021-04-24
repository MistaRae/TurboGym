DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS lessons;
DROP TABLE IF EXISTS slots;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY, 
    first_name VARCHAR(255),
    Last_name VARCHAR(255),
    age INT,
    sex VARCHAR(255),
    turbo_membership BOOLEAN,
    active BOOLEAN
);

CREATE TABLE slots (
    id SERIAL PRIMARY KEY, 
    slot_num INT,
    time_stamp VARCHAR(255),
    turbo_slot BOOLEAN
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255),
    class_type VARCHAR(255),
    difficulty VARCHAR(255),
    duration INT,
    capacity INT,
    slot_id INT REFERENCES slots(id) ON DELETE CASCADE   
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE ,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE   
);