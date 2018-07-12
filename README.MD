## A simple tool to make creating AWS Users simpler

## Requirements
You must have an environment variable set for `GIT_TOKEN` that is equal to an OAUTH token capable of cloning this (or your own hosted) repo in order for the pipeline to work. 

For more info on setting up an OAUTH token please visit the following [page](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).

NOTE: if you are using `OSX` you should `brew install watch` for this script to work properly


## Directions to Launch the User Account Pipeline
To launch the pipeline stack
` sh pipeline.sh`
To update the pipeline stack
`sh pipeline.sh update`
To delete the pipeline stack
`sh pipeline.sh delete`

## Acceptance Criteria:
- The user creation method must have unit tests
- The user creation method must be able to Create users from a YAML file
- The user creation method must be able to assign users to groups

## TODO:
- refactor into IAM class to reduce code duplication
- consume yaml file
- handle yaml file
- decouple tests