let dict =
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&\"";
function encrypt(text) {
    let first = "";
    let reg = /[A-Z]/;

    text.split("").forEach((char, i) => {
        let loc_first = dict.indexOf(char);
        if (loc_first == -1) {
            throw new Error();
        } else {
            if (i % 2 != 0) {
                first += char.toUpperCase();
            } else {
                first += char;
            }
        }
    });
    console.log(first);
    let first_length = first.length;
    let second = first[1];
    for (var i = 1; i < first_length; i++) {
        let loc_second = dict.indexOf(first[i - 1]) - dict.indexOf(first[i]);
        if (loc_second < 0) {
            second += dict[77 + loc_second];
        } else {
            second += dict[loc_second];
        }
    }
    second[0] = dict[77 - dict.indexOf(second[0])];
    return second;
}
function decrypt(encryptedText) {}
