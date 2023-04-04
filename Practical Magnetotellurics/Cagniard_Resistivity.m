function rho = Cagniard_Resistivity(C, frequency)
% Calculates resistivity of a homogenous half space
%
% Input arguments:
% C - The Schmucker-Weidelt transfer function. [m]
% frequency - The angular frequency of the electromagnetic waves. [rad s^-1]
%
% Output:
% rho - The Cagniard resistivty. [ohm m^-1]
%
% For a homogenous half space, the real and imaginary parts of C must have
% the same magnitude.

% magnetic permeability of free space
mu_0 = 1.2566*10^(-6); % [H m^-1]

rho = abs(C).^2*mu_0.*frequency;

end