select
    steam_appid as appid,
    pc_minimum,
    pc_recommended,
    mac_minimum,
    mac_recommended,
    linux_minimum,
    linux_recommended
FROM {{ source('gold', 'steam_requirements_data') }}