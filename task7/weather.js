const express = require('express');
const router = express.Router();


router.get('/', (req, res, next ) => {
    res.status(400).json({
        status: 400,
        message: 'Bad request'
    });
}); 

router.get('/city', (req, res, next) =>{
    res.status(400).json({
        status: 400,
        message: 'Bad request'
    
    });
});

    router.get('/city/:city_name', (req, res, next) =>{
    
        const c = req.params.city_name;
            
        const request = require("request")

        const dotenv = require("dotenv").config()

        const url = `http://api.openweathermap.org/data/2.5/weather?q=${c}&units=metric&appid=${process.env.API_KEY}`

        request(url , function (error, response, body) {
            if (error) 
            {res.status(404).json({
                status: 404,
                message: 'weather data not found'
            
            });
            }
             else
               { res.status(200)
                var data = JSON.parse(body)
                res.send(data)
               }
            });

    })
    
module.exports = router;