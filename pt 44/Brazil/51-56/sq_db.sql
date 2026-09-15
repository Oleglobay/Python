create table if not exists mainmenu(
id integer primary key autoincrement,
title text not null,
url text not null
);
create table if not exists newsTable(
id integer primary key autoincrement,
image text not null,
title text not null,
description text not null
);
create table if not exists contactTable(
id integer primary key autoincrement,
num text not null,
title text not null,
description text not null
);
create table if not exists users (
id integer primary key autoincrement,
nick text not null,
email text not null,
password text not null,
fname text not null,
sname text not null,
age text not null,
);