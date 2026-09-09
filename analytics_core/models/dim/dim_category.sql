select distinct
    appid,
    trim(lower(category)) as category
from {{ref('stg_steam')}}
cross join unnest(split(coalesce(categories, ''), ';')) as t(category)
where trim(category) <> ''