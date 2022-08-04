% Project Euler
% Problem #67 Maximum path sum II

% Idea: Take the current row and take the max of the two sums above each
% entry.
% for instance, row 3 will look like this:
%         132   100
%       52    40    9
% So this last row becomes:
%   184   172   109
% and then look at the next row in the triangle

V = cell(100,1);

fileName = 'p067_triangle.txt';
%% Read data in from text file
fid = fopen(fileName);
lineNum = 1;
while ~feof(fid)
  line = fgetl(fid);
  T = textscan(line, '%u');
  V{lineNum} = cell2mat(T)';
  lineNum = lineNum+1;
end



%% Run algorithm
A = V{1};

for i = 2:length(V)
  B = V{i};
  S = [B(1)+A(1)];
  n = length(B);
  
  for j = 2:n-1
    temp = max(A(j-1),A(j)) + B(j);
    S = [S temp];
  end
  S = [S B(n)+A(n-1)];
  A = S;
end

fprintf('The maximum sum is %d\n', max(S));