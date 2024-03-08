const redis = require('redis');

const subscriber = redis.createClient();
// Creating a new Redis client for subscribing

// Listening for errors when connecting to the Redis server
subscriber.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

// Listening for successful connection to the Redis server
subscriber.on('connect', () => console.log('Connected to the Redis server'));

subscriber.subscribe('holberton school channel'); // Subscribing to a Redis channel

// Listening for messages published to the subscribed channel
subscriber.on('message', (channel, message) => {
    if (channel === 'holberton school channel') console.log(message); // Logging the received message
    if (message === 'KILL_SERVER') { // Check if the message is to kill the server
        subscriber.unsubscribe(); // Unsubscribing from the channel
        subscriber.quit(); // Quitting the Redis client
    }
});

