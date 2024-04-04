+++
title = 'How To Test'
date = 2024-03-31T15:04:27-07:00
draft = false
tags = ['xss', 'lfi', 'rce', 'Atopic']
categories = ['Web Pentesting']
+++
consectetur adipiscing elit. Praesent metus diam, vulputate quis vulputate at, semper id libero. Aliquam imperdiet venenatis mauris, id porttitor nisi mollis nec. Proin ut ullamcorper urna, sit amet pellentesque ex. Aenean vitae luctus nibh, in tincidunt tortor. Aliquam erat volutpat. Mauris sit amet aliquet mi, in lacinia metus. Suspendisse scelerisque consequat malesuada. Aenean porta mi ac ipsum pharetra, ac maximus massa pretium. In consequat sit amet mauris vitae sollicitudin. Fusce imperdiet vel neque pulvinar mollis. Donec at tortor sit amet odio varius dapibus vel quis justo. Nulla rutrum tempus massa, a blandit ante feugiat nec. Praesent a est a erat molestie iaculis sit amet et purus. In tristique laoreet laoreet. Phasellus aliquet libero vel commodo ultricies. Vestibulum porta neque eget arcu mollis vestibulum. \(x^2\) $x^2$ \\$x^2\\$ aasdasd



_this is a test_

$$
\begin{aligned}
KL(\hat{y} || y) &= \sum_{c=1}^{M}\hat{y}_c \log{\frac{\hat{y}_c}{y_c}} \\
JS(\hat{y} || y) &= \frac{1}{2}(KL(y||\frac{y+\hat{y}}{2}) + KL(\hat{y}||\frac{y+\hat{y}}{2}))
\end{aligned}
$$

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

this is a test about http

**Request:**
```http
POST /Controllers/Handlers/SearchHandler.php HTTP/1.1
Host: localhost:1337
Content-Length: 56
sec-ch-ua: "Not(A:Brand";v="24", "Chromium";v="122"
Accept: */*
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36
sec-ch-ua-platform: "Linux"
Origin: http://localhost:1337
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://localhost:1337/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: language=en; welcomebanner_status=dismiss; cookieconsent_status=dismiss; continueCode=1KbV5a7Q65yx3YJp1kNW4RKP9Xzjd58xAvOElgbLeqVmDBMn8roZw2alnjR9
Connection: close

search=%2527%2520or%25201%253D1%2520%252D%252D%2520%252D
```
asd

Etiam tincidunt vitae mauris eu semper. Fusce vestibulum elementum eros, blandit fermentum nisl commodo sed. Phasellus porttitor eleifend congue. In metus lectus, tincidunt non libero et, lacinia finibus enim. Pellentesque vulputate finibus sodales. Quisque ac eros tortor. Nulla a mollis diam. Vestibulum eget odio et quam dignissim rhoncus eget et ante. Morbi tellus elit, interdum ut ultricies a, iaculis nec nulla. In gravida eleifend mi non consequat. Aliquam vitae justo ut lectus ultrices fermentum sed at nibh. Sed congue, lacus quis iaculis rhoncus, nisl orci eleifend augue, eu porta leo quam ac nisi. Vivamus aliquam nulla ut ornare facilisis. Curabitur et nisl convallis, ornare sapien vel, fermentum orci. 

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item 

- test
    - test2
        - test3
**hello world**

__this is underlined__ 

<i> this is italic </i> 

<strong> this is strong </strong>

> Dorothy followed her through many of the beautiful rooms in her castle.
>
>> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

> #### The quarterly results look great!
>
> - Revenue was off the chart.
> - Profits were higher than ever.
>
>  *Everything* is going according to **plan**.

---

this other

I love supporting the **[EFF](https://eff.org)**.

[a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)

heelo ~~world~~

| Num | Header | Header2 | Header3 |
|:---:|--------|---------|---------|
|  1  | first  | 1st     | One     |
|  2  | second | 2nd     | Two     |
|  3  | third  | 3rd     | Three   |
