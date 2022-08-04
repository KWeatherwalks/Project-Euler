%{
Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

(21) 22  23  24 (25)
 20  (7)  8  (9) 10
 19   6  (1)  2  11
 18  (5)  4  (3) 12
(17) 16  15  14 (13)

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
%}

function [sumOfDiagonals, S] = Euler28(n)
% Project Euler Problem #28
% This program constructs a number spiral within a n-by-n matrix, where n
% is an odd number, then it displays a version of the famous Ulam spiral.
% n: an odd number
  
  % initialize n-by-n matrix
  S = zeros(n);
  
  % initialize starting entry in matrix
  ix = [(n+1)/2 , (n+1)/2];
  value = 1;
  S(ix(1),ix(2)) = value;
  % this effectively creates a 1-by-1 spiral (the trivial case)
  
  % initialize sum of diagonals
  sumOfDiagonals = 1;
  
  % spiral around the matrix
  for i = 1:2:n-2
    
    % move right once
    value = value+1;
    ix = right(ix);
    S(ix(1),ix(2)) = value;
    %right
    
    % move down i times
    for j = 1:i
      value = value+1;
      ix = down(ix);
      S(ix(1),ix(2)) = value;
    end %down
    
    % update sum
    sumOfDiagonals = sumOfDiagonals + value;
    
    % move left i+1 times
    for j = 1:i+1
      value = value+1;
      ix = left(ix);
      S(ix(1),ix(2)) = value;
    end %left
    
    % update sum
    sumOfDiagonals = sumOfDiagonals + value;
    
    % move up i+1 times
    for j = 1:i+1
      value = value+1;
      ix = up(ix);
      S(ix(1),ix(2)) = value;
    end %up
    
    % update sum
    sumOfDiagonals = sumOfDiagonals + value;
    
    % move right i+1 times
    for j = 1:i+1
      value = value+1;
      ix = right(ix);
      S(ix(1),ix(2)) = value;
    end %right
    
    % update sum
    sumOfDiagonals = sumOfDiagonals + value;
    
  end %for
  
  
  %% display Ulam Spiral
  V = isprime(S);
  V = double(V);
  %surf(V); view(0,-90);
  
  figure; spy(V);
  
end %Euler28

%% helper functions to find next entry in matrix

function coord = up(idx)
  
  coord = [idx(1)-1, idx(2)];

end %up

function coord = down(idx)
  
  coord = [idx(1)+1, idx(2)];

end %up

function coord = left(idx)
  
  coord = [idx(1), idx(2)-1];

end %up

function coord = right(idx)
  
  coord = [idx(1), idx(2)+1];

end %up