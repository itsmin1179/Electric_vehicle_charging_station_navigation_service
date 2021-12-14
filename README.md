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
     
     ex)
     
     ![KakaoTalk_20210616_171914](https://user-images.githubusercontent.com/60971835/146016022-636eea05-5011-4d75-9ecc-e9d6e4d0ea2c.png)

+ The above two steps will show you the routes and locations of the three charging stations closest to your current location and available without waiting for your current charger.

     ex)
     
     ![KakaoTalk_20210616_172006](https://user-images.githubusercontent.com/60971835/146016209-162e27b8-3935-49ba-a357-74e35b864536.png)
     


---
### result of execution

![KakaoTalk_20210616_172048](https://user-images.githubusercontent.com/60971835/146016219-0d5574b9-6a1a-44c6-bda6-c9a22ec423ef.png)

The picture on the left is when both the current location and destination are set in Korea, and the picture on the right is when coordinates in other countries are set. In Korea, the route visualization function provided by Google Maps cannot be used due to the map export regulations, so even if you set the destination as in the picture on the left, you can see the route is not set. To solve this, it is necessary to use Naver or Kakao API instead of Google Maps API.



