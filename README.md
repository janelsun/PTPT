PTPT website
MYSQL COMMAND:

CREATE SCHEMA PTPT;
CREATE USER 'piupiu'@'localhost' IDENTIFIED BY 'PiuPiu2016';
GRANT ALL PRIVILEGES ON ptpt.* TO 'piupiu'@'localhost';
FLUSH PRIVILEGES;


22/06 UPDATE:
admin username:ptpt
admin password:piupiu2016

models user,tutee,tutor done.
models module, tutor_mod not yet...
