

close all;
coordinate=load('XYZ_coor_only_64_ROIs.txt');
r = 0.55; % threshold 
A = load('A.txt'); % adjacency matrix 
 AT = A > r;  % thresholded marix 
%  gplot(AT, coordinate, '-o'); %2D

x=coordinate(:,1);
y=coordinate(:,2);
z=coordinate(:,3);
adj=A>r;
[r c]=find(adj);
p=[r c]';
plot3(x(p),y(p),z(p),'-bo')
 axis vis3d, box on, view(3)
h=findobj('type','markersize');
set(h,'markersize',40)
ylabel('Posterior-Anterior','fontsize', 30);
xlabel('Left-Right','fontsize',30);
zlabel('Dorsal-Ventral','fontsize',30)

% TYPE r into title!

title('r=0','fontsize',40)
% xlabel('Posterior-Anterior','fontsize', 24);
% ylabel('Inferior-Superior','fontsize',24);
set(gca,'xtick',[]);
set(gca,'ytick',[]);