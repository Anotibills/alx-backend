import kue from 'kue'; // Importing the Kue module

// Blacklisted phone numbers
const blacklistedNum = ['4153518780', '4153518781'];

// Function to send notifications
function sendNotification(phoneNumber, message, job, done) {
    const total = 100; // Total progress value

    job.progress(0, total); // Setting initial progress

    // Check if phone number is blacklisted
    if (blacklistedNum.includes(phoneNumber)) {
        done(Error(`Phone number ${phoneNumber} is blacklisted`)); // Mark job as failed and pass error message
        return;
    }

    job.progress(50, total); // Updating progress

    // Sending notification
    console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
    );

    done(); // Mark job as completed
}

const queue = kue.createQueue(); // Creating a Kue queue instance
const queueName = 'push_notification_code_2'; // Queue name

// Processing jobs from the specified queue with concurrency 2
queue.process(queueName, 2, (job, done) => {
    const { phoneNumber, message } = job.data; // Extracting data from job
    sendNotification(phoneNumber, message, job, done); // Calling the sendNotification function
});

