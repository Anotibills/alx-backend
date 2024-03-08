import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

// Utility functions =================================================

// Function to update seat reservation in Redis
function updateSeatReservation(seats) {
  client.set(seatsKey, seats);
}

// Function to retrieve the current available seats from Redis
async function getCurrentAvailableSeats() {
  const availableSeats = await getAsync(seatsKey);
  return availableSeats;
}

// Redis connection ===================================================

// Creating a Redis client
const client = redis.createClient();
// Promisify the Redis get method
const getAsync = promisify(client.get).bind(client);
// Key to store the available seats in Redis
const seatsKey = 'available_seats';
// Flag to indicate whether seat reservation is enabled
let reservationEnabled;

// Event handlers for Redis client
client.on('error', (error) => {
  console.log(`Error with Redis connection: ${error.message}`);
});

client.on('connect', () => {
  console.log('Connected to Redis server');
  // Initialize the available seats and enable seat reservation
  updateSeatReservation(50);
  reservationEnabled = true;
});

// Kue setup ==========================================================

// Create a Kue queue
const queue = kue.createQueue();
// Name of the queue for seat reservation
const queueName = 'reserve_seat';

// Express setup ======================================================

// Create an Express application
const app = express();
// Port for the Express server
const port = 1245;

// Start listening on the specified port
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

// Route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled === false) {
    res.json({ status: 'Seat reservations are currently unavailable' });
    return;
  }

  const jobData = {}; // Specify the job data format here if needed

  // Create a new job in the queue for seat reservation
  const job = queue.create(queueName, jobData).save((err) => {
    if (err) {
      res.json({ status: 'Seat reservation failed' });
    } else {
      res.json({ status: 'Seat reservation in progress' });
    }
  });

  // Event listeners for job completion and failure
  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process the seat reservation queue
app.get('/process', async (req, res) => {
  // Process the seat reservation queue
  queue.process(queueName, async (job, done) => {
    let availableSeats = await getCurrentAvailableSeats();

    if (availableSeats <= 0) {
      done(Error('Not enough seats available'));
    }

    availableSeats = Number(availableSeats) - 1;

    // Update the seat reservation in Redis
    updateSeatReservation(availableSeats);

    if (availableSeats <= 0) {
      reservationEnabled = false;
    }

    done();
  });

  res.json({ status: 'Queue processing' });
});
