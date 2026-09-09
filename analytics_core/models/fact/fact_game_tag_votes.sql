select distinct
    appid,
    trim(lower(tag)) as tag,
    vote
from {{ ref('stg_steamspy_tag_data')}}
cross join unnest(tags) as t(tag, vote)
where trim(tag) <> ''