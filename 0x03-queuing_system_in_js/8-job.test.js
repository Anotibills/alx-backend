const createPushNotificationsJobs = require('./8-job');
const kue = require('kue');
const { expect } = require('chai');

const queue = kue.createQueue(); // Creating a Kue queue instance

describe('createPushNotificationsJobs', () => {
    before(() => queue.testMode.enter()); // Entering test mode before running tests
    afterEach(() => queue.testMode.clear()); // Clearing the test mode after each test case
    after(() => queue.testMode.exit()); // Exiting test mode after all tests are completed

    it('throws an error if jobs is not an array', () => {
        const job = {
            phoneNumber: '4153518780',
            message: 'Verification code: 1234',
        };
        // Testing if an error is thrown when jobs is not an array
        expect(() => createPushNotificationsJobs(job, queue)).to.throw(Error, 'Jobs is not an array');
    });

    it('creates two new jobs in the queue', () => {
        // Sample jobs data
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'Verification code: 1234',
            },
            {
                phoneNumber: '4153518781',
                message: 'Verification code: 4562',
            },
        ];
        // Creating jobs using the function under test
        createPushNotificationsJobs(jobs, queue);
        // Verifying that two jobs are added to the queue
        expect(queue.testMode.jobs.length).to.equal(2);

        // Checking the details of the first job created
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[0].data).to.deep.equal({
            phoneNumber: '4153518780',
            message: 'Verification code: 1234',
        });

        // Checking the details of the second job created
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.deep.equal({
            phoneNumber: '4153518781',
            message: 'Verification code: 4562',
        });
    });
});

