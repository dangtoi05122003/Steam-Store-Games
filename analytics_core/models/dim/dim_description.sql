select
    appid,
    detailed_description,
    about_the_game,
    short_description
from {{ ref('stg_steam_description_data')}}