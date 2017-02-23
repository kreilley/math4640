function [ ] = Problem5( ~ )
%Problem5 Performs hw3 problem 5 task
%   Kevin Reilley, written 2/21/2017
%   matlab 2015a function for performing the tasks of problem 5 and
%   generating plots.  



% get samples
fx = @(x) sin(3.*x).^2;
xg = linspace(0,2*pi,200);
fg = fx(xg);
[g5,cs] = evalCoeffs(5,xg,fg);

figure(1)
subplot(2,2,1)
plot(xg,fg,'bx',xg,real(g5),'-k')
legend('true values','estimate','Location','BestOutside')
title('Fourier transform of sin(3*x) with j = 5')
ylabel('fcn value')
xlabel('x value')
subplot(2,2,3)
fs = length(cs);
xxx = -(fs-1)/2:1:(fs-1)/2;
bar(xxx,real(cs))
xlabel('frequency')
ylabel('magnitude')

[g10,cs] = evalCoeffs(10,xg,fg);
subplot(2,2,2)
plot(xg,fg,'bx',xg,real(g10),'-k')
title('Fourier transform with j = 10')
ylabel('fcn value')
xlabel('x value')
subplot(2,2,4)
fs = length(cs);
xxx = -(fs-1)/2:1:(fs-1)/2;
bar(xxx,real(cs))
xlabel('frequency')
ylabel('magnitude')

hx = @(x) cos(2.*x).^(3) + cos(sqrt(2).*x);
hg = hx(xg);
[l5,cs] = evalCoeffs(5,xg,hg);
figure(2)
subplot(2,2,1)
plot(xg,hg,'bx',xg,real(l5),'-k')
legend('true values','estimate')
title('Fourier transform of cos(2x)^3 + cos(sqrt(2)*x) with j = 5')
ylabel('fcn value')
xlabel('x value')
subplot(2,2,3)
fs = length(cs);
xxx = -(fs-1)/2:1:(fs-1)/2;
bar(xxx,real(cs))
xlabel('frequency')
ylabel('magnitude')

[l10,cs] = evalCoeffs(10,xg,hg);
subplot(2,2,2)
plot(xg,hg,'bx',xg,real(l10),'-k')
title('Fourier transform with j = 10')
ylabel('fcn value')
xlabel('x value')
subplot(2,2,4)
fs = length(cs);
xxx = -(fs-1)/2:1:(fs-1)/2;
bar(xxx,real(cs))
xlabel('frequency')
ylabel('magnitude')


end

function cs = coeffFcn(jj,fg,xg)
%
%
nm1 = length(xg)-1;
cs = sum(fg.*exp(-xg.*jj.*1i));
cs = cs*(1/(nm1+1));
end

function [gx,cs] = evalCoeffs(jmax,xg,fg)
%
%
gx = zeros(size(xg));
dex = -jmax:1:jmax;
cs = zeros(size(dex));
for ndx = dex;
    cs(dex==ndx) = coeffFcn(ndx,fg,xg);
    gx = gx + cs(dex==ndx)*exp(1i.*ndx.*xg);
end

end