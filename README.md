# Homework
Zoom-Camp Homework
Question:1
docker run -it --entrypoint=bash python:3.13 #creating a docker image with entrypoint = Bash.
pip version = pip 26.2.1

Question:2
postgres:5432
db:5432

Dataset ready with docker file

Question:3
select count(*) from 
public.green_taxi_trips 
WHERE lpep_pickup_datetime >= '2025-11-01'
AND lpep_pickup_datetime < '2025-12-01'
and trip_distance <=1;

Question:4 
SELECT 
    CAST(lpep_pickup_datetime AS DATE) AS pickup_day, 
    MAX(trip_distance) AS max_distance
FROM public.green_taxi_trips
WHERE trip_distance < 100
GROUP BY CAST(lpep_pickup_datetime AS DATE)
ORDER BY max_distance DESC
LIMIT 1;

Question: 5

select "Zone", sum(total_amount)as total 
from public.taxi_zones tz
join green_taxi_trips gt on tz."LocationID" = gt."PULocationID"
where cast(lpep_pickup_datetime as date) = '2025-11-18'
group by tz."Zone"
order by total desc limit 1

Question:6
select tz."Zone", gt.tip_amount, gt.lpep_pickup_datetime
from public.taxi_zones tz 
join green_taxi_trips gt on tz."LocationID" = gt."DOLocationID"
where gt."PULocationID" = 74 
and cast(gt.lpep_pickup_datetime as date) >= '2025-11-01' and cast(gt.lpep_pickup_datetime as date) < '2025-12-01'
order by gt.tip_amount desc limit 1;
