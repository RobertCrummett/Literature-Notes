%% Recreating Figure
% Figure 1.3
% https://digital.library.adelaide.edu.au/dspace/bitstream/2440/48492/8/02chapters1-3.pdf

mu_0 = 4*pi*10^(-7);
conductivity = 10^(-2);
angular_frequency = 10^(-2);

k = (1 + 1i)*sqrt(conductivity.*angular_frequency.*mu_0/2);
nu = sqrt(conductivity.*angular_frequency.*mu_0/2);

B_0 = 10;
E_0 = 10;

B = @(depth) B_0*exp(-1i*nu*depth).*exp(-nu*depth);
E = @(depth) E_0*exp(-1i*nu*depth).*exp(-nu*depth);

skin_depth = 1./real(k);

f = figure(1);
f.Position = [100 100 450 350];
depth = linspace(0,4.7*skin_depth,100);
plot(depth./skin_depth,abs(E(depth)/E_0),'k-','LineWidth',2)
hold on
plot(depth./skin_depth,real(E(depth)/E_0),'r-','LineWidth',2)
plot(depth./skin_depth,imag(E(depth)/E_0),'b-','LineWidth',2)
hold off

grid('on')
legend('absolute attenuation','real part','imaginary part')
ylabel('E(z)/E_0')
xlabel('z/\delta')
title('Depth dependant behavior of the E field')