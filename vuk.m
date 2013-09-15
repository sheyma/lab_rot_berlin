% extended FitzHugh-Nagumo Model

close all;

dt=0.002;
t0=0;
tf=100;
t=t0:dt:tf;
N=length(t);

alpha=.85;
tau=1.25;
gamma=1.0;
b=0.2;


x_limit=2.5;
y_limit=2;
xE=-x_limit:0.01:x_limit;
yE1=xE.^3/3 - gamma*xE;
yE2=(alpha-xE)/b;

xT=zeros(1,N);
yT=xT;
xT(1)=-1;
yT(1)=-0.65;

for i=1:N-1
   xT(i+1)=xT(i)+(gamma*xT(i)-xT(i)^3/3+yT(i))*dt*tau; 
   yT(i+1)=yT(i)+(xT(i)+b*yT(i)-alpha)*(-1/tau)*dt;
end

figure(1)
subplot(1,2,1)
plot(t,xT,'k','LineWidth',1.5)
set(gca,'FontSize',25);
xlabel('time','FontSize',25)
ylabel('x','FontSize',25)
subplot(1,2,2)
set(gca,'FontSize',25);
plot(t,yT,'k','LineWidth',1.5)
xlabel('time','FontSize',25)
ylabel('y','FontSize',25)

% intersection of nullclines
its0=-2; %initial intersection point trial
its_x = fsolve(@(its_x)(-gamma*its_x -(alpha-its_x)/b + its_x^3/3 ), its0)
its_y = (alpha-its_x)/b
its_y2 = its_x^3/3 - gamma*its_x;

lambda1= ((tau*(gamma-its_x^2)-b/tau) + sqrt( tau*(gamma-its_x^2)^2 - 4*((its_x^2-gamma)*b)))/2
lambda2= ((tau*(gamma-its_x^2)-b/tau) - sqrt( tau*(gamma-its_x^2)^2 - 4*((its_x^2-gamma)*b)))/2

figure(2)
hold on
plot(xE,yE1,'r','LineWidth',2.5)
set(gca,'FontSize',20);
xlabel('x','FontSize',20)
ylabel('y','FontSize',20)
plot(xE,yE2,'b','LineWidth',2.5)
axis([-x_limit x_limit -y_limit y_limit])
if lambda1 < 0 & lambda2<0
plot(its_x, its_y, 'ok', 'LineWidth',4)
title('Fixed point is stable', 'FontSize',20)
elseif lambda1 < 0 & lambda2 >0
    plot(its_x, its_y, '--gs', 'LineWidth',20)
    title('Fixed point is Saddle', 'FontSize',20)
elseif lambda1 > 0 & lambda2 <0
    plot(its_x, its_y, '--gs', 'LineWidth',10)
    title('Fixed point is Saddle', 'FontSize',20)
else
    plot(its_x, its_y, 'sk', 'LineWidth',2)
    title('Fixed point is unstable', 'FontSize',20)
end
hold off



hold off