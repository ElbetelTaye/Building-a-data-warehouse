{{config(materialized='table')}}

WITH filtered_data AS (
    SELECT *
    FROM {{ source('raw_data') }}
    WHERE content IS NOT NULL
)
SELECT *
FROM filtered_data;
