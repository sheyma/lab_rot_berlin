function corr_matrix = corr_mtr(in_put)
    close all;
    threshold=input('insert the threshold value of f_ij : ');
    out_put=dlmread(in_put);
    corr_matrix=corr(out_put);
    h=figure;
    imagesc(corr_matrix);
    colorbar;
    title( sprintf('%s = %.2f' , 'r', threshold), 'FontSize', 25);
    set(gca,'FontSize',25)
    name=sprintf('%s%.2f' , 'corr_matrix_r_', threshold);
    print(h,'-depsc2',sprintf('%s.eps', name)); 
    

%   print(h,'-depsc2',sprintf('%s.eps',filo));
%   system(sprintf('ps2pdf -dEPSCrop %s.eps %s.pdf',filo,filo));