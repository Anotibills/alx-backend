const kue = require('kue'); // Importing the Kue module

const queue = kue.createQueue(); // Creating a new Kue queue instance

const jobObj = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
};

const queueName = 'push_notification_code'; // Defining the queue name

const job = queue.create(queueName, jobObj).save(); // Creating and saving a job to the queue

// Listening for various job events
job.on('enqueue', () => console.log(`Notification job created: ${job.id}`)) // When the job is enqueued
    .on('complete', () => console.log('Notification job completed')) // When the job is completed
    .on('failed', () => console.log('Notification job failed')); // When the job fails

