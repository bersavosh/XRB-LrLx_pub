################################################################################
#
# XRB-LrLx_pub
# Python Script to produce LR-Lx plot for accreting systems.
#
# Github page: https://github.com/bersavosh/XRB-LrLx_pub
#
# Developed and maintained by Arash Bahramian 
#
################################################################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc


def data_reader(path_to_data = './data/', include_oddsources=False):
    """
    Function to read data from various CSV files and construct a single Pandas DF

    Parameters
    ----------
    path_to_data: directory containing all csv data files 

    include_oddsources: boolean, indicating whether Cyg X-1 and GRS1915 should be included

    Returns
    -------
    data: a single Pandas dataframe containing all data provided for LrLx

    """
    DATA_BHs = pd.read_csv(path_to_data+'lrlx_data_BHs.csv')
    DATA_candBHs = pd.read_csv(path_to_data+'lrlx_data_candidateBHs.csv')
    DATA_NSs = pd.read_csv(path_to_data+'lrlx_data_NSs.csv')
    DATA_canNSs = pd.read_csv(path_to_data+'lrlx_data_candidateNSs.csv')
    DATA_AMXPs = pd.read_csv(path_to_data+'lrlx_data_AMXPs.csv')
    DATA_tMSPs = pd.read_csv(path_to_data+'lrlx_data_tMSPs.csv')
    DATA_WDs = pd.read_csv(path_to_data+'lrlx_data_WDs.csv')
    if include_oddsources:
        DATA_oddsrcs = pd.read_csv(path_to_data+'lrlx_data_oddsrcs.csv')
        DATA_LIST = [DATA_BHs, DATA_candBHs, DATA_NSs, 
                     DATA_canNSs, DATA_AMXPs, DATA_tMSPs, 
                     DATA_tMSPs, DATA_WDs, DATA_oddsrcs]
    else:
        DATA_LIST = [DATA_BHs, DATA_candBHs, DATA_NSs, 
                     DATA_canNSs, DATA_AMXPs, DATA_tMSPs, 
                     DATA_tMSPs, DATA_WDs]
    DATA = pd.concat(DATA_LIST,ignore_index=True)

    return DATA


def plotter(data, classes, fig, errorbars=True, uplims=True, cor_lines=True):
    """
    Main LrLx plotting function
    
    Parameters
    ----------
    data: Pandas dataframe with the LrLx data to plot.
    
    classes: a list/array of strings that would include a subset of the following:
             ['BH', 'candidateBH', 'NS', 'candidateNS', 'AMXP', 'tMSP', 'WD']
    
    fig: a matplotlib figure object to plot on.
    
    errorbars: boolean variable indicating weather measurement uncertainties 
                should be plotted (where available).
                
    uplims: boolean variable indicating whether data points that consist of either
            X-ray or radio upper limits should be plotted.
            
    cor_lines: boolean variable indicating whether to plot reported correlation lines
                WARNING: While BH systems tend to show a correlation, 
                this seems not to be a case for NS systems anymore.
                Thus, plotting them could be misleading and hence not recommended.
                The trends are kept in the function for historical purposes, 
                but are by default commented out.

    Returns
    -------
    fig: matplotlib figure with a new axis added with LrLx plotted.
    
    """
    
    # BW print-friendly color palette adopted from CubeHelix by Matt Davis
    colorset = ['#000000', '#00270C', '#00443C', '#005083', 
                '#034BCA', '#483CFC', '#9C2BFF', '#EB24F4', 
                '#FF2DC2', '#FF4986', '#FF7356', '#FFA443', 
                '#EBD155', '#D3F187', '#D7FFC8', '#FFFFFF']


    # Matplotlib configuration to emulate text with LaTeX
    # By default it is off, set usetex=True to change.
    rc('text', usetex=False)
    rc('font', **{'family' : 'serif'})
    
    ax = fig.add_subplot(1,1,1)

    no_uplimdata = data[data['uplim'] == 'None']
    uplimdata = data[data['uplim'] != 'None']

    # Detection data points:
    if 'BH' in classes:
        cond = no_uplimdata['Class'] == 'BH'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  'o',ms=4, c=colorset[2],mec='k',zorder=2,mew=0.3,label='Quiescent/hard state BHs')
    if 'candidateBH' in classes:
        cond = no_uplimdata['Class'] == 'candidateBH'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  'o',ms=6, c=colorset[6],mec='k',mew=0.2,zorder=3,label='Lr/Lx BH candidates')
    if 'NS' in classes:
        cond = no_uplimdata['Class'] == 'NS'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  's',ms=5, c=colorset[4],mec='k',mew=0.3,zorder=3,label='Quiescent/hard state NSs')
    if 'candidateNS' in classes:
        cond = no_uplimdata['Class'] == 'candidateNS'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  'v',ms=8, c=colorset[12],mec='k',mew=0.2,zorder=3,label='Lr/Lx NS candidates')
    if 'AMXP' in classes:
        cond = no_uplimdata['Class'] == 'AMXP'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  '*',ms=10,c=colorset[9],mec='k',mew=0.2,zorder=5,label='AMXPs')
    if 'tMSP' in classes:
        cond = no_uplimdata['Class'] == 'tMSP'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  '^',ms=8,c=colorset[14],mec='k',mew=0.2,zorder=2,label='tMSPs (in accretion state)')
    if 'WD' in classes:
        cond = no_uplimdata['Class'] == 'WD'
        ax.loglog(no_uplimdata[cond]['Lx'],no_uplimdata[cond]['Lr'],
                  'd',ms=8, c=colorset[10],mec='k',mew=0.2,zorder=6,label='WDs')
    
    # Plotting errorbars (if available):
    if errorbars and uplims:
        errorbardata = data[data['Class'].isin(classes)]
        ax.errorbar(x=errorbardata['Lx'], y=errorbardata['Lr'], 
                    yerr=[errorbardata['Lr_ler'],errorbardata['Lr_uer']], 
                    xerr=[errorbardata['Lx_ler'],errorbardata['Lx_uer']],
                    fmt='.', ms=0,ecolor='k', zorder=0, elinewidth=0.8)

    elif errorbars and ~uplims:
        errorbardata = no_uplimdata[no_uplimdata['Class'].isin(no_uplimdata)]
        ax.errorbar(x=errorbardata['Lx'], y=errorbardata['Lr'], 
                    yerr=[errorbardata['Lr_ler'],errorbardata['Lr_uer']], 
                    xerr=[errorbardata['Lx_ler'],errorbardata['Lx_uer']],
                    fmt='.', ms=0,ecolor='k', zorder=0, elinewidth=0.8)

    # Plotting upper limits:
    if uplims:
        if 'BH' in classes:
            cond = uplimdata['Class'] == 'BH'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      'o',ms=4, mec=colorset[2], mfc='w',zorder=2,mew=1)
        if 'candidateBH' in classes:
            cond = uplimdata['Class'] == 'candidateBH'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      'o',ms=6, mec=colorset[6],mfc='w',mew=1,zorder=3)
        if 'NS' in classes:
            cond = uplimdata['Class'] == 'NS'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      's',ms=5, mec=colorset[4],mfc='w',mew=1,zorder=3)
        if 'candidateNS' in classes:
            cond = uplimdata['Class'] == 'candidateNS'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      'v',ms=8, mec=colorset[12],mfc='w',mew=1,zorder=3)
        if 'AMXP' in classes:
            cond = uplimdata['Class'] == 'AMXP'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      '*',ms=10,mec=colorset[9],mfc='w',mew=1,zorder=5)
        if 'tMSP' in classes:
            cond = uplimdata['Class'] == 'tMSP'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      '^',ms=8,mec=colorset[14],mfc='w',mew=1,zorder=2)
        if 'WD' in classes:
            cond = uplimdata['Class'] == 'WD'
            ax.loglog(uplimdata[cond]['Lx'],uplimdata[cond]['Lr'],
                      'd',ms=8, mec=colorset[10],mfc='w',mew=1,zorder=6)
        
    
        
        Xlimit_data = data[data['Class'].isin(classes) & (data['uplim']=='Lx')]
        ax.errorbar(x=Xlimit_data['Lx'], 
                    y=Xlimit_data['Lr'], 
                    xerr=Xlimit_data['Lx']*0.5, xuplims=True,
                    fmt='.', ms=0,ecolor='k', zorder=0, elinewidth=0.8)
        Rlimit_data = data[data['Class'].isin(classes) & (data['uplim']=='Lr')]
        ax.errorbar(x=Rlimit_data['Lx'], 
                    y=Rlimit_data['Lr'], 
                    yerr=Rlimit_data['Lr']*0.5, uplims=True,
                    fmt='.', ms=0,ecolor='k', zorder=0, elinewidth=0.8)

    if cor_lines:
        # Plotting fitted lines:
        fit_x = np.logspace(29,39,num=10,base=10)
        # BH
        ax.loglog(fit_x,pow(10,(29.65+0.15-(0.61*36.32)))*pow(fit_x,0.61),
                  'k--',zorder=1,alpha=0.5)
        # NS:
        #plt.loglog(fit_x,pow(10,(28.59-(1.4*36.62)))*pow(fit_x,1.4),'-.',c='#73C1F9',zorder=1)
        #plt.loglog(fit_x,pow(10,(28.59-(0.7*36.62)))*pow(fit_x,0.7),'--',c='#73C1F9',zorder=1)
        # tMSP:
        #plt.loglog(fit_x,pow(10,(28.95+0.15-(0.61*36.32)))*pow(fit_x,0.61),c='#1AD668',ls=':',lw=1,zorder=1)

    
    
    # Artist functions:
    ax.legend()
    ax.set_xlabel(r'1-10 keV X-ray luminosity (erg s$^{-1}$)', fontsize=16)
    ax.set_xlim(1.01e29, 1e39)
    ax.set_ylabel(r'5-GHz radio luminosity (erg s$^{-1}$)', fontsize=16)
    ax.set_ylim(1e25, 3e31)
    ax.tick_params('both', length=9, width=1, which='major')
    ax.tick_params('both', length=5, width=1, which='minor')
    ax.tick_params(axis='both', which='major', labelsize=16)
    ax.tick_params(axis='both', which='both',direction='in',right=True,top=True)

    return fig


def main_function():
    DATA = data_reader()
    CLASSES = ['BH', 'candidateBH', 'NS', 'candidateNS', 'AMXP', 'tMSP', 'WD']   
    FIG = plt.figure(figsize=(8,6))
    plotter(DATA,CLASSES,fig=FIG, uplims=True);
    FIG.savefig('lrlx_plot.jpg', dpi=300, bbox_inches='tight')
    
    return FIG

main_function();
