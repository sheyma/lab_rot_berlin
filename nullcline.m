close all;

% simple FitzHugh-Naguma Model - nullcline analysis
a=0.90;
eps=1;

xlimit=2.5;
ylimit=2;
x=-xlimit:0.1:xlimit;
y=x-x.^3/3;
yy=-ylimit:0.1:ylimit;
xx=-a*ones(1,length(yy));

lambda(1)= (1-a^2 + sqrt( (1-a^2)^2-4*eps) )/(2*eps);
lambda(2)= (1-a^2 - sqrt( (1-a^2)^2-4*eps) )/(2*eps);

dt=0.002;
t0=0;
tf=50;
t=t0:dt:tf;
N=length(t);

xt=zeros(1,N);
yt=zeros(1,N);
xt(1)=-0.05;
yt(1)=-.75;

for i=1:N-1
   xt(i+1)=xt(i)+(xt(i)-xt(i)^3/3-yt(i))*dt/eps;
   yt(i+1)=yt(i)+(xt(i)+a)*dt;
end

% figure(1)
% subplot(1,2,1)
% set(gca,'FontSize',25);
% plot(t,xt,'k','LineWidth',1.5)
% xlabel('time','FontSize',25)
% ylabel('x','FontSize',25)
% subplot(1,2,2)
% set(gca,'FontSize',25);
% plot(t,yt,'k','LineWidth',1.5)
% xlabel('time','FontSize',25)
% ylabel('y','FontSize',25)
% 
% figure(2)
% hold on
% axis([-xlimit xlimit -ylimit ylimit])
% set(gca,'FontSize',25);
% plot(xt,yt, 'g', 'LineWidth',4)
% plot(xt(1),yt(1), 'xg', 'LineWidth',10)
% plot(x,y, 'r', 'LineWidth', 2.5)
% plot(xx,yy, 'b', 'LineWidth', 2.5)
% xlabel('x','FontSize',20)
% ylabel('y','FontSize',20)
% if lambda < 0
% plot(-a, -a+a^3/3, 'ok', 'LineWidth',4)
% title('Fixed point is stable', 'FontSize',20)
% else
%     plot(-a, -a+a^3/3, 'ks', 'LineWidth',3)
%     title('Fixed point is unstable', 'FontSize',20)
% end
% hold off

% extended FitzHugh-Nagumo Model

a1=0.9;
eps1=0.4;
gamma=0.05;

x_limit=2.5;
y_limit=1;
xE=-x_limit:0.01:x_limit;
yE=(xE+a1)./gamma;
yE2=(xE-xE.^3/3);

xT=zeros(1,N);
yT=xT;
xT(1)=-0.75;
yT(1)=-1;

for i=1:N-1
   xT(i+1)=xT(i)+(xT(i)-xT(i)^3/3-yT(i))*dt/eps1; 
   yT(i+1)=yT(i)+(xT(i)-gamma*yT(i)+a1)*dt;
end

figure(3)
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
b0=-2;
b = fsolve(@(b)(-a1/gamma+ (1-1/gamma)*b - b^3/3 ), b0);
c = (b+a1)/gamma;

lambda1(1)= ((1-b^2-gamma*eps1) + sqrt((1-b^2-gamma*eps1)^2 - 4*(gamma*eps1*b^2 + eps1 - gamma*eps1)  ) )/2;
lambda1(2)= ((1-b^2-gamma*eps1) - sqrt((1-b^2-gamma*eps1)^2 - 4*(gamma*eps1*b^2 + eps1 - gamma*eps1)  )) /2;

figure(4)
hold on
plot(xT,yT, 'g', 'LineWidth',4)
plot(xT(1),yT(1), 'xg', 'LineWidth',10)
plot(xE,yE,'b', 'LineWidth', 2.5)
set(gca,'FontSize',20);
plot(xE,yE2, 'r', 'LineWidth', 2.5)
if lambda1 <0 
    plot(b,c, 'ok', 'LineWidth',4)
    title('Fixed point is stable', 'FontSize',20)
else
    plot(b,c, 'sk', 'LineWidth',2)
    title('Fixed point is unstable', 'FontSize',20)
end
    
    axis([-x_limit x_limit -ylimit ylimit])
hold off