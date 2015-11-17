var passport = require('passport');
var User = require('../app/models/user.js')
var userSemilla = require('../app/models/user.semilla.js')('ElDon', 'LaContrasena', 'mmaammbbuu@gmail.com')
// userSemilla('ElDon', 'LaContrasena', 'mmaammbbuu@gmail.com')

var strategies = require('./strategies.js')
strategies.forEach(function(s) { passport.use(s.name, s);})
passport.serializeUser(function(user, done) {
  done(null, user.id);
});
passport.deserializeUser(function(id, done) {
  User.findById(id, function(err, user) {
    done(err, user);
  });
});

module.exports = function (app) {
  app.login = __login
  app.isAuthenticated = __isAuthenticated
  app.logout = __logout
}

function __login(req, res, next) {
  passport.authenticate(req.body.authtype, {
    session: true
  }, function(err, user) {
    if (err) { return next(err); }
    if (!user) { return res.redirect('/login'); }
    req.logIn(user, function(err) {
      if(err) {return next(err)}
      console.log('Authorized user ', user)
      res.redirect('/user')
    });
  })(req, res, next);
}

function __isAuthenticated(req, res, next) {
  console.log('User authed? ', req.isAuthenticated())
  if(!req.isAuthenticated()) {
    res.redirect('/login')
    return
  }
  next()
}

function __logout(req, res) {
  console.log('__logout ', req.username)
  req.logout()
  res.redirect('/')
}
