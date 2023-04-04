function [C] = Schmucker_Weidelt1(conductivity,frequency)
% Calculates transfer function of a homogenous half space
%
% Input arguments:
% conductivity - The conductivity of the homogenous half space. [S m^-1]
% frequency - The angular frequency of the electromagnetic waves. [rad s^-1]
%
% Output:
% C - The Schmucker-Weidelt transfer function. [m]
%
% For a homogenous half space, the real and imaginary parts of C must have
% the same magnitude.

[p,~] = EM_SkinDepth(conductivity,frequency);

C = p./2 - 1i*p./2;
% same as C = 1/q
end