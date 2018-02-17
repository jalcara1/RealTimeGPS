# RealTimeGPS


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

to run this project locally you must have installed, NOTE: this was deployed in
linux enviroment , specially ubuntu 16.04.

* [npm and node](https://docs.npmjs.com/getting-started/installing-node) - The web framework used


### Installing

A step by step series of examples that tell you have to get a development env running

* clone this repo
```
$git clone https://github.com/jalcara1/RealTimeGPS.git
```

* once in the folder, run the next command where the package.json is (this will install all the dependecies for the app)
```
$npm install 
```

* now you could run the project, before run the server check if you have mongod
service running (for ubuntu 16.04: sudo service mongod start) and check that port:3000 is free to use

```
$ node server.js
```

* if everything went rigth you should see the next message

```
MongoDB connected

connection with the MongoDB successful
```

## Running the tests

To test if the app is working , you could do it on your local browser, and start exploring the app using the default url that was meant to be

http://127.0.0.1:8000/

## Running the tests

To test if the app is working in the DCA , you could do it on your local browser, and start exploring the app using the default url that was meant to be

http://10.131.137.202:443/

## Deployment

there is already an instance of this app runnig on heroku on the next page

https://fast-beyond-41815.herokuapp.com/

## Built With

* npm 3.5.2
* node v4.2.6
* mongodb - Mlab

## Authors

* ** Juan Pablo Alcaraz Florez**