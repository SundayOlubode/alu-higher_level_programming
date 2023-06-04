#!/usr/bin/node

const {argv} = process
let numArg = Number(argv[2])
let result;

function recr(num){
	if (!num || num === 1) return 1

	return num * recr(num - 1)
}

result = recr(numArg)
console.log(result)
