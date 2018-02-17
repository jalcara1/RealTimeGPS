var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');
var routes = require('./routes'); //importing route

app.use(bodyParser.json());
mongoose = require('mongoose');
routes(app);
app.use(bodyParser.urlencoded({ 'extended': 'true' })); // parse application/x-www-form-urlencoded
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(morgan('dev')); // log every request to the console
app.use(bodyParser.json({ type: 'application/vnd.api+json' })); // parse application/vnd.api+json as json
app.use(bodyParser.json()); // parse application/json
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');

var server = app.listen(8000, function() {
    console.log('Escuchando en el puerto ', server.address().port);
});

mongoose.Promise = global.Promise;
var mongodbUri = 'mongodb://jalcara1:jalcara1123@ds139138.mlab.com:39138/realtimegps';
mongoose.connect(mongodbUri, function(err){
    if(err){
	console.error('Can\'t connect to MongoDB\n' + err);
	return err;
    }
    console.log("MongoDB connected");
});

