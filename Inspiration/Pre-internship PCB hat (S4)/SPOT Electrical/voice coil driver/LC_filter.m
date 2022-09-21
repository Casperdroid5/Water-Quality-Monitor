clear all; close all; clc;
% Parallel damped LC filter for switched mode supply
% (see http://www.ti.com/lit/an/snva538/snva538.pdf)
% see Farnell SMD High Frequency Inductors
% 

Lf = 1e-3;
Cf = 47e-6;
Rf = 1; % inductor series resistance
ESRCf = 10; %
ESRCd = 10; %

nn_f_scale = [0:50e3];

Rd = 10;sqrt(Lf/Cf); % 
Cd = 2*Cf; %
Z1 = Rf + 2*pi*sqrt(-1)*nn_f_scale*Lf;
Z2 = ESRCf + 1./(2*pi*sqrt(-1)*nn_f_scale*Cf);
Z3 = 1./(2*pi*sqrt(-1)*nn_f_scale*Cd) + ESRCd + Rd;

% Z2eq2 = Z2*Z./(Z2+Rin);
Z3eq2 = Z2.*Z3./(Z2 + Z3);

H = abs(Z3eq2./(Z3eq2+Z1));

figure; %
semilogx(nn_f_scale, 20*log10(H));
hold on; grid on;


