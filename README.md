# WeatherSearch
This is a weather search website!
****
## Techniques
* 01 Python version 3.4
* 02 Django version 1.8.16
* 03 Sqlite3(built-in django)
* 04 Request library
* 05 Open Weather Map (https://openweathermap.org/)
* 06 Open Street Map (https://www.openstreetmap.org/about)

## Functions
* 01 Need a Location input widget (The weather you want to know in that place).
* 02 Display the weather information about that place.
* 03 When users input location and press search button, it will submit to server in form format, and server will request OWM api and get weather data. Finally, render the weather information to HTML.
* 04 If the location not exist, the server will hint users that location is not found.

## Results
成果影片連結:
https://www.youtube.com/watch?v=N04y1LOI4Y8 <br><br>
天氣查詢網站
![](https://i.imgur.com/Gl4lJf3.png)
輸入想查詢之城市，會出現該城市之天氣資訊和地圖所在位置
![](https://i.imgur.com/VCsPMhP.png)
若輸入錯誤或者該城市找不到，則會有提示訊息告知使用者
![](https://i.imgur.com/P5gbFOh.png)

