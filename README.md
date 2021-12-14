# Electric_vehicle_charging_station_navigation_service

This project is a service that receives data from electric vehicle charging stations across the country in real time from a public data portal(https://www.data.go.kr/) and provides the locations and paths of three charging stations in consideration of whether it is the closest to the vehicle's current location and whether the charger can be used immediately.

To use this code, you have to receive the service key about data api and googlemap api

> reference data
>
> https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000297
>
> https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=3068728
>
> https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15076352 


You need to fix the following before running your code:

+ Enter the service key you received after applying for data utilization at the public data portal.
+ Enter your location key after applying for use of Google Maps API.

This code includes the following features:

+ Get the current location coordinates using the Google Maps api.
+ Of the data received through the api, only the name of the charging station, whether or not the charger is used, and location information are used.
+ The above two steps will show you the routes and locations of the three charging stations closest to your current location and available without waiting for your current charger.

