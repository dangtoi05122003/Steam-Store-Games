select
    steam_appid as appid,
    detailed_description,
    about_the_game,
    short_description 
from {{ source('gold', 'steam_description_data') }}