% extended FitzHugh-Nagumo Model

close all;

dt=0.002;
t0=0;
tf=100;
t=t0:dt:tf;
N=length(t);

alpha=0.85;
tau=1.25;
gamma=1;  %gamma close to 1
b=0.2;  % incline 


x_limit=2.5;
y_limit=2;
xE=(-x_limit:0.01:x_limit);
yE1=xE.^3/3 - gamma*xE;  % make yE totally minus
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
its_x = fsolve(@(its_x)(-gamma*its_x -(alpha-its_x)/b + its_x^3/3 ), its0);
its_y = (alpha-its_x)/b;
its_y2 = its_x^3/3 - gamma*its_x;

A=1;
B=b/tau - (gamma - its_x^2)*tau;
C=1- b*(gamma - its_x^2);

lambda1= (-B + sqrt(B^2 - 4*A*C)) / (2*A);
lambda2= (-B - sqrt(B^2 - 4*A*C)) / (2*A);

figure(2)
hold on
plot(xT,yT, 'g', 'LineWidth',3)
plot(xT(1),yT(1), 'xg', 'LineWidth',10)
plot(xE,yE1,'r','LineWidth',2.5)
set(gca,'FontSize',20);
xlabel('x','FontSize',20)
ylabel('y','FontSize',20)
plot(xE,yE2,'b','LineWidth',2.5)
axis([-x_limit x_limit -y_limit-1 y_limit+1])
if real(lambda1) < 0 && real(lambda2)<0
plot(its_x, its_y, 'ok', 'LineWidth',4)
title('Fixed point is stable', 'FontSize',20)
elseif  real(lambda1) < 0 && real(lambda2)>0  
    plot(its_x, its_y, '--gs', 'LineWidth',20)
    title('Fixed point is Saddle', 'FontSize',20)
elseif  real(lambda1) > 0 && real(lambda2)<0
    plot(its_x, its_y, '--gs', 'LineWidth',10)
    title('Fixed point is Saddle', 'FontSize',20)
else
    plot(its_x, its_y, 'sk', 'LineWidth',2)
    title('Fixed point is unstable', 'FontSize',20)
end
hold off

%note saddle does not happen actually, beacuse we eliminate it

