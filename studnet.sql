CREATE TABLE `Students` (
 `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '학번',
 `name` varchar(32) NOT NULL,
 `addr` varchar(30) NOT NULL,
 `birth` varchar(8) NOT NULL,
 `tel` varchar(15) NOT NULL,
 `email` varchar(31) NOT NULL,
 `regdt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (`id`),
 KEY `index_Students_tel` (`tel`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

select * from Student where birth like '198%' order by addr, name desc;
select * from Student;
select * from Student where name like '방__';
select * from Student where id in (10, 20, 30);
select * from Student where id = 10 or id = 20 or id = 30;
select * from Student where id between 10 and 30;

select * from Student where email  like 'a%' and tel like '010-%9';

select * from Student where addr like'강%' order by birth desc limit 10, 5;


update Test set name=(select name from Student where id=1) where id=3;
select name from Student where id=1;
insert into Test(name) value('김이수');
insert into Test set name='김삼수';

select * from Test;Test