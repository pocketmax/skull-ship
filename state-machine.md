# state machine cluster
* client sends staged changes to one node to be confirmed by other nodes
* all nodes can only vote on one state change per state object
* DFSM: deterministic finite state machine. Only 1 transition from any allowed input
* NDFSM: non-deterministic finite state machine. Can have multiple transitions from one state to others
* saga: state machine for event sourcing

## Features
* reads get latest version or fail, guaranteed
* writes persist or fail, guaranteed

## uses
* visitor session state
* shopping cart state
* distributed lock
* message deduplication
* message ordering
* coordinating multiple routines passing data between each other i.e. one routine sending data that another routine needs
* change TTL i.e. do something after certain amount of inactivity
* block asset append services

## things to figure out
* custom error messages for specific errors
* nested conditions
* running checksum function
* how to reference dst and src data
* how to cover a lot of scenarios with little definition logic
* can generate a diagram of state machine showing labeled states and transitions

## REST API OPTION 1:
* POST /schema				create schema
- sends to all nodes

* GET /schema/{schemaID}	get schema
- if not found, get from other nodes

* POST /object/{objectID}	creates a new object from a schema (schema ID is required in request)
- sent to all nodes

* PATCH /object/{objectID}	update a state object (requires votes)
- sent to all nodes

* PUT /object/{objectID}	vote for state change to a state object
- sent to all nodes

* GET /object/{objectID}	get current object

## REST API OPTION 2:

* POST /machine/{machineId}	create a state schema
* GET /machine/{machineId}	get a state schema

* PATCH /machine/{machineId}/object/{objectId}/transition/{transaction}	vote transition to a different state
* PUT /machine/{machineId}/object/{objectId}/transition/{transaction}	transition to a different state
* note: if object doesn't exist, create it.

* GET /machine/{machineId}/object/{objectId}	get current objects state

## SCHEMAS - REDIS

### state machine schema
### state machine objects
### state machine objects


## SCHEMAS

### node table
```json
{
	"a node ID": {
		"lastSeen": "timestamp"
	}
}
```

### state schema
```json
{
	"id": "hash of schema",
	"schema": {
		"foo":"bar data goes here"
	}
}
```

### state object
```json
{
	"id": "primary key of object...UUID",
	"version": "int starting at 1",
	"state": {
		"foo":"bar data goes here"
	}
}
```

### pending change
```json
{
	"id": "id of pending change. hash(objectId + hash of the change)",
	"objectId": "id of object",
	"version": "version of object",
	"schema": {
		"asdf": "schema used to validate state changes"
	},
	"state": {
		"object":"data of change goes here"
	}
}
```

## schema language examples

### scenario: versioned lock
### scenario: timed lock
### scenario: tally sheet

### scenario: block building
```yaml
states:
	genesis:
		rootBlock:
			$vars:
				firstHalf: substr(0,64)
			matches: "${src.firstHalf}${src.firstHalf}"
			regex: !!pcre /^[a-f0-9]{128}$/	// must match regex
	build:
		previousBlock:
			required: true,
			type: 'string'	// must be string
			regex: !!pcre /^[a-f0-9]{64}$/	// must match regex
			src: currentBlock	// must match source
		currentBlock: 
			required: true,
			type: 'string'	// must be string
			regex: !!pcre /^[a-f0-9]{64}$/	// must match regex
transitions:
	init:
		$dst:
		
		$src:
		
init:	# transition name
	$dst: null	# null indicates this transition create the object initially
	$src:
next:
	$dst:	# array indicates OR logic. an object indicates AND logic
	- rootBlock:
		$vars:
			firstHalf: substr(0,64)
		matches: "${src.firstHalf}${src.firstHalf}"
		regex: !!pcre /^[a-f0-9]{128}$/	// must match regex
	- previousBlock:
		required: true,
		type: 'string'	// must be string
		regex: !!pcre /^[a-f0-9]{64}$/	// must match regex
		src: currentBlock	// must match source
	  currentBlock: 
		required: true,
		type: 'string'	// must be string
		regex: !!pcre /^[a-f0-9]{64}$/	// must match regex
	$src:
```











