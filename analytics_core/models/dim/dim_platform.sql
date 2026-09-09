select distinct
    appid,
    trim(lower(platform)) as platform
from {{ref('stg_steam')}}
cross join unnest(split(coalesce(platforms, ''), ';')) as t(platform)
where trim(platform) <> ''