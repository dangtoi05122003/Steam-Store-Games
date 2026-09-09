select distinct
    appid,
    trim(lower(tag)) as tag
from {{ ref('stg_steam')}}
cross join unnest(split(coalesce(steamspy_tags, ''), ';')) as t(tag)
where trim(tag) <> ''