#!/usr/bin/node
exports.esrever = function (list) {
    for (let i = 0; i < (list.length) / 2; i++) {
        let a = list[i];
        list[i] = list[list.length - i - 1];
        list[list.length - i - 1] = a;
    }
    return (list);
}
