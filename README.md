Authour: Joseph Cates

contact: jcates5@uoregon.edu

project description: A calculator for determining the opening and closing times for brevets, which are long-distance cycling events with checkpoints. Each checkpoint has an opening time (the earliest you can continue to the next checkpoint) and a closing time (the latest you can reach the checkpoint and still continue in the event). Each distance bracket (0 km - 200 km, 201 km - 400 km, 401 km - 600 km, 601 km - 1000 km) has specific maximum and minimum speeds used to calculate these times.

For example, if an event includes a checkpoint at 200 km, the opening time for this checkpoint would be calculated based on the maximum speed of 34 km/h for the first 200 km. If the next checkpoint is at 400 km, the opening time would be calculated as 200 km divided by 32 km/h (the maximum speed for the 201 km - 400 km bracket), plus 200 km divided by 34 km/h (the time to reach the first checkpoint).

The algorithm takes the checkpoint distance and determines the corresponding distance interval. It then subtracts the total brevet distance from the checkpoint distance, subtracts 200 km (or 400 km for the 1000 km bracket) from the result to find the distance traveled in that interval, calculates the time for that distance, and adds this to the total time. This process continues until the control point distance is reduced to zero. The total time is then rounded and returned.

Additionally, a MongoDB database has been integrated into this project, allowing you to save your input data by pressing the submit button. This action clears all fields, enabling you to input new values for testing without losing previous entries. Pressing "Display" will restore all values that were present on the page before submitting.


Added a flask rest API to the project that communicates with the database to make the overall implementation much cleaner.  The API commands are as follows:

  GET http://API:PORT/api/brevets  displays all brevets stored in the database.

  GET http://API:PORT/api/brevet/ID  displays brevet with id ID.

  POST http://API:PORT/api/brevets  inserts brevet object in request into the database.

  DELETE http://API:PORT/api/brevet/  deletes brevet with id ID.

  PUT http://API:PORT/api/brevet/ID  updates brevet with id ID with object in request.
  



To run this project download the repository, docker and docker compose, create a .env file based off the given template, and then run docker
