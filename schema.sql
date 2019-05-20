drop table if exists booklibrary;
create table booklibrary (
    id integer primary key autoincrement,
    userid integer not null,
    title text not null,
    author text not null,
    pagecount integer not null,
    averagerating real not null,
    thumbnail integer not null
);

drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);

insert into users (username, password) values ('admin', 'password');
insert into users (username, password) values ('user1', 'myapp');
insert into users (username, password) values ('jojo', 'myapp');
