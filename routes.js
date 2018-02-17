var controllers = require('./controllers');
module.exports = function (app) {
    app.get('/Hello', (req, res) => {
	res.send('Hello');
    });
    app.route('/login')
        .get(controllers.sendLogin);
    app.route('/sign')
        .get(controllers.sendSign);
    app.route('/mapa')
        .get(controllers.sendMapa);
};
