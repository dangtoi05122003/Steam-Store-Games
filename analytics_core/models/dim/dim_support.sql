select
    appid,
    website,
    support_url,
    support_email
from {{ ref('stg_steam_support_info') }}