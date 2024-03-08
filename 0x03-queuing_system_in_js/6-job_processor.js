import kue from 'kue'; // Importing the Kue module

const queue = kue.createQueue(); // Creating a new Kue queue instance

// Function to send notifications
function sendNotification(phoneNumber, message) {
    console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
    );
}

const queueName = 'push_notification_code'; // Defining the queue name

// Processing jobs from the specified queue
queue.process(queueName, (job, done) => {
    // Extracting phoneNumber and message from job data
    const { phoneNumber, message } = job.data;
    // Calling the sendNotification function with extracted data
    sendNotification(phoneNumber, message);
    done(); // Indicating that the job processing is complete
});

