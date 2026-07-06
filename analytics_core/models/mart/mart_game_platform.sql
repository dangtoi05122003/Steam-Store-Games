SELECT
    appid,
    TRIM(platform) AS platform
FROM {{ source('gold', 'steam') }}
CROSS JOIN UNNEST(SPLIT(platforms, ';')) AS t(platform)