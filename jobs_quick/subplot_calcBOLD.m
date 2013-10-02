function g = subplot_calcBOLD(simfile)
        
    thresholds = [38 50 78];
    sigma = [0 2 5 7 9];
    m = length(sigma) ;
    n = length(thresholds);
    p = 1;
    
    for j =1:m
        simfile(17)=num2str(sigma(j));
        for i = 1:n
            simfile(6:7) = num2str(thresholds(i));
            subplot(m,n,p)
            set(gca,'FontSize',25)
            calcBOLD(simfile)
            if j==1
                title(['r=0.',num2str(thresholds(i))],'FontSize',30)
            end
            
            if i==1
                 ylabel(['c=0.',num2str(sigma(j))],'FontSize',30)
            end
            p=p+1;
        end
    end

   