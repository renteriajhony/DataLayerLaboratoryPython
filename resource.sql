
-- insert into public.person(name,last_name,email) values
-- ('Jhony','Renteria','jrenteria@mail.com'),
-- ('Pablo','Perez','pperz@mail.com'),
-- ('Ninfa','Narvaez','nnarvaez@mail.com')

-- truncate public.person cascade

-- ALTER SEQUENCE person_id_person_seq RESTART WITH 1;
-- UPDATE public.person SET id_person=nextval('person_id_person_seq');

insert into public.user (username, password)
select split_part(email,'@',1) as username, '1234' as password from person order by id_person
-- select * from public.user

select * from public.user;
