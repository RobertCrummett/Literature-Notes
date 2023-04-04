function DFact = DFactorial(n)
% Double factorial function, n!!
% https://en.wikipedia.org/wiki/Double_factorial
% 
% n!! = 1 for both n == 1 and n == 0
% Inputs must be vectors of positive, real integers
%
% Designed by John D'Errico on 9 Oct 2020, taken from the MATLAB forum
% Vectorized by Robert Nate Crummett 30 July 2022

DFact = zeros(size(n));
idx_zeros = find(n == 0);
idx_ones = find(n == 1);
DFact([idx_ones, idx_zeros]) = 1;

n_end = n(~DFact);
start = 1 + mod(n_end + 1,2); % caters for either parity of n
prod_results = zeros(size(n_end));

for i = 1:length(n_end)
    prod_results(i) = prod(start(i):2:n_end(i));
end

DFact(~DFact) = prod_results;

end