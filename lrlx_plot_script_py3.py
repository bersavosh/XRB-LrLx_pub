################################################################################
#
# XRB-LrLx_pub
# Python Script to produce LR-Lx plot for BHs, NSs, CVs, etc.
#
# Github page: https://github.com/bersavosh/XRB-LrLx_pub
#
# Developed and maintained by Arash Bahramian 
#
################################################################################

import numpy as np
import matplotlib.pyplot as plt
import pickle

# For reading from the CSV file:
from astropy.io import ascii

# BW print-friendly color palette adopted from CubeHelix by Matt Davis
colorset = ['#000000', '#00270C', '#00443C', '#005083', '#034BCA', '#483CFC', '#9C2BFF', '#EB24F4', '#FF2DC2', '#FF4986', '#FF7356', '#FFA443', '#EBD155', '#D3F187', '#D7FFC8', '#FFFFFF']

# Matplotlib configuration to emulate text with LaTeX
from matplotlib import rc
rc('text', usetex=True)
font = {'family' : 'serif'}
rc('font', **font)

# Loading the pre-compiled catalog in pickle format
src_list = pickle.load(open('lrlx_data.p', 'rb'), encoding='latin1')
# Reading from CSV:
#src_list = ascii.read('lrlx_data.csv')


plt.figure(figsize=(8,6))
for i in src_list:
    # Plotting each class with different markers:
    if i['Class'] == 'BH':
        BHs,=plt.loglog(i['Lx'],i['Lr'],'o',ms=4, c=colorset[2],mec='k',zorder=2,mew=0.3,label='Quiescent/hard state BHs')
    if i['Class'] == 'NS':
        NSs,=plt.loglog(i['Lx'],i['Lr'],'s',ms=5, c=colorset[4],mec='k',mew=0.3,zorder=3,label='Quiescent/hard state NSs')
    if i['Class'] == 'AMXP':
        AMXPs,=plt.loglog(i['Lx'],i['Lr'],'*',ms=10,c=colorset[9],mec='k',mew=0.2,zorder=5,label='AMXPs')
    if i['Class'] == 'tMSP':
        tMSPs,=plt.loglog(i['Lx'],i['Lr'],'^',ms=8,c=colorset[14],mec='k',mew=0.2,zorder=2,label='tMSPs (in accretion state)')
    if i['Class'] == 'LrLx_BH':
        LrLxBHs,=plt.loglog(i['Lx'],i['Lr'],'o',ms=6, c=colorset[6],mec='k',mew=0.2,zorder=3,label=r'Lr/Lx BH candidates')
    if i['Class'] == 'LrLx_NS':
        LrLxNSs,=plt.loglog(i['Lx'],i['Lr'],'v',ms=8, c=colorset[12],mec='k',mew=0.2,zorder=3,label=r'Lr/Lx NS candidates')
    if i['Class'] == 'CV':
        CVs,=plt.loglog(i['Lx'],i['Lr'],'d',ms=8, c=colorset[10],mec='k',mew=0.2,zorder=6,label='CVs (at flare peak)')
    if i['Class'] == 'UI':
        UIs,=plt.loglog(i['Lx'],i['Lr'],'p',ms=8, c=colorset[8],mec='k',mew=0.2,zorder=8,label='Unknown')

    # Plotting errorbars (if available):
    # If reading the pickle file:
    if len(i['Lx_er']) > 0 and len(i['Lr_er']) > 0:
        plt.errorbar(i['Lx'],i['Lr'],yerr=i['Lr_er'],xerr=i['Lx_er'], fmt='.',ms=0,ecolor='k',zorder=2,elinewidth=0.8)
    # If reading a CSV file (comment the lines above and uncomment the ones below):
    #if i['Lx_ler'] > 0 and i['Lr_ler'] > 0:
    #    plt.errorbar(i['Lx'],i['Lr'],yerr=[[i['Lr_ler']],[i['Lr_uer']]],
    #                 xerr=[[i['Lx_ler']],[i['Lx_uer']]], fmt='.',ms=0,ecolor='k',zorder=2,elinewidth=0.8)



    # Upper limits:
    # Given the clutter in the plot, to show upper limits clearer, I make upper limit data points hallow
    if i['uplim'] != None:
        if i['Class'] == 'BH':
            plt.loglog(i['Lx'],i['Lr'],'o',ms=4, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'NS':
            plt.loglog(i['Lx'],i['Lr'],'s',ms=3, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'AMXP':
            plt.loglog(i['Lx'],i['Lr'],'*',ms=5, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'tMSP':
            plt.loglog(i['Lx'],i['Lr'],'^',ms=4, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'LrLx_BH':
            plt.loglog(i['Lx'],i['Lr'],'o',ms=3, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'LrLx_NS':
            plt.loglog(i['Lx'],i['Lr'],'v',ms=4, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'CV':
            plt.loglog(i['Lx'],i['Lr'],'d',ms=4, c='w',mec='k',mew=0.0,zorder=20)
        if i['Class'] == 'UI':
            plt.loglog(i['Lx'],i['Lr'],'p',ms=4, c='w',mec='k',mew=0.0,zorder=20)
    if i['uplim'] == 'Lx' and i['Class'] == 'AMXP':
        plt.errorbar(i['Lx'],i['Lr'],xerr=i['Lx']*0.6, fmt='.', ms=0, xuplims=True,ecolor='k',capsize=0,zorder=5,elinewidth=0.8)
    if i['uplim'] == 'Lr' and i['Class'] == 'AMXP':
        plt.errorbar(i['Lx'],i['Lr'],yerr=i['Lr']*0.5, fmt='.', ms=0, uplims=True,ecolor='k',capsize=0,zorder=5,elinewidth=0.8)
    if i['uplim'] == 'Lx' and i['Class'] != 'AMXP':
        plt.errorbar(i['Lx'],i['Lr'],xerr=i['Lx']*0.6, fmt='.', ms=0, xuplims=True,ecolor='k',capsize=0,zorder=3,elinewidth=0.8)
    if i['uplim'] == 'Lr' and i['Class'] != 'AMXP':
        plt.errorbar(i['Lx'],i['Lr'],yerr=i['Lr']*0.5, fmt='.', ms=0, uplims=True,ecolor='k',capsize=0,zorder=3,elinewidth=0.8)    

# Legends:
if 'UIs' in globals():
    plt.legend(handles=[BHs,LrLxBHs,NSs,LrLxNSs,AMXPs,tMSPs,CVs,UIs],loc=2,numpoints=1,fontsize=12)
else:
    plt.legend(handles=[BHs,LrLxBHs,NSs,LrLxNSs,AMXPs,tMSPs,CVs],loc=2,numpoints=1,fontsize=12)


# Plotting fitted lines:
# While BH systems tend to show a correlation, this seems not to be a case for NS systems anymore
# Thus, plotting them could be misleading and hence not recommended.
fit_x = np.logspace(29,39,num=10,base=10)
# BH:
plt.loglog(fit_x,pow(10,(29.65+0.15-(0.61*36.32)))*pow(fit_x,0.61),'k--',zorder=1,alpha=0.5)
# NS:
#plt.loglog(fit_x,pow(10,(28.59-(1.4*36.62)))*pow(fit_x,1.4),'-.',c='#73C1F9',zorder=1)
#plt.loglog(fit_x,pow(10,(28.59-(0.7*36.62)))*pow(fit_x,0.7),'--',c='#73C1F9',zorder=1)
# tMSP:
#plt.loglog(fit_x,pow(10,(28.95+0.15-(0.61*36.32)))*pow(fit_x,0.61),c='#1AD668',ls=':',lw=1,zorder=1)

# Artist functions:
plt.xlabel(r'1-10 keV X-ray luminosity (erg s$^{-1}$)', fontsize=16)
plt.xlim(1.01e29, 1e39)
plt.ylabel(r'5-GHz radio luminosity (erg s$^{-1}$)', fontsize=16)
plt.ylim(1e25, 3e31)
plt.tick_params('both', length=9, width=1, which='major')
plt.tick_params('both', length=5, width=1, which='minor')
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tick_params(axis='both', which='both',direction='in',right=True,top=True)

# Saving
plt.savefig('./lrlx_plot.pdf', bbox_inches='tight')
