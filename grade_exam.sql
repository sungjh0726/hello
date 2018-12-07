CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `dooodb`@`%` 
    SQL SECURITY DEFINER
VIEW `Report1` AS
    SELECT 
        `sub`.`id` AS `id`,
        `sub`.`sbj_name` AS `sbj_name`,
        `sub`.`stu_name` AS `stu_name`,
        `g`.`midterm` AS `midterm`,
        `g`.`finalterm` AS `finalterm`,
        (`g`.`midterm` + `g`.`finalterm`) AS `total_score`,
        ((`g`.`midterm` + `g`.`finalterm`) / 2) AS `avg_score`
    FROM
        (`dooodb`.`Grade` `g`
        JOIN (SELECT 
            `e`.`id` AS `id`,
                `sbj`.`name` AS `sbj_name`,
                `stu`.`name` AS `stu_name`
        FROM
            ((`dooodb`.`Enroll` `e`
        JOIN `dooodb`.`Student` `stu` ON ((`e`.`student` = `stu`.`id`)))
        JOIN `dooodb`.`subject` `sbj` ON ((`e`.`subject` = `sbj`.`id`)))
        ORDER BY `sbj`.`name`) `sub` ON ((`g`.`enroll` = `sub`.`id`)));
        
select sub.id, sub.sbj_name, sub.stu_name, g.midterm, g.finalterm
  from Grade g inner join (
select e.id, sbj.name as sbj_name, stu.name as stu_name
 from Enroll e inner join Student stu on e.student = stu.id
			   inner join subject sbj on e.subject = sbj.id
			    order by sbj.name) sub
                     on g.enroll = sub.id;
                     
-- 학생이 듣고 있는 과목들이 어떤 것들이 있는 지 알아봐
-- 과목 안에 
	
select stu_name, count(*)
  from Report1
  group by stu_name;
				
select sbj_name, group_concat(stu_name) as 'student names' from t_report1 group by sbj_name;