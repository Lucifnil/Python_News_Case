drop table  if exists news;

create table if not exists news(
    id integer primary key autoincrement,
    title text not null ,
    link text,
    source_name text,
    title_length integer,
    keyword text,
    pub_time text

);