%{
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors 
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known
that the greatest number that cannot be expressed as the sum of two 
abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.
%}

abundants = [];

pb = waitbar(0,'building list of abundant numbers');

for i = 12:28111
  
  waitbar((i-12)/28111,pb);
  
  D = divisors(i);
  num = sum(D(1:length(D)-1));
  
  if num > i
    abundants = [abundants, i];
  end %if
  
end % for

delete(pb);

n = length(abundants);
A = zeros(n);

for i = 1:n
  for j = 1:i
    
    A(i,j) = abundants(i) + abundants(j);
    
  end %for
end %for


% sum of all integers from 1 to 28123
S = sum(1:28123);

% sum of all numbers which can be expressed as sum of two abundants
s = sum(unique(A(A<28124)));

% display result
disp(S-s);
