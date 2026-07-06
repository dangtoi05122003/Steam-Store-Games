select
    appid,
    name,
    release_date,
    english,
    developer,
    publisher,
    platforms,
    categories,
    genres,
    steamspy_tags,
    required_age
FROM {{ source('gold', 'steam') }}