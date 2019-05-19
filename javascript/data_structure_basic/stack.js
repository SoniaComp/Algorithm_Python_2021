/*
https://helloworldjavascript.net/pages/282-data-structures.html
배열을 이용해서 간단하게 큐와 스택을 구현할 수 있다.
*/

class Stack{
  constructor(){
    this._arr = [];
  }

  push(item){
    this._arr.push(item);
  }

  pop(){
    return this._arr.pop();
  }

  peek(){
    return this._arr[this._arr.length-1];
  }
}

// python __init__ -> js constructor

/*
자바스크립트 배열 객체 내장함수
https://developer.mozilla.org/ko/docs/A_re-introduction_to_JavaScript
---
a.toString(), a.toLocaleString(), a.concat(item, ..), a.join(sep),
a.pop(), a.push(item, ..), a.reverse(), a.shift(), a.slice(start, end),
a.sort(cmpfn), a.splice(start, delcount, [item]..), a.unshift([item]..)
---
concat 해당 배열에 지정한 항목들을 추가한 새로운 배열을 돌려줍니다
pop 마지막 항목을 제거한 다음 돌려둡니다
push 마지막에 하나 이상의 항목을 추가합니다 (ar[ar.length]와 같이)
slice 배열의 일부분을 돌려줍니다
sort 비교에 사용할 함수를 따로 지정할 수 있습니다
splice 구역을 삭제하거나 항목을 추가해서 배열을 수정할 수 있게합니다
unshift 배열의 시작부분에 항목을 붙일 수 있습니다
*/