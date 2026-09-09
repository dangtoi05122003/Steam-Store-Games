select distinct
    cast(date_format(release_date, '%Y%m%d') as integer) as date_key,
    release_date as full_date,
    year(release_date) as year,
    month(release_date) as month,
    day_of_week(release_date) as day_of_week
from {{ ref('stg_steam')}}