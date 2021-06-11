function isValidWalk(walk) {
  if (walk.length() > 10) {
    return false;
  } else {
    let map = {
      n_s: 0,
      w_e: 0
    };
    walk.forEach((item, i) => {
      if (item == "n") {
        map.n_s + 1;
      } else if (item == "s") {
        map.n_s - 1;
      } else if (item == "w") {
        map.w_e - 1;
      } else if (item == "e") {
        map.w_e - 1;
      }
    });
    if (map.n_s == 0 && map.w_e == 0) {
      return true;
    } else {
      return false;
    }
  }
}
