close all;
b=dlmread('A.txt');
c=dlmread('A_16x16.txt');
subplot(1,2,1)
imagesc(b)
h = colorbar;
set(gca,'FontSize',25)
title('A.txt','FontSize',25)
subplot(1,2,2)
imagesc(c)
h = colorbar;
set(gca,'FontSize',25)
title('A\_16x16.txt','FontSize',25)
hold off
