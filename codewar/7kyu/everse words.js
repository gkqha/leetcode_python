function reverseWords(str) {
  let result = "";
  let list = "";
  for (i of str) {
    if (i != " ") {
      list += i;
    } else {
      result += list
        .split("")
        .reverse()
        .join("");
      list = "";
      result += " ";
    }
  }
  result += list
    .split("")
    .reverse()
    .join("");
  return result;
}
