console.log("Lambda1:: Starteds");
const AWS=require("aws-sdk");
AWS.config.update({region:"us-east-1"});
const stepFunctions = new AWS.StepFunctions();


exports.handler = async (event) => {
    console.log(JSON.stringify(event));
    let fileProcessed = event.Records.map( async (record)=>{
        let temp={
            stateMachineArn:process.env.STATE_MACHINE_ARN,
            input:JSON.stringify(record)
        }
        let data = await stepFunctions.startExecution(temp).promise();
        console.log("lambda1::",data);
        return data;
    });

    let results = await Promise.all(fileProcessed);
    return results;
};
