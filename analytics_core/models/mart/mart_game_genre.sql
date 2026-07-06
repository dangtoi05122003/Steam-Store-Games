SELECT
    appid,
    TRIM(genre) AS genre
FROM {{ source('gold', 'steam') }}
CROSS JOIN UNNEST(SPLIT(genres, ';')) AS t(genre)