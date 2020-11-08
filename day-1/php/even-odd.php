<?php

// convert the given number to binary if it is even or
// hexadecimal if it is not

function evens_and_odds($n)
{
    if ($n % 2 == 0) {
        return decbin($n);
    } else {
        return dechex($n);
    }
}

$num = 10;
echo evens_and_odds($num);

echo "\n";

$num = 13;
echo evens_and_odds($num);
