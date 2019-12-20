create database cmdb default charset utf8;

use cmdb;

create table user(
    id int primary key auto_increment,
    name varchar(32) unique not null default '',
    password varchar(512) not null default '',
    birthday date not null,
    height float not null default 0,
    weight float not null default 0,
    tel varchar(32) not null default '',
    sex bool not null default 1,
    remark text,
    addr varchar(256) not null default '',
    status int not null default 0
) default charset utf8;


insert into user(name, password, birthday, height, weight, tel, sex, remark, addr)
values
('kk', '123456', '1987-10-10', 168, 68, '1234567896', 1, '', '北京'),
('kk1', '123456', '1987-10-10', 168, 68, '1234567895', 1, '', '北京'),
('kk2', '123456', '1987-10-10', 168, 68, '1234567894', 1, '', '北京'),
('kk3', '123456', '1977-10-10', 168, 68, '1234567893', 1, '', '北京'),
('woniu', '123456', '1988-10-10', 168, 68, '1234567892', 1, '', '北京'),
('ada', '123456', '1997-10-10', 168, 68, '1234567891', 0, '', '北京');

create table users(
	id int primary key auto_increment,
	name varchar(20) not null default '',
	password varchar(256) not null default '',
	age int not null default '',
	sex bool not null default 1,
	tel varchar(32) not null default ''
	) default charset utf8;

insert into users( name, password, age, sex, tel)
    values
        ('kk', '123', 19, 0, '139133333'),
        ('kk1', '123', 19, 0, '139133333'),
        ('kk2', '123', 19, 0, '139133333'),
        ('kk3', '123', 19, 0, '139133333'),
        ('kk4', '123', 19, 0, '139133333')
