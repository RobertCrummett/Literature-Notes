%% Wait's Recursion Method Demonstration
% Input an Earth model.
% Ouputs graphs of:
% 1. apparent resistivity vs period
% 2. phase angle vs. period
% 3. resistivity vs. depth

%% Earth Model UI
clear; clf; close all

% Inputs:
conductivity = [10^(-4.4), 10^(-2)];
conductivity = [10^(-0.5), 10^(-2)];
depth = [0, 10^4];
depth = [0, 100];

%% Wait's Recursion Method Implemented
mu_0 = 1.2566*10^(-6);
N = length(conductivity);
L = @(n) (depth(n+1) - depth(n));
tf = cell(N,1);

% layer N
q = @(f,n) sqrt(1i*mu_0*conductivity(n)*f);
C = @(f,n) 1./q(f,n);
C = @(f) C(f,N);
tf{N} = @(f) C(f);

% layer N - 1 through 1
for i = N-1:-1:1

    C = @(f,n) (1./q(f,n)).*...
        (q(f,n).*C(f) + tanh(q(f,n).*L(n)))./...
        (1 + q(f,n).*C(f).*tanh(q(f,n).*L(n)));

    C = @(f) C(f,i);
    tf{i} = C;
end

%% Plotting Resulting Transfer Function Information

% Plot apparent resistivity vs period
C = tf{1};
ar = @(f) abs(C(f)).^2.*mu_0.*f;

T = logspace(-3,3,50);
freq = period_2_freq(T);

figure(1);
subplot(2,2,3)
plot(T, ar(freq), 'r*')
set(gca,'YScale','log')
set(gca,'XScale','log')
ylim([10^0, 10^(4)])

xlabel('Period [s]')
ylabel('Apparent Resistivity [{\Omega}m]')

% Plot phase vs period
phase = @(f) angle(C(f)) + pi/2;

subplot(2,2,4);
hold on
yline(45,'k-')
plot(T, rad2deg(phase(freq)), 'b*')
hold off
set(gca,'XScale','log')
set(gca,'YLim',[0,90])

xlabel('Period [s]')
ylabel('Phase [degrees]')

% Plot depth vs resistivity (earth model)
subplot(2,2,1.5);
max_depth = (10^6);
N = length(depth);
hold on
plot([1/conductivity(1), 1/conductivity(1)], [1, depth(2)],...
    'k-', LineWidth = 2)
plot([1/conductivity(1), 1/conductivity(2)], [depth(2), depth(2)],...
    'k-', LineWidth = 2)
for i = 2:(N-1)
    plot([1/conductivity(i), 1/conductivity(i)], [depth(i), depth(i+1)],...
        'k-', LineWidth = 2)
    plot([1/conductivity(i), 1/conductivity(i+1)], [depth(i+1), depth(i+1)],...
        'k-', LineWidth = 2)
end
plot([1/conductivity(N), 1/conductivity(N)], [depth(N), max_depth],...
    'k-', LineWidth = 2)
hold off

xlim([10^0, max_depth])
set(gca,'YScale','log')
set(gca,'XScale','log')
set(gca,'XAxisLocation','top')
set(gca,'YDir','reverse')
grid on
ylabel('Depth [m]')
xlabel('Resistivity [{\Omega}m]')

sgtitle('Figure 2.4 Practical Magnetotellurics')