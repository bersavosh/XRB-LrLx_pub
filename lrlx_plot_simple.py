# Python Script to make LR-Lx plot for BHs, NSs, CVs, etc.
# THIS IS THE SIMPLE VERSION: it reads from a pre-compiled database
# This script uses Numpy, Astropy and Matplotlib
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import pickle

# Matplotlib configuration to emulate text with LaTeX
from matplotlib import rc
rc('text', usetex=True)
font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : '14'}
rc('font', **font)

# Data format: Both txt and pickle are available:
data_fmt = 'txt'
#data_fmt = 'pickle'

if data_fmt == 'txt':
    src_list = ascii.read('lrlx_data.csv')

if data_fmt == 'pickle':
    src_list = pickle.load(open('lrlx_data.p', 'rb' ))

plt.figure(figsize=(8,6))

for i in src_list:
    # Plotting each class with different markers:
    if i['Class'] == 'BH':
        BHs,=plt.loglog(i['Lx'],i['Lr'],'o',ms=4, c='k',mec='k',zorder=2,label='Quiescent/hard state BHs')
    if i['Class'] == 'NS':
        NSs,=plt.loglog(i['Lx'],i['Lr'],'s',ms=5, c='#73C1F9',mec='k',mew=0.3,zorder=3,label='Hard state NSs')
    if i['Class'] == 'AMXP':
        AMXPs,=plt.loglog(i['Lx'],i['Lr'],'*',ms=10,c='#F45FE0',mec='k',mew=0.2,zorder=3,label='AMXPs')
    if i['Class'] == 'tMSP':
        tMSPs,=plt.loglog(i['Lx'],i['Lr'],'^',ms=8,c='#1AD668',mec='k',mew=0.2,zorder=2,label='tMSPs (in accretion state)')
    if i['Class'] == 'LrLx_BH':
        LrLxBHs,=plt.loglog(i['Lx'],i['Lr'],'o',ms=8, c='#F7ED57',mec='k',mew=0.2,zorder=3,label=r'Lr/Lx BH candidates')
    if i['Class'] == 'CV':
        CVs,=plt.loglog(i['Lx'],i['Lr'],'d',ms=8, c='#8407F1',mec='k',mew=0.2,zorder=6,label='CVs (at flare peak)')
    if i['Class'] == 'UI':
        UIs,=plt.loglog(i['Lx'],i['Lr'],'p',ms=8, c='r',mec='k',mew=0.2,zorder=8,label='New GC BH candidates')

    if data_fmt == 'pickle':
        # Plotting errorbars (if available):
        if len(i['Lx_er']) > 0 and len(i['Lr_er']) > 0:
                plt.errorbar(i['Lx'],i['Lr'],yerr=i['Lr_er'],xerr=i['Lx_er'], fmt='.',ms=0,ecolor='k',zorder=2)
        # Upper limits:    
        if i['uplim'] == 'Lx':
           plt.errorbar(i['Lx'],i['Lr'],xerr=i['Lx']*0.6, fmt='.', ms=0, xuplims=True,ecolor='k',capsize=0,zorder=3)
        if i['uplim'] == 'Lr':
            plt.errorbar(i['Lx'],i['Lr'],yerr=i['Lr']*0.5, fmt='.', ms=0, uplims=True,ecolor='k',capsize=0,zorder=3)

    if data_fmt == 'txt':
        # Plotting errorbars (if available):
        plt.errorbar(i['Lx'],i['Lr'],yerr=[[i['Lr_ler']],[i['Lr_uer']]],xerr=[[i['Lx_ler']],[i['Lx_uer']]], fmt='.',ms=0,ecolor='k',zorder=2)
        # Upper limits:    
        if i['uplim'] == 'Lx':
            plt.errorbar(i['Lx'],i['Lr'],xerr=i['Lx']*0.6, fmt='.', ms=0, xuplims=True,ecolor='k',capsize=0,zorder=3)
        if i['uplim'] == 'Lr':
            plt.errorbar(i['Lx'],i['Lr'],yerr=i['Lr']*0.5, fmt='.', ms=0, uplims=True,ecolor='k',capsize=0,zorder=3)

# Legends:
if 'UIs' in globals():
    plt.legend(handles=[BHs,LrLxBHs,NSs,AMXPs,tMSPs,CVs,UIs],loc=2,numpoints=1,fontsize=12)
else:
    plt.legend(handles=[BHs,LrLxBHs,NSs,AMXPs,tMSPs,CVs],loc=2,numpoints=1,fontsize=12)

# Plotting fitted lines:
fit_x = np.logspace(29,39,num=10,base=10)
# BH:
plt.loglog(fit_x,pow(10,(29.65+0.15-(0.61*36.32)))*pow(fit_x,0.61),'k--',zorder=1)
# NS:
plt.loglog(fit_x,pow(10,(28.59-(1.4*36.62)))*pow(fit_x,1.4),'-.',c='#73C1F9',zorder=1)
plt.loglog(fit_x,pow(10,(28.59-(0.7*36.62)))*pow(fit_x,0.7),'--',c='#73C1F9',zorder=1)
# tMSP:
plt.loglog(fit_x,pow(10,(28.95+0.15-(0.61*36.32)))*pow(fit_x,0.61),c='#1AD668',ls=':',lw=1,zorder=1)

#########################
# ADD YOUR DATA POINTS HERE:
# plt.errorbar(Lx,Lr,yerr=Lr_er,xerr=Lx_err)

#########################


# Artist functions:
plt.xlabel(r'1-10 keV X-ray luminosity (erg s$^{-1}$)', fontsize=16)
plt.xlim(1.01e29, 1e39)
plt.ylabel(r'5-GHz radio luminosity (erg s$^{-1}$)', fontsize=16)
plt.ylim(1e25, 2e31)
plt.tick_params('both', length=9, width=1, which='major')
plt.tick_params('both', length=5, width=1, which='minor')
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tick_params(axis='both', which='both',direction='in',right='on',top='on')

# Saving
plt.savefig('./lrlx_plot_simple.pdf', bbox_inches='tight')
