select
    appid,
    positive_ratings,
    negative_ratings,
    average_playtime,
    median_playtime,
    achievements,
    price,
    cast(date_format(release_date, '%Y%m%d') as integer) as date_key,
    try_cast(split_part(replace(owners, ',', ''), '-', 1)as bigint) as owner_min,
    try_cast(split_part(replace(owners, ',', ''), '-', 2)as bigint) as owner_max,
    positive_ratings * 1.0 / (positive_ratings + negative_ratings) as rating_ratio
FROM {{ ref('stg_steam') }}