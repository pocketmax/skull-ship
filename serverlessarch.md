# serverless arch notes

## invoke a simple function

### amazon cloud
#### using vendor cli, invoke locally
#### using vendor cli, invoke remotely
#### using sls, invoke locally
#### using sls, invoke remotely

### google cloud platform
#### using vendor cli, invoke locally
#### using vendor cli, invoke remotely
#### using sls, invoke locally
#### using sls, invoke remotely

### azure cloud
#### using vendor cli, invoke locally
#### using vendor cli, invoke remotely
#### using sls, invoke locally
#### using sls, invoke remotely

### kubeless
#### using vendor cli, invoke locally
#### using vendor cli, invoke any kubernets based remote
#### using sls, invoke locally
#### using sls, invoke any kubernets based remote

### cloud flare
#### using vendor cli, invoke locally
#### using vendor cli, invoke remotely
#### using sls, invoke locally
#### using sls, invoke remotely

### fn
#### using vendor cli, invoke locally
#### using sls, invoke locally

### spotinst
#### using vendor cli, invoke locally
#### using vendor cli, invoke remotely
#### using sls, invoke locally
#### using sls, invoke remotely


## invoke function emits a named event
## running function receives event
## have a function emit an event buffer
## trigger a function with an http request
## run http trigger with static data
## emit http trigger with mocha
## functions in separate folders

## things to try to do with each vendor
* dependency injection for lambda functions?
* pass buffers between events?
* putting lambdas in separate folders?
* emitting more then one event?
* emitting events natively without custom event client?
* triggers lambda via HTTP call?
* passing stub event into function?
* passing stub event into http endpoint?
* run mocha unit testing on functions directly?
* run mocha e2e testing on HTTP endpoint?