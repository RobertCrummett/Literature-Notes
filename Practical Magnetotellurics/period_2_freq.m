function frequency = period_2_freq(T)
% Converts the period into angular frequency
%
% Inputs:
% T - The period of the signal. [s cycle^-1]
%
% Outputs:
% frequency - The angular frequency. [rad s^-1]

frequency = 2*pi./T;

end