% Project Euler 
% Problem #25 1000-digit Fibonacci number
digit = 1000;
d = digit-1;
F1 = 1;
F2 = 1;

idx = 3;
Fm2 = F1; Fm1 = F2;
Fib = Fm1 + Fm2;

while Fib < 10^d
  Fm2 = Fm1;
  Fm1 = Fib;
  idx = idx+1;
  Fib = Fm1+Fm2;
  if (Fib/10 > 1)
    d = d - 1;
    Fib = Fib/10;
    Fm2 = Fm2/10;
    Fm1 = Fm1/10;
  end
end

fprintf('The %dth term is the first %d-digit Fibonacci number.\n', idx, digit);