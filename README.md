RealTimeGPS

"Topicos especiales en telematica" - Project 1


## Getting Started

These instructions will get you a copy of the project and how to run on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

To run this project you must installed,

* [NodeJS](https://nodejs.org/es/) - The web framework used
* [MongoDB](https://docs.mongodb.com/) - DataBase

## Design

### Data
Everything that is going to be store is in schema format , example :
```
    {
        email: String,
        password: String,
        trk : [{
            lat : String,
            lng : String
        }]
    }
```

### Dependencies
* Bcrypt: Password hashing function
* Body-Parser: Understand data from the Web Application
* Connect-Flash: Session used for storing messages
* Cookie: Piece of data sent from a website and stored
* Ejs: Client-side templating language
* Express: Web application framework to write a clear and light server
* Mongoose: Allow us writing MongoDB validation
* Morgan: Used for automated logging of requests details
* Passport: Extremely flexible and modular authentication middleware for NodeJS

### Installing and Running

* clone repository
```
$ git clone https://github.com/jalcara1/RealTimeGPS.git
```

* Run where the package.json is (Will install all the dependecies)
```
$ npm install
```

### Execution
* Execute the command and could run the project

```
$ npm start
```
* Are running on port:3000

# Execute with Apache-Server
* To configure the firewall and the network interface [Apache-RedInterface](https://devops.profitbricks.com/tutorials/how-to-set-up-ip-and-port-based-virtual-hosting-vhosts-with-apache-web-server-on-centos-7/)
* To connect the Web Server (Apache-Server) with the aplication you must intalled Passenger [Passenger](https://www.phusionpassenger.com/library/install/apache/install/oss/el7/)
* Then you could configure Apache-Server to run the aplication [Apache-Server](https://www.phusionpassenger.com/library/walkthroughs/deploy/nodejs/digital_ocean/apache/oss/el7/deploy_app.html)

### Running the tests

To test the aplication on a local Web Browser.

http://localhost:3000/

### Deployment in Heroku

To deploy the application in a Heroku Server

[Heroku-Platform](https://devcenter.heroku.com/categories/nodejs)


### Built With

* npm 3.10.10
* NodeJS v6.12.3
* Mongod v3.6.3

###  Test - Application
Can test the applicaiton deployed and heroku or in the DCA (Data Center Academic)

* [Application on Heroku](https://afternoon-savannah-18678.herokuapp.com) -- https://afternoon-savannah-18678.herokuapp.com

* [Application on DCA](http://10.131.137.162) -- http://10.131.137.162

## Authors

* **Juan Pablo Alcaraz Flórez**