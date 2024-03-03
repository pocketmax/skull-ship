'use strict';
let Rx = require('rxjs/Rx');

// TODO with an array of values, delay each item by a duration

let data = [
	['a'],
	['b'],
	['c'],
	['d'],
	['e'],
	['f'],
	['g'],
	['h'],
	['i'],
	['j'],
	['k'],
	['l'],
	['m'],
	['n'],
	['o'],
	['p'],
	['q'],
	['r'],
	['s'],
	['t'],
	['u'],
	['v'],
	['w'],
	['x'],
	['y'],
	['z']
];


Rx.Observable.create(obs => {

	let i = 0;
	let y = 0;
	let myFunc = ()=>{
		if(i>=data.length) {
			i=0;
			y++;
		}
		let cnt = Math.floor(Math.random() * 500);

 		setTimeout(()=>{
			obs.next(data[i] + y);
			i++;
			myFunc(cnt);
		},cnt);
	};
	myFunc();
})
.bufferCount(4,1)
// .defaultIfEmpty()
.bufferTime(1000)
.subscribe(x => console.log(x));
//let result = observable;
//.map(x => parseInt(x));
//.filter(x => !isNaN(x))
//.reduce((x,y)=>x+y);

//result