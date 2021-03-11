# Weather station REST API

The project is created for handle data from ESP8266 module, which is collecting temperature and humidity values. At this moment collected data are available here (in JSON format): http://arduino.gaway.pl/api/measurement/. In the future, it is planned to add a page to data visualization.

###[ESP8266 with DHT11 sensor](https://github.com/kmsky/esp8266-with-dht11) - project using this API

## Libraries

- Django (ver. 3.1.7)
- Django REST Framework (ver. 3.12.2)

## Endpoints

| URL   |Method     |Functionality|
|-------|:---------:|------------:|
|`/api/measurement/`|GET|list measurements|
|`/api/measurement/?date1={YYYY-MM-DD}&date2={YYYY-MM-DD}`|GET|list measurements within two dates|
|`/api/measurement/last/`|GET|get last measurement|
|`/api/measurement/{measurementId}`|GET|get specific measurement|
|`/api/measurement/post/`|POST|add measurement|
|`/api/measurement/update/{measurementId}`|PUT|modify measurement|
|`/api/measurement/update/{measurementId}`|PATCH|modify partially measurement|
|`/api/measurement/update/{measurementId}`|DELETE|delete measurement|

#### Example
```djangourlpath
http://arduino.gaway.pl/api/measurement/?date1=2021-03-06&date2=2021-03-07
```

#### cURL example
```shell
$ curl -X POST -u username:password -d "temp=-14.5&humidity=23.3" http://localhost:8000/api/measurement/post/
```

#### Example API answer
for http://arduino.gaway.pl/api/measurement/last/:
```json
{
  "id":314,
  "measure_date":"2021-03-07T13:50:48.686409+01:00",
  "temp":3.0,
  "humidity":87.0
}
```



## Contribute the project!
__If you want to join and contribute to the project with us, create and program your own [ESP8266 module with DHT11](https://github.com/kmsky/esp8266-with-dht11). Then contact us, we will provide you with API access.__

Contact: arduino@gaway.pl

### License
MIT