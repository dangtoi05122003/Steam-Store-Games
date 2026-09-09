select distinct
    appid,
    trim(lower(genre)) as genre
from {{ref('stg_steam')}}
cross join unnest(split(coalesce(genres, ''), ';')) as t(genre)
where trim(genre) <> ''