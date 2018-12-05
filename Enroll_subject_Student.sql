create table Club(
	id smallint unsigned not null auto_increment primary key,
	name varchar(31) not null,
    createdate timestamp not null default current_timestamp,
	leader int unsigned,
    constraint foreign key fk_leader_student(leader) references Student(id)
);
-- unsigned 된거를 student를 일치 시키고 create table 먼저 실행해야됨

insert into Club(name, leader) values('요술부', 300);

select * from Club;

select c.*, s.name as 'student name' from Club c inner join Student s on c.leader = s.id;

create table Prof(
	id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    likecnt int default 0 
    
);

select ceil(rand() * 100) from dual;

insert into Prof(name, likecnt) select name,ceil(rand() * 100)  from Student order by rand() limit 100;

select * from Prof;


create table subject(
	id int unsigned not null auto_increment primary key,
    name varchar(31) not null,
    prof smallint unsigned not null,
    constraint foreign key fk_prof(prof) references Prof(id)
    on delete set null,

);
-- fk_prof(여기 안에 prof 컬럼을 넣어줘야함) 그리고 Prof에서 레퍼런스를 불러오기alter


insert into subject(name,prof)
 select '국어', id from Prof order by rand() limit 10;
 
 update subject set name ='기술' where name = '국어' and id <> 10 limit 1;
 
 select * from subject;
 

desc subject;


select * from Enroll;

create table Enroll(
	id int unsigned auto_increment primary key,
    subject int unsigned not null,
    student int unsigned not null,
	constraint foreign key fk_subject(subject) references subject(id), 
    constraint foreign key fk_student(student) references Student(id)
	
);

insert into subject(name,Student)
 select '국어', id from Prof order by rand() limit 1000;

insert into Enroll(name, subject) select name from Student order by rand() limit 1000;

select * from subject (select name from Student order by rand() limit 1000);

--insert into Enroll(name, subject, Student) 
 (select b.*, s.name as 'student name' from subject b inner join Student s on b.name = s.id);

--문장끝마다 ,표시하기 / 대소문자/ colum type 맞추기
