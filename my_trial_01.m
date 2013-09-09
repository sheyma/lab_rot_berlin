% calculate BOLD signal from pydelay/netpy output
% ###############################################

function b = calcBOLD(simfile)

	%% simfile should be the output file from the python script

  disp(simfile ) 

  tic;
  simoutput = dlmread(simfile);
  toc;

	%% get number of network nodes N and read u_i timeseries from simfile:

  tvec = simoutput(:,1);

  size(simoutput)
  nt = size(tvec,1)
  dt = tvec(2)-tvec(1)

  N = (size(simoutput,2)-1)/2

  timeseries = zeros(size(simoutput,1),N);
  size(timeseries)

  for roi = 1:N
    timeseries(:,roi) = simoutput(:,2*roi);
  end

  save([simfile(1:end-4),'_timeseries.mat'],'timeseries','tvec')
  %load([simfile(1:end-4),'_timeseries.mat'])
  
  %% plot sample time series     
  
  % specify plotting interval:
  minval = 325;
  range = 50;
  h = figure;
  plot(timeseries(minval:minval+range,:));
  xlim([0 range])
  xlabel('t in [ms]')
  ylabel('u(t)')
  
    textobj = findobj('type', 'text');
  set(textobj, 'fontunits', 'points');
  set(textobj, 'fontsize', 60);
  
  filo = ['sample_',simfile(1:end-4)]; 
  print(h,'-depsc2',sprintf('%s.eps',filo));
  system(sprintf('ps2pdf -dEPSCrop %s.eps %s.pdf',filo,filo));  
  close(h);
  
  %%% apply Balloon Windkessel model in BOLD.m :  

  % initialize array:
  boldsignal = cell(N,1);
	
	% important: specify here to which time interval the simulated 
	% time series corresponds:
  T = 60; % in [s]
  
  for roi = 1:N 
    boldsignal{roi} = BOLD(T,timeseries(:,roi));
    disp(roi)
    % verify that there is no errors in the BOLD results
    nans = size(find(isnan(boldsignal{roi})),1);
    if nans > 0
      disp(nans)
    end
  end
  
  