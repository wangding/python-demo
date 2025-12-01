n = input('n: ');
x = 1:2:(2*n-1);
y = (-1).^(2:n+1)./x;
pai = sum(y)*4
