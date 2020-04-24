/*

* Route: PATCH /note

*/


const AWS= require("aws-sdk");
AWS.config.update({region: 'us-east-1'});
const util=require("./util.js");
const moment = require('moment');
const uuid =  require('uuid/v4');

const db=new AWS.DynamoDB.DocumentClient();
const tableName =  process.env.NOTES_TABLE;

module.exports.handler = async (event) => {
    try {
        
        let item =  JSON.parse(event.body).Item;
        item.user_id= util.getUserId(event.headers);
        item.user_name= util.getUserName(event.headers);
        item.expires=moment().add(90,'days').unix();

        let data = await db.put({
            TableName: tableName,
            Item: item,
            ConditionExpression: '#t = :t',
            ExpressionAttributeNames: {
                '#t': 'timestamp'
            },
            ExpressionAttributeValues: {
                ':t': item.timestamp
            }
        }).promise();
        




        return {
            statusCode: 200,
            header: util.getResponseHeaders(),
            body: JSON.stringify(item)
        }

    }catch (err){
        console.log("Error:: update-node.js");
        return {
            statusCode: err.statusCode ? err.statusCode : 500,
            header: util.getResponseHeaders(),
            body: JSON.stringify({
                error: err.name ? err.name : "Exception",
                message: err.message ? err.message : "Unknown Error"
            })

        }
    }

}
