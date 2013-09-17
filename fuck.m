close all;
b=dlmread('FSL_ROIs_distance_matrix.dat');

imagesc(b)




h = colorbar;
set(gca,'FontSize',25)
ylabel(h, 'Distance (mm)', 'FontSize', 25)