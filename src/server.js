const express = require('express');
const app = express();

const path = require('path'); // Management Routes files and directories
const mongoose = require('mongoose'); // Connect to MongoDB
const passport = require('passport'); // Configure autentication form
const flash = require('connect-flash');
const morgan = require('morgan'); // How to we define the petitions from the web
const cookieParser = require('cookie-parser'); // Management browser cookies
const bodyParser = require('body-parser'); // Transform the data from the web (JSON)
const session = require('express-session');

const urlDB = 'mongodb://jalcara1:1234567890@ds139138.mlab.com:39138/realtimegps'

mongoose.connect(urlDB);

require('./config/passport')(passport);

// Settings
app.set('port', process.env.PORT || 3000) 
app.set('views', path.join(__dirname, 'views')); //Join views directory with this
app.set('view engine', 'ejs');

// Middlewares
app.use(morgan('dev')); // View request logs in console and 
app.use(cookieParser()); // Use and interpret cookies
app.use(bodyParser.urlencoded({extended: false})); // Interpret request from the url, and not process media
app.use(session({ // Management express sessions
    secret: 'thisisasecretsentence',
    resave: false,  // Don't save in specific time
    saveUninitialized: false
}))
app.use(passport.initialize());
app.use(passport.session());
app.use(flash()); //Transfer data between HTMLs

// Routes
//require('./app/routes')(app, passport);
require('./app/routes.js')(app, passport);

// Static Files
app.use(express.static(path.join(__dirname, 'public'))); // CSS, Images, Sources, Static Files

app.listen(app.get('port'), () => {
    console.log('server on port', app.get('port'));
});
