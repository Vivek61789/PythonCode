# Write your MySQL query statement below
SELECT ROUND(
    COUNT(DISTINCT a.player_id) / COUNT(DISTINCT f.player_id),
    2
) AS fraction
FROM Activity f
LEFT JOIN Activity a
    ON a.player_id = f.player_id
   AND a.event_date = DATE_ADD(f.event_date, INTERVAL 1 DAY)
WHERE f.event_date = (
    SELECT MIN(event_date)
    FROM Activity
    WHERE player_id = f.player_id
);