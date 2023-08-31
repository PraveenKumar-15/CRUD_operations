create database Crud_data;
use Crud_data;
create table users(
ID integer auto_increment primary key,
NAME varchar(30),
AGE integer,
CITY varchar(50)
);

select * from users;
insert into users(NAME,AGE,CITY) values("messi",10,"barka"),("jovi",12,"slalam"),("ram",24,"kovai");
drop table users;


