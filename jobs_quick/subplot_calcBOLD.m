function g = subplot_calcBOLD(simfile)
        
    thresholds = [38 50 78];
    sigma = [0 2 5 7 9];
    m = length(sigma) ;
    n = length(thresholds);
    p = 1;
    
    for j =1:m
        simfile(17)=num2str(sigma(j))
        
        for i = 1:n
            thr = thresholds(i);
            simfile(6:7) = num2str(thr);
            position = strcat(num2str(m),',',num2str(n),',',num2str(p))
            my_calcBOLD(simfile,position)
            p=p+1;
        end
    end

   