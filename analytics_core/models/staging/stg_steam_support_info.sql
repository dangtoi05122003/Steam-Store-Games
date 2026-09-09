select
    steam_appid as appid,
    website,
    support_url,
    support_email
from {{ source('gold', 'steam_support_info') }}