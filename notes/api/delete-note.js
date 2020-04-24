/*

* Route: POST /note/t/{timestamp}

*/


const AWS= require("aws-sdk");
AWS.config.update({region: 'us-east-1'});
const util=require("./util.js")

const db=new AWS.DynamoDB.DocumentClient();
const tableName =  process.env.NOTES_TABLE;

module.exports.handler = async (event) => {
    try {
        let timestamp = decodeURIComponent(event.pathParameters.timestamp);
        
        let user_id= util.getUserId(event.headers);
        console.log(typeof(timestamp),"---",user_id,"----",tableName);
        let params= {
            TableName: tableName,
            Key: {
                user_id: user_id,
                timestamp: parseInt(timestamp)
            }

        }

        await db.delete(params).promise();
        return {
            statusCode: 200,
            headers: util.getResponseHeaders(),
        }

    }catch (err){
        console.log("Error:: delete-node.js");
        return {
            statusCode: err.statusCode ? err.statusCode : 500,
            headers: util.getResponseHeaders(),
            body: JSON.stringify({
                error: err.name ? err.name : "Exception",
                message: err.message ? err.message : "Unknown Error"
            })

        }
    }

}
