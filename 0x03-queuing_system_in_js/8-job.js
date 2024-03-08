import kue from 'kue'; // Importing the Kue module

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
    // Check if jobs is an array
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }

    // For each job in jobs array
    jobs.forEach((jobData) => {
        // Create a new job in the queue push_notification_code_3
        const job = queue.create('push_notification_code_3', jobData).save((err) => {
            if (err) {
                console.error(`Error creating job: ${err}`);
            } else {
                console.log(`Notification job created: ${job.id}`);
            }
        });

        // Listen for job completion
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        // Listen for job failure
        job.on('failed', (err) => {
            console.error(`Notification job ${job.id} failed: ${err}`);
        });

        // Listen for job progress
        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs; // Exporting the function

