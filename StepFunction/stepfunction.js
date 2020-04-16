{
  "StartAt":"GetFileType",
  "States":{
    "GetFileType":{
      "Type": "Task",
      "Resource":"arn:aws:lambda:us-east-1:911904338222:function:getFileType",
      "TimeoutSeconds":3,
      "ResultPath":"$.results.fileType",
      "Next":"CheckFileType",
      "Catch":[
        {
        "ErrorEquals": ["States.ALl"],
          "Next": "QuitMain"
        }
      ]
    },
    "CheckFileType":{
      "Type": "Choice",
      "Choices":[
        {
          "Variable":"$.results.fileType",
          "StringEquals":"jpg",
          "Next":"ProcessFile"
        }
      ],
      "Default": "DeleteSourceFile"
    },
    "DeleteSourceFile": {
     "Type": "Task",
      "Resource":"arn:aws:lambda:us-east-1:911904338222:function:deleteFile",
      "TimeoutSeconds":10,
      "ResultPath":"$.results.deleteStatus",
      "OutputPath":"$.results",
      "End": true,
      "Catch":[
        {
        "ErrorEquals": ["States.ALl"],
          "Next": "QuitMain"
        }
      ]

    },
    "ProcessFile" :{
      "Type":"Parallel",
      "ResultPath":"$.results.images",
      "Next":"writeToDynamoDB",
      "Branches": [
        {
          "StartAt":"CopyToDestination",
          "States": {
            "CopyToDestination":{
                 "Type": "Task",
                  "Resource":"arn:aws:lambda:us-east-1:911904338222:function:copyfile",
                  "TimeoutSeconds":10,
                  "ResultPath":"$.image.original",
                  "OutputPath": "$.image",
                  "End":true,
                  "Retry":[
                    {
                    "ErrorEquals": ["States.TaskFailed","States.Timeout"],
                      "IntervalSeconds":5,
                      "MaxAttempts":2,
                      "BackoffRate":2.0
                  },
                    {
                    "ErrorEquals": ["States.ALL"],
                      "IntervalSeconds":2,
                      "MaxAttempts":2,
                      "BackoffRate":2.0
                  }
                  ],
                  "Catch":[
                    {
                    "ErrorEquals": ["States.ALl"],
                      "Next": "QuitParallelMain"
                    }
                  ]
            },
            "QuitParallelMain":{
              "Type":"Fail",
              "Error":"CopyError",
              "Cause":"An error occured while executing state Parallel machine"
            }
          }
        },
        {
          "StartAt":"RenameImage",
          "States": {
            "RenameImage":{
                  "Type": "Task",
                  "Resource":"arn:aws:lambda:us-east-1:911904338222:function:renameimage",
                  "TimeoutSeconds":3,
                  "ResultPath":"$.image.resized",
                  "OutputPath": "$.image",
                  "End":true,
                  "Retry":[
                    {
                    "ErrorEquals": ["States.TaskFailed","States.Timeout"],
                      "IntervalSeconds":5,
                      "MaxAttempts":2,
                      "BackoffRate":2.0
                  },
                    {
                    "ErrorEquals": ["States.ALL"],
                      "IntervalSeconds":2,
                      "MaxAttempts":2,
                      "BackoffRate":2.0
                  }
                  ],
                  "Catch":[
                    {
                    "ErrorEquals": ["States.ALl"],
                      "Next": "QuitParaMain"
                    }
                  ]
            },
              "QuitParaMain":{
              "Type":"Fail",
              "Error":"CopyError",
              "Cause":"An error occured while executing state Parallel machine"
            }
          }
        }
      ]
    },
    "writeToDynamoDB":{
                  "Type": "Task",
                  "Resource":"arn:aws:lambda:us-east-1:911904338222:function:writetoDynamoDb",
                  "TimeoutSeconds":3,
                  "ResultPath":"$.image.writeStaus",
                  "Next":"DeleteSourceFile",
                   "Catch":[
                    {
                    "ErrorEquals": ["States.ALl"],
                      "Next": "QuitMain"
                    }
                  ]

  },
    "QuitMain":{
      "Type":"Fail",
      "Error":"GenericError",
      "Cause":"An error occured while executing state machine"
  }

  }
}
