var express = require('express');
var app = express()
var __testPort = 3001
app.isAuthenticated = __isAuthenticated


app.get('/', app.isAuthenticated, function (req, res, next) {
  res.end('end')

})

app.listen(__testPort, function () {
  console.log('TEST app listenign on port' + __testPort)

})

function __isAuthenticated(req, res, next) {
  console.log('__isAuthed constructed and called')
  next()

}
