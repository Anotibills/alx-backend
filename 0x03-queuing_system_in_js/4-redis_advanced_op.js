const redis = require('redis');

const client = redis.createClient();
// Creating a new Redis client

// Listening for errors when connecting to the Redis server
client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

// Listening for successful connection to the Redis server
client.on('connect', () => console.log('Connected to the Redis server'));

const KEY = 'HolbertonSchools'; // Defining the key for the Redis hash set

const keys = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris']; // Array of keys
const values = [50, 80, 20, 20, 40, 2]; // Array of corresponding values

// Looping through the keys array and setting key-value pairs in the Redis hash set
keys.forEach((key, index) => {
    client.hset(KEY, key, values[index], redis.print);
});

// Retrieving all key-value pairs from the Redis hash set
client.hgetall(KEY, (err, value) => {
    console.log(value); // Logging the retrieved key-value pairs
});

