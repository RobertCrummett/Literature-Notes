function [Z_rel_error] = impedence_conf_interval(conf_level,...
    degrees_of_freedom,epsilon)
% This functions calculates the condifence interval of the impedence
% 
% Inputs:
% conf_level - The statistical measure of the probability that the
%              predicted value of Z lies within the calculated error.
% degrees_of_freedom - The number of independant ibservations
%
% Optional Inputs:
% epsilon - The residuum, the relative fraction of the electric power
%           spectrum that is not correlated with the magnetic field.
%           Default is sqrt(15)
%
% Outputs:
% Z_rel_error - the order of magnitude of the relative error of an 
%               impedence Z

if ~exist('epsilon','var')
    % experience suggests, for longest periods, epsilon^2 = 0.15
    % Simpson and Bahr, 2005
    epsilon = sqrt(0.15);
end

Z_rel_error = sqrt(4*finv(conf_level,4,degrees_of_freedom-4)*epsilon^2/...
    (degrees_of_freedom - 4));

end