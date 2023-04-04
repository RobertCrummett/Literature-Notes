function [T] = Depth_2_Period_Estimate(conductivity,...
    necessary_penetration_depth)
% Inverts the skin depth calculation to solve for period in terms of depth
%
% Inputs:
% conductivity - The conductivity of the 'homogenous' halfspace.
%                Keep in mind this is an approximation. [S m^-1]
% necessary_penetration_depth - The skin depth required. [m]
%
% Outputs:
% T - Period required to reach the skin depth. [s]

mu_0 = 4*pi*10^(-7); % [H m^-1]

T = mu_0*conductivity.*pi.*necessary_penetration_depth.^2;

end

