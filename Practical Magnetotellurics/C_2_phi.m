function phi = C_2_phi(C)
% Converts the transfer function to the impedence phase
%
% Inputs:
% C - The Schmucker-Weidelt transfer function. [m]
%
% Outputs:
% phi - The impedence phase. [rad]

phi = angle(C) + pi/2;

end