select
    appid,
    positive_ratings,
    negative_ratings,
    average_playtime,
    median_playtime,
    achievements,
    price,
    owners,
    positive_ratings * 1.0 / (positive_ratings + negative_ratings) as rating_ratio
FROM {{ source('gold', 'steam') }}