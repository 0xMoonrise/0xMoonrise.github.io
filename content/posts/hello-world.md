+++
title = 'Hello World'
date = 2024-03-31T15:04:27-07:00
draft = false
test = 'a'
+++
hello world

this is a test

test

```python
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1







#This is a fkinc comment
```

This is oter text

```bash
#!/bin/bash
echo "hello world"
```

this another text just for fcking fun

```perl
#!/usr/local/bin/perl
#
# composite series of images over a background image
#

if ($#ARGV != 4) {
 print "usage: compem bg.rgb inbase outbase startNum stopNum\n";
 exit;
}

$bg = $ARGV[0];
$inbase = $ARGV[1];
$outbase = $ARGV[2];
$start = $ARGV[3];
$stop = $ARGV[4];

# for each image
for ($i=$start; $i <= $stop; $i++) {

    # pad numbers
    $num = $i;
    if($i<10) { $num = "00$i"; }
    elsif($i<100) { $num = "0$i"; }

    # call unix command "over"
    $cmd = "over $bg $inbase.$num $outbase.$num 0 0";
    print $cmd."\n";
    if(system($cmd)) { print "over failed\n"; }
}
```
