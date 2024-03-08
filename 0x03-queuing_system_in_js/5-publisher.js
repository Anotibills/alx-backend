const redis = require('redis'); // Importing the Redis module

const publisher = redis.createClient(); // Creating a new Redis client for publishing

// Listening for errors when connecting to the Redis server
publisher.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

// Listening for successful connection to the Redis server
publisher.on('connect', () => console.log('Connected to the Redis server'));

function publishMessage(message, time) {
    // Setting a timeout to simulate delayed publishing
    setTimeout(() => {
        console.log(`About to send ${message}`); // Logging the message to be sent
        publisher.publish('holberton school channel', message); // Publishing the message to the specified channel
    }, time); // Delaying the execution according to the specified time
}

// Calling the function to publish messages with specified delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300); // Sending a message to kill the server
publishMessage('Holberton Student #3 starts course', 400);

