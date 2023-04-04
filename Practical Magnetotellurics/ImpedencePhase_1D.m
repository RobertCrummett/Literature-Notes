function phi = ImpedencePhase_1D(E_x,B_y)
% Calculates the impedence phase of the transfer function Schmicker_Weidelt2()
%
% Inputs:
% E_x - The x component of the electric field. [V m^-1]
% B_y - The y component of the magnetic field. [V s m^-2]
%
% Outputs:
% phi - The impedence phase. [rad]

phi = atan2(E_x, B_y);

end