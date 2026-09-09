select
    steam_appid as appid,
    header_image,
    screenshots,
    background,
    movies
from {{ source('gold', 'steam_media_data') }}