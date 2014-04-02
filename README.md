doordash-challenge
==================

You will be given a "street map" with the locations of one or more pairs of restaurants and customers, and the location of one or more drivers. Each driver or set of drivers must collectively pick up and deliver all the orders without driving offroad in order to successfully complete a map.

Maps will be provided as follows:

```
1,1       // starting x,y of driver(s), semicolon delimited
6,6       // width and height of the map, comma delimited
.233A.    // the 6x6 map
.1....
.1211.
.1..1.
.1222.
.a....
```

Lower and uppercase letters will represent the restaurant and customer pair, respectively (restaurant a gets picked up and delivered to customer A, restaurant b to customer B, etc). Visiting the road tile tangent (not diagonally) to the restaurant or customer will perform a "pickup" or "delivery". We will assume instantaneous pickup delivery times (the driver does not need to wait at that square). A period tile represents an undriveable and unremarkable tile.

Each number tile represents the amount of time it takes to drive through that tile. Higher numbers means it will take longer to drive through, and each time a driver moves into a tile, that tile value will count towards the overall delivery time. The starting tile value does not count. These time values will be added up, and a lower score means a quicker delivery time, which is obviously desirable.

Some maps will have multiple drivers, which can operate simultaneously and independently of each other. Drivers cannot exchange orders. Drivers are assumed to not interact with each other, and they will not impede each other on the road or at customer/restaurant locations. Each driver's path must be separately recorded, and the driver times will be added together for that map's score. (Alternately, the scoring could be how long each customer waits for their food, which would take care of the unused driver problem which multiple drivers could introduce)

Drivers are free to pick up orders in whatever order they choose, assume their cars can hold an infinite amount of orders.

The solution will be sequential strings of 'N','S','E','W', representing cardinal directional movements on roads for each individual driver.

The best solution for the above map would be: SSSNNNNEE, for a total score of 14.

--------------------------

This challenge is intended to be too difficult to optimally solve in a few hours. For reference, the Firebase challenge is supposed to take about 6 hours, and has a hard time limit of 16 hours. I would argue that this is slightly more difficult than theirs.

They would be provided with test cases, a testing script, and would be free to use any language of choice. They would submit the code, and we would be able to collectively review it and talk with them about it. The final implementation would be tested against a large set of variable test cases.

Bonus: this would allow an internal competition for the best score.