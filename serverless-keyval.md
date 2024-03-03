# serverless architecture

provider aka publisher = where lambdas get their messages
* HTTP API GATEWAY
* SMTP
* CHRON SCHEDULER
* QUEUE - 1:1 msg to instance ratio
* PUBSUB CHANNEL - 1:m msg to instance ratio


## connecting lambda to infrastructure
INGRESS - how the lambda gets it's input
LAMBDA
EGRESS - how the lambda sends it's output


things to figure out
1. how to call other lambdas?
2. how to handle instance state?
3. should state of transaction be handled as well i.e. end to end data from http request/response round trip?
4. how to pass incoming stateful http2 requests from API gateway to lambda pointing to it
5. how to glue all these lambdas together?
6. how to handle a state object where all the lamdas update
7. how to orchestrate lambas execution? contract based like apache airflow or independent like AWS
8. how to prevent no two lambda executions with the same args? maybe specify a unique key field to prevent dupe execution
9. how to give lambda domain provider credentials dynamicaly on startup? have host server give them on lambda deployment
10. how to scale instances
11. how to guarantee instances are stateless? from in the container, detect when script finishes then restart it

## example use cases

### treedb - visitor creating a keyval
* blocking/end to end transaction
* uses persistent storage
* stateless
* init input comes from outside (http request)
* final output returns to outside (http response)
* fast/frequent calls

1. httpPOST(req)
2. writeKeyval(key, val)
3. storeInsert(key, val)

### blockhub - visitor emits blob to chain for commit via web socket
* non-blocking/emit transaction
* uses persistent storage
* stateful lambda - block builder
* init input comes from outside (websock request)
* no final output
* fast/frequent calls

1. websock(payload)    payload has blob and chainId in it
2. hopper(blob, chainId)
3. fetchLastBlock(chainId): blockId
4. blockStoreInsert(block)
5. blockBuilder(prevBlockId, blockId)
6. blobStoreInsert(blob)

### treedb - internal process sorts children under a keyval
* uses persistent storage
* stateful lambda - block builder
* init input comes from inside
* final output changes persistent storage
* slow/infrequent/long running calls
* no two instances can run with the same arguments

1. sortKey(key)
2. sortKey(key,page1,limit)
  2a. getKey(key,page3,limit)
  2b. sort(list, DESC)
  2c. writeKey(key, list)
2. sortKey(key,page2,limit)
  2a. getKey(key,page3,limit)
  2b. sort(list, DESC)
  2c. writeKey(key, list)
2. sortKey(key,page3,limit)
  2a. getKey(key,page3,limit)
  2b. sort(list, DESC)
  2c. writeKey(key, list)
  
### blockhub - walker traverses a block chain to populate a projection
* self looping with different arguments
* each execution would end after next execution is called i.e. bottomless middleware
* uses persistent storage i.e. projection
* exclusive write lock on projection
* stateless lambda
* init input comes from inside or outside via http handler
* final output is read from persistent storage
* slow/infrequent/long running calls
* many instances of the same lambda with different arguments
* final execution returns collected data

1. walk(blockId)
2. readBlock(blockId)
3. readBlock(blockId)

### blockhub - walker traverses a block chain to populate a projection with splits
* final results from each process is merged together and returned
1. walk(blockId)
  1a. fetchIndexOffsets(4) returns the 4 blockIds that are evently split across the chain
  1b. walk(blockId1)
  1b. walk(blockId2)
  1b. walk(blockId3)
  1b. walk(blockId4)
  1c. mergeResults(results1,results2,results3,results4)  
