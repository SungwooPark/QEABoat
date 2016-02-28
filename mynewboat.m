function mynewboat
clf
% define the size and mass of the boat
L = 55;%cm
W = 30;%cm
mass = 1224;%grams
% define a grid of points (don't change)
dy = 0.02;
dz = 0.01;
da = dy.*dz;

[y,z]=meshgrid(-1:dy:1,-1:dz:0);
% set the shape
n = 3;
% set a guess for the intercept (don't change)
d = -0.5;
% set the relative center of mass
ycom = 0;
zcom = -(1-0.254);
% loop through the angles (will fail at exactly 90 so avoid)
for theta = 0:sqrt(5):180
    % find the waterline (don't change)
    d = fzero(@(d) bouyancy(y,z,n,theta,d,da,L,W,mass), d);
    % find the cob (don't change)
    [ycob,zcob] = cob(y,z,n,theta,d,da);
    % define the water vector (don't change)
    watervec = [cosd(theta) sind(theta)];
    % find the arm (don't change)
    arm = (W/2).*[ycob-ycom,zcob-zcom]*watervec';%cm
    % plot the stability curve
    plot(theta,arm,'r*'), hold on, grid on
    xlabel('Heel Angle (degrees)')
    ylabel('Moment Arm (cm)')
end
end

function res = bouyancy(y,z,n,theta,d,da,L,W,mass)
% return the difference between boat mass and displaced water mass (don't
% change)
res = sub_area(y,z,n,theta,d,da)*(W/2)^2*L - mass;%grams
end

function area = sub_area(y,z,n,theta,d,da)
% find the submerged area (don't change)
if theta < 90
    index = find(z > hull(y,n) & z < water(y,theta,d));
else
    index = find(z > hull(y,n) > 0 & z > water(y,theta,d) & z < 0);
end
area = length(index).*da;
end

function [ycob,zcob] = cob(y,z,n,theta,d,da)
% find the cob (don't change)
if theta < 90
    index = find(z > hull(y,n) & z < water(y,theta,d));
else
    index = find(z > hull(y,n) > 0 & z > water(y,theta,d) & z < 0);
end
area = length(index).*da;
ycob = sum(y(index).*da)./area;
zcob = sum(z(index).*da)./area;
end

function z = hull(y,n)
% the hull function (don't change)
z = abs(y).^n - 1;
end

function z = water(y,theta,d)
% the water function (don't change)
z = tand(theta).*y + d;
end