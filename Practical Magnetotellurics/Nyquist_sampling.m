function [sample_rate] = Nyquist_sampling(smallest_period)
% This function implements the sampling theorem
%
% Inputs:
% smallest_period - The smallest period of interest in a time series. [s]
%
% Outputs:
% sample_rate - The minimum sample rate required to adequately sample
%                the smallest period of interest. [s]

sample_rate = smallest_period/2;
% less than or equal to
end
