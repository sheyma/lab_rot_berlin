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

  nt = size(tvec,1)
  dt = tvec(2)-tvec(1)     % same dt as in fhn_time_delays.py

  N = floor((size(simoutput,2)-1)/2)  % number of nodes 

  timeseries = zeros(size(simoutput,1),N);
  size(timeseries)

  for roi = 1:N
    timeseries(:,roi) = simoutput(:,2*roi);
  end

  save([simfile(1:end-4),'_timeseries.mat'],'timeseries','tvec')
  %load([simfile(1:end-4),'_timeseries.mat'])
  
  %% plot sample time series     
  close all;
  % specify plotting interval:
  minval = 325;
  range = 500;
%   h = figure;
%   plot(timeseries(minval:minval+range,:));
%   xlim([0 range])
%   xlabel('t in [ms]')
%   ylabel('u(t)')
%   axis([0 range 0.93 1.04])
  
%  plot only first u_i series as a function of time
%   figure(2)
%   plot((dt:dt:dt*nt),timeseries(:,1))
%   xlabel('t in [ms]','FontSize',25)
%   ylabel('u_1(t)','FontSize',25)
%   set(gca,'FontSize',25);
%  
%   textobj = findobj('type', 'text');
%   set(textobj, 'fontunits', 'points');
%   set(textobj, 'fontsize', 60);
%   
%   filo = ['sample_',simfile(1:end-4)]; 
%   print(h,'-depsc2',sprintf('%s.eps',filo));
%   system(sprintf('ps2pdf -dEPSCrop %s.eps %s.pdf',filo,filo));  
%   close(h);
  
  %%% apply Balloon Windkessel model in BOLD.m :  

  % initialize array:
  boldsignal = cell(N,1);
	
	% important: specify here to which time interval the simulated 
	% time series corresponds:
  %T = 700.0; % in [s] -Vesna
  T = (nt*dt)/1000;  % (ms to s : tmax/1000) - Seyma
  
  for roi = 1:N 
    boldsignal{roi} = BOLD(T,timeseries(:,roi));
    disp(roi)
    % verify that there is no errors in the BOLD results
    nans = size(find(isnan(boldsignal{roi})),1);
    if nans > 0
      disp(nans)
    end
  end
  
  %% filter below 0.25Hz:

  f_c=0.25;
  dtt=0.001; % Resolution of the BOLD signal (here 1 millisecond).

  % Low-Pass filter the BOLD signal

  n_t       = size(boldsignal{1},1)
  BOLD_filt = zeros(n_t,N);
  f_s       = 1/dtt                  % Sampling frequency (Hz)
  f_N       = f_s/2                 % Nyquist frequency (Hz)
 
  % Bold signal before filtering - sheyma
  sBOLD = zeros(n_t, N);
  for i=1:N
      sBOLD(:,i) = boldsignal{i};
  end
  
%   figure(3);
%   
%   plot((dt:dt:dt*n_t),sBOLD(:,1))
%   xlabel('t in [ms]','FontSize',25)
%   ylabel('simulated - u_1(t)','FontSize',25)
%   set(gca,'FontSize',25 )
% 

%   figure(4);
%   
%   plot((dt:dt:dt*n_t),sBOLD(:,1:N))
%   xlabel('t in [ms]','FontSize',25)
%   ylabel('simulated - u_1(t)','FontSize',25)
%   set(gca,'FontSize',25 )




  % Calculate variables for Butterworth lowpass filter of order 5 
  % with cut off frequency f_c/f_N
  [Bs,As] = butter(5,f_c/f_N,'low')

  
  size(BOLD_filt)

  for n = 1:N
    x               = boldsignal{n};
    BOLD_filt(:,n)  = filtfilt(Bs,As,x); % Apply filter
    %size(BOLD_filt)
  end
  
  

  
%   k=figure(5);
%   plot((dt:dt:dt*n_t),BOLD_filt(:,1:N))
%   xlabel('t in [ms]','FontSize',25)
%   ylabel('simulated - u_i(t)','FontSize',25)
%   set(gca,'FontSize',25 )
%   set(get(k,'Position'), [5 567 1272 380])

  %% Downsampling: select one point every 'ds' ms to match fmri resolution:

  ds=2; 
  down_bds=BOLD_filt(1:ds/dtt:end,:);
  lenBold = size(down_bds,1)
  
  %% Cutting first and last seconds (distorted from filtering) and keep the middle:
  nFramesToKeep = 10;
  minFrame = floor((lenBold-nFramesToKeep)/2)
  maxFrame = floor((lenBold+nFramesToKeep)/2)-1
  bds = down_bds(minFrame:maxFrame,:);
  size(bds)  
  save([simfile(1:end-4),'_bds.mat'],'bds')

  %%
  
  %load([simfile(1:end-4),'_bds.mat'])

  simfc = corr(bds);
  save([simfile(1:end-4),'_simfc.mat'],'simfc')
  
   % plot simulated functional connectivity
 % h = figure;
  imagesc(simfc); % automatic color scaling from min to max value 
  %imagesc(simfc,[-1.0 1.0]); chose this for color scaling from -1 to 1
  
  %title(['v=',simfile(29:30),' m/s'],'FontSize',40)
  set(gca, 'fontsize',30)
  %ylabel('r=0.78','FontSize',40)

  textobj = findobj('type', 'text');
  set(textobj, 'fontunits', 'points');
  set(textobj, 'fontsize', 60);

  filo = ['simfc_',simfile(1:end-4)]; 
  print(h,'-depsc2',sprintf('%s.eps',filo));
  system(sprintf('ps2pdf -dEPSCrop %s.eps %s.pdf',filo,filo));
  
end
