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
x1 = real(cs);
y1 = imag(cs);
xlabel('frequency')
ylabel('real-value magnitude')

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
x2 = real(cs);
y2 = imag(cs);
xlabel('frequency')
ylabel('real-value magnitude')

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
x3 = real(cs);
y3 = imag(cs);
xlabel('frequency')
ylabel('real-value magnitude')

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
x4 = real(cs);
y4 = imag(cs);
xlabel('frequency')
ylabel('real-value magnitude')

figure(3)
subplot(2,2,1)
plot(x1,y1,'b*')
title('Complex Plane Coefficients for j = 5, sin3x')
xlabel('Real part')
ylabel('Imag part')
subplot(2,2,2)
plot(x2,y2,'b*')
title('Complex Plane Coefficients for j = 10, sin3x')
xlabel('Real part')
ylabel('Imag part')
subplot(2,2,3)
plot(x3,y3,'b*')
title('Complex Plane Coefficients for j = 5, cos(2x)^3 + cos(sqrt(2)*x)')
xlabel('Real part')
ylabel('Imag part')
subplot(2,2,4)
plot(x4,y4,'b*')
title('Complex Plane Coefficients for j = 10, cos(2x)^3 + cos(sqrt(2)*x)')
xlabel('Real part')
ylabel('Imag part')


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