var User = require('../models/user.js')
module.exports = function (app) {

  app.get('/user', app.isAuthenticated, function(req, res, next) {
    console.log('/user ', req.user)
    res.render('user')
  })
  app.post('/user', function(req, res) {
    res.send('posted user')
  })
  app.get('/signup', function(req, res, next) {
    res.render('signup')

  })
  app.post('/signup', signup);
}

function signup(req, res, next) {
  console.log(req.body.username)
  User.findOne({username: req.body.username}, function (err, user) {
   if(err) {
     throw new Error(err)
     res.end('error')
   }
   if(!err && user) {
     res.redirect('/signup')
   }
   if(!err && !user) {
     console.log('New user')
     var newUser = new User({
       username: req.body.username,
       password: req.body.password,
       email: req.body.email,
       profile: {
         profpic: 'pic'
       }
     })
     newUser.save()
     res.render('/user', {
       userinfo: {
         unsername: req.body.username,
        password: req.body.password
       }
     })
   }

 })

}

// User.findOne({username: username}, function (err, user) {
//   if(err) throw new Error(err)
//   if(!err && user) {
//     console.log(user)
//     var pic = user.prof.profpic || 'no prof pic'
//   }
//   return {
//     userinfo: {
//       profpic: null ,
//       username: null,
//       email: null,
//     }
//   }
//
// })
