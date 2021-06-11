function chained(functions) {
  return function(res) {
    for (let i = 0; i < functions.length; i++) {
      res = functions[i](res);
    }
    return res;
  };
}
