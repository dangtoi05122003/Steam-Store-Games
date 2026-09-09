select
    appid,
    name,
    english,
    developer,
    publisher,
    required_age
FROM {{ ref('stg_steam') }}