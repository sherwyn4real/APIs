const express = require('express');
const router = express.Router();


router.get('/', (req, res, next ) => {
    res.status(400).json({
        status: 400,
        message: 'Bad request'
    });
}); 

router.get('/country', (req, res, next) =>{
    res.status(400).json({
        status: 400,
        message: 'Bad request'
    
    });
});

    router.get('/country/code', (req, res, next) =>{
        res.status(400).json({
            status: 400,
            message: 'Bad request'
        
        });
    });

    router.get('/country/code/:country_code', (req, res, next) =>{
        const c = req.params.country_code;
            
        
    const request = require('request');
    const dotenv = require("dotenv").config()
    
    const options = {
    method: 'GET',
     url: 'https://rapidapi.p.rapidapi.com/country/code',
    qs: {code: c },
    headers: {
    'x-rapidapi-key': process.env.API_KEY,
    'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
    useQueryString: true
                }
    }

    request.get(options, function (error, response, body) {
        
     

        if(error)
       { 
           res.status(404).json({
           status: 404,
           message: 'No records found'
                   })
       }
         else{
        res.status(200)
        const data = JSON.parse(body)
        res.send(data)
       }
   
       });

    });
    
    module.exports = router;