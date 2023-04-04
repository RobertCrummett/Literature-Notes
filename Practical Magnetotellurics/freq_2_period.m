function T = freq_2_period(frequency)
% Converts the angular frequency into periods
%
% Inputs:
% frequency - The angular frequency. [rad s^-1]
%
% Outputs:
% T - The period of the signal. [s cycle^-1]

T = 2*pi./frequency;

end