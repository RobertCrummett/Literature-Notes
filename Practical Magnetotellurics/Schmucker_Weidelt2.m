function [C] = Schmucker_Weidelt2(E_x, B_y,frequency)
% Calculates transfer function of a homogenous half space
%
% Input arguments:
% E_x - The x component of the electric field. [V m^-1]
% B_y - The y component of the magnetic field. [V s m^-2]
% frequency - The angular frequency of the electromagnetic waves. [rad s^-1]
%
% Output:
% C - The Schmucker-Weidelt transfer function. [m]
%
% For a homogenous half space, the real and imaginary parts of C must have
% the same magnitude.

C = E_x./(1i.*frequency.*B_y);
end