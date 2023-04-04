function [p, q] = EM_SkinDepth(conductivity, frequency)
% Calculates electromagnetic skin depth of a homogenous half space
%
% Input arguments:
% conductivity - The conductivity of the homogenous half space. [S m^-1]
% frequency - The angular frequency of the electromagnetic waves. [rad s^-1]
%
% Output:
% p - The electromagnetic skin depth. [m]
% q - Propogration constant [m^-1].

% magnetic permeability of free space
mu_0 = 1.2566*10^(-6); % [H m^-1]

p = sqrt(2./(mu_0.*conductivity.*frequency));
q = sqrt(mu_0*conductivity.*frequency/2) +...
    1i.*sqrt(mu_0*conductivity.*frequency/2);
end