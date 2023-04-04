%% Example 8.1
% We did MLE on Old Faithful eruption wait times in Example 5.27. Now,
% characterize the emprical PDF of the data, and then resample from it with
% replacement 30, 100, 300, 1000, 3000, and 10000 times. Plot the sample
% eman for each replicate. Plot the resulting bootstrap distributions for
% the sample mean. Repeat for the kurtosis.

%% Importing Data
clear; close all; clf;
geyser = importdata('geyser.dat');

%% Gaussian Q-Q Plot
figure(1);
qqplot(geyser)
title 'Gaussian Q-Q Plot for the Old Faithful Data'

% The data is shorter tailed than Gaussian data at the top and bottom, with
% an excess of probability near the distribution mode.

%% Bootstrapping Method for Sample Means
n = length(geyser);
b = [30 100 300 1000 3000 10000];
bins = [10 20 30 30 50 50];

% Initialize random number seed so the result will be reproducible
rng default

figure(2)
for i = 1:length(b)
    % Use unidrnd() to get indices to sample the data with replacement
    ind = unidrnd(n, n, b(i));
    boot = geyser(ind); %resample the data
    kurtb = mean(boot);
    mean(kurtb)
    subplot(3, 2, i)
    histogram(kurtb, bins(i), 'Normalization', 'pdf')
    title(strcat(string(b(i)), " resamples with replacement"))
end
sgtitle('Bootstrapping Method for Sample Means')

%% Bootstrapping Method for Kurtosis

figure(3)
for i = 1:length(b)
    % Use unidrnd() to get indices to sample the data with replacement
    ind = unidrnd(n, n, b(i));
    boot = geyser(ind); %resample the data
    kurtb = kurtosis(boot);
    mean(kurtb)
    subplot(3, 2, i)
    histogram(kurtb, bins(i), 'Normalization', 'pdf')
    title(strcat(string(b(i)), " resamples with replacement"))
end
sgtitle('Bootstrapping Method for Sample Kurtosis')

% The approach in this section was nonparametric bootstrapping because
% there were no asumptions made about the distribution of the data being
% resampled.
