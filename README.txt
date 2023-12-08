Создание таблицы:

CREATE TABLE demo(
user_id serial PRIMARY KEY,
fio CHARACTER VARYING(255) NOT NULL,
email CHARACTER VARYING(255) NOT NULL,
city CHARACTER VARYING(255) NOT NULL,
school CHARACTER VARYING(255) NOT NULL,
is_finished boolean,
type_mk boolean)