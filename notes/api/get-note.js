/*

* Route: GET /note/n/{note_id}

*/


const AWS= require("aws-sdk");
AWS.config.update({region: 'us-east-1'});
const util=require("./util.js")
const _=require("underscore");
const db=new AWS.DynamoDB.DocumentClient();
const tableName =  process.env.NOTES_TABLE;

module.exports.handler = async (event) => {
    try {
        let note_id = decodeURIComponent(event.pathParameters.note_id);

        let params={
            TableName: tableName,
            IndexName: "note_id-index",
            KeyConditionExpression: "note_id = :note_id",
            ExpressionAttributeValues: {
                ":note_id": note_id
            },
            Limit: 1
        };

        let data = await db.query(params).promise();
        console.log(JSON.stringify(data.Items))
        if(!_.isEmpty(data.Items)){
            return {
                statusCode: 200,
                headers: util.getResponseHeaders(),
                body: JSON.stringify(data.Items[0])
            }

        }else{
            return {
                statusCode: 404,
                headers: util.getResponseHeaders(),
                body: JSON.stringify("Item NOT Present/Found")
            }
        }


        

    }catch (err){
        console.log("Error:: get-node.js");
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
