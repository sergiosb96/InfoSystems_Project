const amqp = require("amqplib");

const msg = {number: process.argv[2]}
connect();
async function connect() {

    try {
        const connection = await amqp.connect("amqp://192.168.90.90:5672");
        const channel = await connection.createChannel();
        const result = await channel.assertQueue("jobs");
        channel.sendToQueue("jobs", Buffer.from(JSON.stringify(msg)));
        console.log(`Job sent succesfully ${msg.number}`);

    }
    catch (ex){
        console.error(ex)
    }
}