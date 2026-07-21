console.log("=================================================");
console.log(" 1. BOOLEAN & EQUALITY PARADOXES ");
console.log("=================================================");

// Array equals its own negation!
// Step-by-step: ![] becomes false -> [] == false -> "" == false -> 0 == 0 -> true
console.log("[] == ![]                    :", [] == ![]); // true

// Empty array equals false, but empty array is truthy!
console.log("[] == false                  :", [] == false); // true
console.log("Boolean([])                  :", Boolean([])); // true

// True is equal to '1', but not equal to 'true'
console.log("true == '1'                  :", true == '1'); // true  (1 == 1)
console.log("true == 'true'               :", true == 'true'); // false (1 == NaN)
console.log("false == '0'                 :", false == '0'); // true  (0 == 0)

// Deeply nested empty arrays coerce to 0
console.log("[[[[]]]] == 0                :", [[[[]]]] == 0); // true


console.log("\n=================================================");
console.log(" 2. ARRAY & OBJECT ALCHEMY ");
console.log("=================================================");

// Array addition results in string concatenation
console.log("[] + []                      :", JSON.stringify([] + [])); // ""
console.log("[1, 2] + [3, 4]              :", [1, 2] + [3, 4]); // "1,23,4"

// Object + Array vs Array + Object
console.log("([] + {})                    :", [] + {}); // "[object Object]"
console.log("({} + [])                    :", {} + []); // "[object Object]" (in expression context)

// Array subtraction tries numeric conversion
console.log("[5] - [3]                    :", [5] - [3]); // 2
console.log("[5] + [3]                    :", [5] + [3]); // "53"


console.log("\n=================================================");
console.log(" 3. MATH & FLOATING-POINT MADNESS ");
console.log("=================================================");

// Math.min is larger than Math.max when called with no arguments!
// Explanation: Math.min() defaults to Infinity, Math.max() defaults to -Infinity
console.log("Math.min() > Math.max()      :", Math.min() > Math.max()); // true

// NaN is the only value in JS not equal to itself
console.log("NaN === NaN                  :", NaN === NaN); // false

// IEEE 754 Floating point precision issues
console.log("0.1 + 0.2 === 0.3            :", 0.1 + 0.2 === 0.3); // false (0.30000000000000004)

// Number.MIN_VALUE is the smallest POSITIVE float, not negative!
console.log("Number.MIN_VALUE > 0         :", Number.MIN_VALUE > 0); // true

// Large integer precision loss
console.log("9999999999999999             :", 9999999999999999); // 10000000000000000


console.log("\n=================================================");
console.log(" 4. STRING & OPERATOR HACKS ");
console.log("=================================================");

// Unary plus coerces strings to numbers
console.log("+'42'                        :", +'42'); // 42
console.log("+true                        :", +true); // 1
console.log("+null                        :", +null); // 0
console.log("+undefined                   :", +undefined); // NaN

// Double negation hyphen trick (double minus converts second string to negative number)
console.log("'5' - - '3'                  :", "5" - - "3"); // 8
console.log("'5' + + '3'                  :", "5" + + "3"); // "53"
console.log("'5' + - '3'                  :", "5" + - "3"); // "5-3"

// The famous "baNaNa" string synthesis
console.log("'b' + 'a' + + 'a' + 'a'     :", 'b' + 'a' + + 'a' + 'a'); // "baNaNa"


console.log("\n=================================================");
console.log(" 5. JSFUCK: SPELLING WORDS FROM NOTHING ");
console.log("=================================================");
// JSFuck extracts characters by coercing objects/booleans/numbers to strings
// and pulling letters using index lookups [].

const letter_a = (![] + [])[1]; // "false"[1] -> "a"
const letter_e = (true + [])[3]; // "true"[3]  -> "e"
const letter_i = ([false] + undefined)[10]; // "falseundefined"[10] -> "i"
const letter_o = ({} + [])[1]; // "[object Object]"[1] -> "o"

console.log("Extracting 'a' from (![]+[])[1] :", letter_a);
console.log("Extracting 'e' from (true+[])[3]:", letter_e);
console.log("Extracting 'o' from (({})+[])[1]:", letter_o);
console.log("Spelling 'fail' from void    :", letter_a + letter_i + "l");


console.log("\n=================================================");
console.log(" 6. ARRAY SORTING & TYPE QUIRKS ");
console.log("=================================================");

// Default Array.prototype.sort converts elements to STRINGS before sorting!
console.log("[10, 1, 5, 2, 25].sort()     :", [10, 1, 5, 2, 25].sort()); // [1, 10, 2, 20, 5]

// typeof null is 'object' (a 30+ year old bug preserved for backwards compatibility)
console.log("typeof null                  :", typeof null); // "object"

// null vs undefined comparison
console.log("null == undefined            :", null == undefined); // true
console.log("null === undefined           :", null === undefined); // false
console.log("null > 0                     :", null > 0); // false
console.log("null == 0                    :", null == 0); // false
console.log("null >= 0                    :", null >= 0); // true (Wait... what?!)
