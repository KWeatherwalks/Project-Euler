V{1} = [75];
V{2} = [95 64];
V{3} = [17 47 82];
V{4} = [18 35 87 10];
V{5} = [20 04 82 47 65];
V{6} = [19 01 23 75 03 34];
V{7} = [88 02 77 73 07 63 67];
V{8} = [99 65 04 28 06 16 70 92];
V{9} = [41 41 26 56 83 40 80 70 33];
V{10} = [41 48 72 33 47 32 37 16 94 29];
V{11} = [53 71 44 65 25 43 91 52 97 51 14];
V{12} = [70 11 33 28 77 73 17 78 39 68 17 57];
V{13} = [91 71 52 38 17 14 91 43 58 50 27 29 48];
V{14} = [63 66 04 68 89 53 67 30 73 16 69 87 40 31];
V{15} = [04 62 98 27 23 09 70 98 73 93 38 53 60 04 23];

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