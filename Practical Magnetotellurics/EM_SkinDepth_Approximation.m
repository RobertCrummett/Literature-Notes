function p = EM_SkinDepth_Approximation(T, apparent_resistivity)
% Calculates an approximate skin depth
%
% Inputs:
% T - Period of electromagnetic wave. [s]
% apparent_resistivity - Apparent resistivity of the medium. [Ohm m]
%
% Outputs:
% p - Electromagnetic skin depth approximation. [m]

p = 500*sqrt(T.*apparent_resistivity);

end