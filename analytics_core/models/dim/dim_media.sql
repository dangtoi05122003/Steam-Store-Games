select
    appid,
    header_image,
    screenshots,
    background,
    movies
from {{ ref('stg_steam_media_data') }}