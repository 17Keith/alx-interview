#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const movieEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const names = [];
let people = [];


// getting the characters function, and if there is an error, show the status code.
const requestCharacters = async () => {
    await new Promise(resolve => request(movieEndPoint, (err, res, body) => {
        if (err || res.statusCode !== 200) {
            console.error('Error :', err, ' | statusCode:', res.statusCode);

        } else {
            const jsonBody = JSON.parse(body);
            people = jsonBody.characters;
            resolve();
        }
    }));
};

// Requesting names function, and if there is an error, show the status code.
const requestNames = async () => {
    if (people.length > 0) {
        for (const p of people) {
            await new Promise(resolve => request(p, (err, res, body) => {
                if (err || res.statusCode !== 200) {
                    console.error('Error :', err, ' | statusCode:', res.statusCode);
                } else {
                    const jsonBody = JSON.parse(body);
                    names.push(jsonBody.name);
                    resolve();
                }
            }));
        }
    } else {
        console.error('Error: No Characters.');
    }
};

// calling the function to print the results, (if all goes well.)

const getCharNames = async () => {
    await requestCharacters();
    await requestNames();

    for (const n of names) {
        if (n === names[names.length - 1]) {
            process.stdout.write(`${n}\n`);
        } else {
            process.stdout.write(`${n}\n`);
        }
    }
};

getCharNames();
