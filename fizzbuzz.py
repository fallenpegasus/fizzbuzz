#!/usr/bin/python

# this doesn't seem that hard

# http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/
# Write a program that prints the numbers from 1 to 100. But for
# multiples of three print “Fizz” instead of the number and for the
# multiples of five print “Buzz”. For numbers which are multiples of
# both three and five print “FizzBuzz”."

# todo, make "FizzBuzz" drop out as an emergent case of "Fizz" and "Buzz"
# todo, generate a lazy evaluated sequence, and then just output the first 100 members

for i in xrange(1, 101):
    if (i % 5) == 0 and (i % 3) == 0:
        print "FizzBuzz"
    elif (i % 3) == 0:
        print "Fizz"
    elif (i % 5) == 0:
        print "Buzz"
    print i

