% Project Euler
% Problem #31 Coin sums

syms x
p1 = 1/(1-x);
p2 = 1/(1-x^2);
p5 = 1/(1-x^5);
p10 = 1/(1-x^10);
p20 = 1/(1-x^20);
p50 = 1/(1-x^50);
p100 = 1/(1-x^100);
p200 = 1/(1-x^200);

C = p1*p2*p5*p10*p20*p50*p100*p200;
T = taylor(C,'Order',201);
tCoeffs = coeffs(T);
numWays = tCoeffs(201);

fprintf('There are %d ways to make change for 200p\n',numWays);