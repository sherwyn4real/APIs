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

    
    router.get('/country/search', (req, res, next) =>{
       
        if(req.query.searchText == '' || req.query.searchText == undefined)
        {
            res.status(400).json({
            status: 400,
            message: 'Bad request'
        
        });
        return
        }
       
        var c = req.query.searchText;
         
        let u = ''
        let x = ''

        if(c.length<=3)
            {
         u = 'https://rapidapi.p.rapidapi.com/country/code'
        x = 'code'
            }
            else
         {
             u = 'https://rapidapi.p.rapidapi.com/country'
         }
    const request = require('request');
    const dotenv = require("dotenv").config()
    
if(x == 'code')
{
    const options = {
    method: 'GET',
     url: u,
    qs: {code : c },
    headers: {
    'x-rapidapi-key': process.env.API_KEY,
    'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
    useQueryString: true
                }
    }

    request(options, function (error, response, body) {
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
        console.log(data)
       }
   
       });
    }

    else{

        const options = {
            method: 'GET',
             url: u,
            qs: {name : c },
            headers: {
            'x-rapidapi-key': process.env.API_KEY,
            'x-rapidapi-host': 'covid-19-data.p.rapidapi.com',
            useQueryString: true
                        }
            }
        
            request(options, function (error, response, body) {
               
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

    }

    });

    
    module.exports = router;