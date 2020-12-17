function characterMapping(str) {
  let value = 0;
  let objMap = {};
  let sol = [];
  for (ch of [...str]) {
    if (objMap[ch] === undefined) {
      if (value === 0) {
        sol.push(value);
        objMap[ch] = value;
        value++;
      } else {
        if (value === 0) {
          value++;
          objMap[ch] = value;
        } else {
          objMap[ch] = value;
          value++;
        }
        sol.push(objMap[ch]);
      }
    } else {
      sol.push(objMap[ch]);
    }
  }
  return sol;
}
