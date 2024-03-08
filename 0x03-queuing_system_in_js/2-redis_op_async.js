const redis = require('redis');
const { promisify } = require('util');

// Creating a new client
const client = redis.createClient(); 
// By default redis.createClient() will use 127.0.0.1 and port 6379

// Promisify the client.get function
const asyncGet = promisify(client.get).bind(client);

// Listening for the connect event to confirm successful connection to the Redis server
client.on('connect', () => console.log('Connected to the Redis server'));

// Listening for the error event to check for failed connection attempts
client.on('error', (err) => console.error(`Failed to connect to the Redis server: ${err.message}`));

function setNewSchool(schoolName, value) {
    // Using redis.print to print "Reply: OK" to the console indicating successful value save
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
    // Using async/await to get the value of the schoolName
    console.log(await asyncGet(schoolName));
}

// Example usage of the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

