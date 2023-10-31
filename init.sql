/*
* Create a group
*/
CREATE ROLE poseidon_dev
    WITH NOLOGIN;

/*
* Create database
*/
CREATE DATABASE poséidon;

/*
* Transfer ownership to group
*/
ALTER DATABASE poséidon
    OWNER TO poseidon_dev;

/*
* Grant permissions to group
*/
GRANT SELECT, INSERT, UPDATE, DELETE
    ON ALL TABLES
    IN SCHEMA public
    TO poseidon_dev;

/*
* Give CREATE permission to backend group
*/
GRANT CREATE
    ON SCHEMA public
    TO poseidon_dev;

/*
* Create new users
*/
CREATE ROLE postgres
    WITH LOGIN
    PASSWORD 'password'
    INHERIT;

GRANT poseidon_dev
    TO postgres