class Queue{
  constructor(){
    this._arr = [];
  }

  enqueue(item){
    this._arr.push(item);
  }

  dequeue(){
    return this._arr.shift();
  }
  // shift() 메서드는 배열에서 첫 번째 요소를 제거하고, 제거된 요소를 반환합니다. 이 메서드는 배열의 길이를 변하게 합니다
  // https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/shift
}