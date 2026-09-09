select
    appid,
    tags
from {{ source('gold', 'steamspy_tag_data') }}