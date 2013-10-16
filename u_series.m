function b = u_series(simfile)

	%% simfile should be the output file from the python script

  disp(simfile ) 
  simoutput = dlmread(simfile);

	%% get number of network nodes N and read u_i timeseries from simfile:

  tvec = simoutput(:,1);

  nt = size(tvec,1)
  dt = tvec(2)-tvec(1)     % same dt as in fhn_time_delays.py

  N = floor((size(simoutput,2)-1)/2)  % number of nodes 

  timeseries = zeros(size(simoutput,1),N);
  size(timeseries)

  for roi = 1:N
    timeseries(:,roi) = simoutput(:,2*roi);
  end
  
 save([simfile(1:end-4),'_u_series.mat'],'timeseries')
 
%  simfc = corr(timeseries)
%  imagesc(simfc);