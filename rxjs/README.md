Observable: represents the idea of an invokable collection of future values or events.
Observer: is a collection of callbacks that knows how to listen to values delivered by the Observable.
Subscription: represents the execution of an Observable, is primarily useful for cancelling the execution.
Operators: are pure functions that enable a functional programming style of dealing with collections with operations like map, filter, concat, reduce, etc.
Subject: is the equivalent to an EventEmitter, and the only way of multicasting a value or event to multiple Observers.
Schedulers: are centralized dispatchers to control concurrency, allowing us to coordinate when computation happens on e.g. setTimeout or requestAnimationFrame or others.

Observables - represents 
Operators - transform way data in handled, used and looks like

``
Rx.Observable
.fromEvent(button,'click')
.throttleTime(1000)				// operator
.subscribe(
  (event)=>console.log('Clicked')
);
``

Observable - wrapper around some async data source. can also uses sync data
Observer - to execute code when ever we see a new val or an error or the observable says it's done
Subscription - connects observer to observable. Observer makes next(), error() and complete() when subscribed for Observable to execute
