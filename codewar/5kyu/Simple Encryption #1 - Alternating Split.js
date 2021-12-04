function encrypt(text, n) {
    if (text === null) return null;
    if (text === "") return "";
    let result = text;
    while (n > 0) {
        result = encrypt_unit(result);
        n--;
    }
    return result;
}

function decrypt(encryptedText, n) {
    if (encryptedText === null) return null;
    if (encryptedText === "") return "";
    let result = encryptedText;
    while (n > 0) {
        result = decrypt_unit(result);
        n--;
    }
    return result;
}
function encrypt_unit(text) {
    let first = "";
    let second = "";
    text.split("").forEach((char, i) => {
        if (i % 2 == 0) {
            first += char;
        } else {
            second += char;
        }
    });
    return second + first;
}
function decrypt_unit(text) {
    let avg = text.length / 2;
    let first = text.slice(0, avg);
    let second = text.slice(avg);
    let result = "";
    for (i in second) {
        if (first[i] != undefined) {
            result += second[i];
            result += first[i];
        } else {
            result += second[i];
        }
    }
    return result;
}
