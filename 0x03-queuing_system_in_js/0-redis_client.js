const redis = require('redis');

// creating a new client
const client = redis.createClient(); 
// By default redis.createClient() will use 127.0.0.1 and port 6379

// listen for the connect event to see whether we successfully connected to the redis-server
client.on('connect', () => console.log('Connected to Redis server'));

// listen for the error event to check if we failed to connect to the redis-server
client.on('error', (err) => console.error(`Failed to connect to Redis server: ${err.message}`));
