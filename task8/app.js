const express = require('express');

const app = express();

const weatherroutes = require('./weather');
 
app.use('/weather', weatherroutes);

app.use((req, res, next) =>{
  const error = new Error('weather data not found');
  error.status= 404;
  next(error) 
});

app.use((error, req, res, next) => {
  res.status(error.status || 400);

  res.json({
    error: {
          status: error.status,
           message: error.message
          }
  });
});
 module.exports = app;