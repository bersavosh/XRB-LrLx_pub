# Radio/X-ray correlation database for X-ray binaries

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6956521.svg)](https://zenodo.org/record/6956521) 
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bersavosh/XRB-LrLx_pub)](https://github.com/bersavosh/XRB-LrLx_pub/releases/tag/v0.2) 
[![GitHub](https://img.shields.io/github/license/bersavosh/XRB-LrLx_pub)](https://github.com/bersavosh/XRB-LrLx_pub/blob/master/LICENSE)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bersavosh/XRB-LrLx_pub/HEAD?labpath=quick_plotter.ipynb)

*[Bahramian et al. 2018](http://doi.org/10.5281/zenodo.1252035)* - Last update: Aug 3, 2022

This is a database for radio and X-ray observation of X-ray binaries based on published data in the literature. It also includes a simple python script to visualize the data.

For quick plotting of new sources, you can launch [this Binder instance](https://mybinder.org/v2/gh/bersavosh/XRB-LrLx_pub/HEAD?labpath=quick_plotter.ipynb).

## Contents

- [Introduction](https://github.com/bersavosh/XRB-LrLx_pub#introduction)
- [Package Description](https://github.com/bersavosh/XRB-LrLx_pub#Package-Description)
- [List of sources](https://github.com/bersavosh/XRB-LrLx_pub#list-of-sources)
- [List of updates](https://github.com/bersavosh/XRB-LrLx_pub#list-of-updates)
- [Warnings and cautions](https://github.com/bersavosh/XRB-LrLx_pub#warnings-and-cautions)
  - [Sampling issues](https://github.com/bersavosh/XRB-LrLx_pub#sampling-issues)
  - [Odd sources](https://github.com/bersavosh/XRB-LrLx_pub#odd-sources)
  - [tMSPs](https://github.com/bersavosh/XRB-LrLx_pub#tmsps)
  - [Correlation lines](https://github.com/bersavosh/XRB-LrLx_pub#correlation-lines)
- [Using and citing this package](https://github.com/bersavosh/XRB-LrLx_pub#using-and-citing-this-package)
- [Plot](https://github.com/bersavosh/XRB-LrLx_pub#plot)

## Introduction

The radio-X-ray correlation in accreting neutron stars and black holes has been discussed in detail in the literature. BH X-ray binaries (XRBs) show compact partially self-absorbed jet emission in quiescence and in the hard state during outbursts, making them brighter in radio compared to NS LMXBs with similar X-ray luminosities (Fender,Gallo & Jonker 2003; Gallo, Fender & Pooley 2003; Maccarone 2005, Migliari & Fender 2006). Since, there have been numerous efforts at further exploring and understanding this correlation. Numerous sources (both known and newly identified) have been observed in radio and X-rays. Here, we have compiled a collection of these measurements from the literature and we actively add new measurements as we notice new publications.

Many of these measurements have been done/reported in different radio and X-ray bands. To allow comparison, we convert all of these measurements to 5 GHz (in radio) and 1-10 keV (in X-rays). For these conversions, we generally assume a flat spectrum in the radio and use the best known photon index (assuming a power-law model) in the X-rays.

## Package Description

**Data**: A catalog of radio and X-ray observations of Galactic X-ray binaries broken down based on system class. The data are stored in `.csv` format in the "data" directory, with all systems within a single system class included in a single file. Each data file has the following columns:

- `Name` : Name of the source.
- `Class` : System class, see [System types](https://github.com/bersavosh/XRB-LrLx_pub#system-types) for details.
- `Lr` : Radio luminosity of the source in the 5 GHz band.
- `Lr_ler` : Lower uncertainty on `Lr`.
- `Lr_uer` : Upper uncertainty on `Lr`.
- `Lx` : X-ray luminosity of the source in the 1-10 keV band.
- `Lx_ler` : Lower uncertainty on `Lx`.
- `Lx_uer` : Upper uncertainty on `Lx`.
- `uplim` : Indicating whether the reported data point contains an upperlimit. `"None"` indicates both reported `"Lr"` and `"Lx"` for the point are detections. String of `Lr` or `Lx` in this columns indicates non-detection and uppoer limit value for radio or X-rays respectively.
- `Ref` : The reference publication for the data point.

**Script**: This package also contains a simple Python script to plot these data using `Matplotlib` and `Pandas` and allow easy modification to create your own version of the plot. The default output of this script is shown [here](https://github.com/bersavosh/XRB-LrLx_pub#plot).

**Notebooks**: There are also two notebooks, 


## List of sources

All the sources included in this database and plot are tabulated below.

### System types

- BH: Black hole XRBs (both confirmed and candidates).
- candidateBH: Candidate black hole XRB systems which are classified based on radio/X-ray correlation.
- NS: Neutros star XRBs (confirmed through type 1 X-ray bursts or pulsations)
- candidateNS: Candidate neutron star XRB systems which are classified based on radio/X-ray correlation.
- tMSP: Transitional Millisecond Pulsars (observations during accreting states - as opposed to pulsar state)
- AMXP: Accreting millisecond X-ray pulsars
- WD: White dwarf systems including cataclysmic variables (observations at or near flare peak) and other unusual WDs with bright radio detection.

|                   Name |    Type | Golbular Cluster |                                                                                                 Reference |
|------------------------|---------|------------------|-----------------------------------------------------------------------------------------------------------|
|               A0620-00 |      BH |             None |                                      Gallo et al. 2006, MNRAS, 370, 1351; Dincer et al. 2018, ApJ, 852, 4 |
|          XTE J1118+480 |      BH |             None |                                  Fender et al. 2010, MNRAS, 406, 1425; Gallo et al. 2014, MNRAS, 445, 290 |
|               GX 339-4 |      BH |             None |                                                                      Corbel et al. 2013, MNRAS, 428, 2500 |
|             H 1743-322 |      BH |             None |                                                                       Coriat et al. 2011, MNRAS, 414, 677 |
|              V 404 Cyg |      BH |             None | Corbel et al. 2008, MNRAS, 389, 1697; Rana et al. 2016, ApJ, 821, 103; Plotkin et al. 2017, ApJ, 834, 104 |
|     Swift J1753.5-0127 |      BH |             None | Soleri et al. 2010 MNRAS 406 1471; Rushton et al. 2016 MNRAS, 463, 628, Plotkin et al. 2017, ApJ, 848, 92 |
|         MAXI J1659-152 |      BH |             None |                                                                      Jonker et al. 2012, MNRAS, 423, 3308 |
|          XTE J1752-223 |      BH |             None |                               Ratti et al. 2012, MNRAS, 423, 2656; Brocksopp et al. 2013, MNRAS, 432, 931 |
|                MWC 656 |      BH |             None |                                                                            Ribo et al. 2017, ApJ, 835, 33 |
|         MAXI J1836-194 |      BH |             None |                                                                     Russell et al. 2015, MNRAS, 450, 1745 |
|           GRO J1655-40 |      BH |             None |                           Coriat et al. 2011, IAU Symp 275, 255; Calvelo, D. et al. 2010, MNRAS, 409, 839 |
|          XTE J1550-564 |      BH |             None |                                                                         Gallo et al. 2003, MNRAS, 344, 60 |
|          XTE J1720-318 |      BH |             None |                                                                    Brocksopp et al. 2005, MNRAS, 356, 125 |
|        IGR J17177-3656 |      BH |             None |                                                                         Paizis et al. 2011, ApJ, 738, 183 |
|           GRS 1758-258 |      BH |             None |                                                                         Gallo et al. 2003, MNRAS, 344, 60 |
|        IGR J17091-3624 |      BH |             None |                                                                       Rodriguez et al. 2011, A&A, 533, L4 |
|             GS 1354-64 |      BH |             None |                                                                         Gallo et al. 2003, MNRAS, 344, 60 |
|             4U 1543-47 |      BH |             None |                                                                         Gallo et al. 2003, MNRAS, 344, 60 |
|          XTE J1650-500 |      BH |             None |                                                                        Corbel et al. 2004, ApJ, 617, 1272 |
|               M62-VLA1 | candidateBH |          M62 |                                             Chomiuk et al. 2013, ApJ, 777, 69; Bahramian et al., in prep. |
|             M22-VLA1,2 | candidateBH |          M22 |                                                                       Strader et al. 2012, Natur, 490, 71 |
|               47Tuc X9 | candidateBH |        47Tuc |                       Miller-Jones et al. 2015, MNRAS, 453, 3918; Bahramian et al. 2017, MNRAS, 467, 2199 |
|           VLA J2130+12 | candidateBH |         None |                                                                    B. Tetarenko et al. 2016, ApJ, 825, 10 |
|               M10-VLA1 | candidateBH |          M10 |                                                                  Shishkovsky et al. 2018, ApJ., in press. |
|        XSS J12270-4859 |    tMSP |             None |                                                                         Hill et al. 2011, MNRAS, 415, 235 |
|        IGR J18245-2452 |    tMSP |              M28 |                                                                      Papitto et al. 2013, Natur, 501, 517 |
|         PSR J1023+0038 |    tMSP |             None |                                 Deller et al. 2015, ApJ, 809, 13; Bogdanov et al. 2017, arXiv, 1711.04791 |
|           EXO 1745-248 |      NS |          Terzan5 |                                                                 A. Tetarenko et al. 2016, MNRAS, 460, 345 |
|           EXO 1745-248 |      NS |          Terzan5 |                                                                 A. Tetarenko et al. 2016, MNRAS, 460, 345 |
|                Cen X-4 |      NS |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|                Cen X-4 |      NS |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|  1RXS J180408.9-342058 |      NS |             None |                                                                 Gusinskaia et al., 2017, MNRAS, 470, 1871 |
|  1RXS J180408.9-342058 |      NS |             None |                                                                 Gusinskaia et al., 2017, MNRAS, 470, 1871 |
|         MAXI J0556-332 |      NS |             None |                                                                           Coriat et al., 2011, ATel, 3119 |
|           MXB 1730-335 |      NS |             None |                                                                             Rutledge et al. 1998, ATel, 8 |
|                Aql X-1 |      NS |             None |                                                                    Migliari et al. 2011, MNRAS, 415, 2407 |
|             4U 1728-34 |      NS |             None |                                                                    Migliari et al. 2011, MNRAS, 415, 2407 |
|            4U 0614+091 |      NS |             None |                                                                    Migliari et al. 2011, MNRAS, 415, 2407 |
| Swift J175233.9-290952 | candidateNS |         None |                                                                        Tetarenko et al. 2017, ATel, 10422 |
|            4U 1543-624 | candidateNS |         None |                                                                           Ludham et al. 2017, ATel, 10690 |
|       SAX J1808.4-3658 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|        IGR J00291+5934 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|        IGR J00291+5934 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|        IGR J17511-3057 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|       SAX J1748.9-2021 |    AMXP |         NGC 6440 |                                 Miller-Jones et al., 2010, ATel, 2377; Tetarenko et al. 2017, ATel, 10843 |
|        IGR J16597-3704 |    AMXP |         NGC 6256 |                                                                        Tetarenko et al. 2017, ATel, 10894 |
|         MAXI J0911-635 |    AMXP |         NGC 2808 |                                                                             Tudor et al. 2016, ATel, 8914 |
|          XTE J0929-314 |    AMXP |             None |                                                                    Migliari et al. 2011, MNRAS, 415, 2407 |
|        IGR J17379-3747 |    AMXP |             None |                             van den Eijnden et al. 2018, ATel, 11487; Strohmayer et al. 2018, ATel, 11507 |
|        IGR J17591-2342 |    AMXP |             None |                              Russell et al. 2018, ApJL, 869, 16; Gusinskaia et al. 2020, MNRAS, 492, 1091 |
|                 SS Cyg |      WD |             None |                                                                     Russell et al. 2016, MNRAS, 460, 3720 |
|                 AE Aqr |      WD |             None |                              Eracleous et al. 1991, ApJ, 382, 290; Abada-Simon et al. 1993, ApJ, 406, 692 |
|                 AR Sco |      WD |             None |                                                                        Marsh et al. 2016, Natur, 537, 374 |

## List of updates

Since publication of the version published in [Tetarenko, B., et al. 2016](http://adsabs.harvard.edu/abs/2016ApJ...825...10T), the following updates have been applied (in chronological order):

- **MWC 656** updated based on [Ribo et al. 2017](http://adsabs.harvard.edu/abs/2017ApJ...835L..33R). Previous measurements (X-rays from [Munar-Adrover et al. 2014](http://adsabs.harvard.edu/abs/2014ApJ...786L..11M) and radio from [Dzib et al. 2015](http://adsabs.harvard.edu/abs/2015A&amp;A...580L...6D) were non-simultaneous).
- **EXO 1745-248** added based on [Tetarenko, A., et al. 2016](http://adsabs.harvard.edu/abs/2016MNRAS.460..345T).
- **M62 VLA1** updated based on Bahramian et al. in prep.
- **Swift J1753.5−0127** more data added based on [Rushton et al. 2016](http://adsabs.harvard.edu/abs/2016MNRAS.463..628R) and [Plotkin et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv170905242P).
- **New AMXPs and NSs added** Data for AMXPs IGR J00291+5934, SAX J1808.4-3658, IGR J17511-3057 and NS Cen X-4 (in quiescence) added from [Tudor et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470..324T).
- **SAX J1748.9-2021** added based on [Tetarenko et al. 2017](http://adsabs.harvard.edu/abs/2017ATel10843....1). Note: The observed X-ray activity (which Tetarenko et al.'s results are based on), is not yet been confirmed to be from SAX J1748.9-2021 (as opposed to other X-ray sources in globular cluster NGC 6440). However, this source is the most likely origin.
- **1RXS J180408.9-34205** added based on [Gusinskaia et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470.1871G).
- **Major update (Jan 2018)**:
  - New data points for MAXI J0911−635, SAX J1748.9−2021, Swift J175233.9-290952, 4U 1543−624, MAXI J0556−332, MXB 1730−335 based on [Tetarenko et al. 2018](https://ui.adsabs.harvard.edu/abs/2018ApJ...854..125T/abstract).
  - AR Scorpii added based on [Marsh et al. 2016](http://adsabs.harvard.edu/abs/2016Natur.537..374M).
  - New data points for "active" and "passive" accretion modes of PSR J1023+0038 addded based on [Bogdanov et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv170908574B).
  - Data for A0620-00 updated based on [Dincer et al. 2018](http://adsabs.harvard.edu/abs/2018ApJ...852....4D).
- **M10 VLA1** data added based on [Shishkovsky et al. 2018](http://adsabs.harvard.edu/abs/2018arXiv180201704S).
- **IGR J17379-3747** added based on [van den Eijnden et al. 2018](http://www.astronomerstelegram.org/?read=11487). NICER observations identified this transient as an AMXP ([Strohmayer et al. 2018](http://www.astronomerstelegram.org/?read=11507)).
- **Major update (Apr 2018)** We have now added multiple sources and more data to some exisiting sources based on archival studies (Motta et al., in prep.).
- **Release of Version 0.1 (May 2018)**
- **2020 update**:
  - A radio uppler limit data point for IGR J17511-3057 from [Tudor et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470..324T) was included here with a numerical error. The upper limit is 8e+27, and not 8e+28.
  - One omitted data point for IGR J00291+5934 ([Tudor et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470..324T)) is now included.
  - New source IGR J17591-2342 added based on [Russell et al. 2018](https://ui.adsabs.harvard.edu/abs/2018ApJ...869L..16R/abstract) and [Gusinskaia et al. 2020](https://ui.adsabs.harvard.edu/abs/2020MNRAS.492.1091G/abstract).
  - Thanks to Nina Gusinskaia for poiting out these issues and providing the data.
- **2022 update 1**
  - Data re-organized into multiple `csv` files based on source classes to facilitate contributions and updates.
  - Plotting script updated to incorporate better practices and switch dependencies from pickles and `astropy` tables to `pandas` dataframes.

## Warnings and cautions

### Sampling issues

**Simultaneity** - For most of these measurements, X-ray and radio observations have been simultaneous or quasi-simultaneous (within 1-2 days). However, we warn the user to check the original reference as some of these measurements might have been far apart in time.

**Bands, sensitivity, number of observations** - The data quality, depth of observations, number of observations per source, observatories (and hence the observation bands) vary strongly in this catalog. Some sources like XTE J1118+480 or Swift J1753.5-0127 have been covered over a broad range of luminosities and are also observed numerous times, while many other sources are not observed more than a handful of times.

**Distance** - Another issue in sampling is large distances (combined with telescope sensitivity limits), which hampers study of many of these sources at lower luminosities. This is a dominant factor as to why there are very few data points at Lr < 1e28 erg/s and Lx < 1e34 erg/s. It is also important to note that many of these distance measurements are extremely uncertain.

**Short-timescale variability** - It is important to note that almost all of the sources in this catalog show short-timescale variability. This can impcat observations and sampling, specially if observations are short. For example, the data points included for the CVs are specifically chosen to show these sources at their flare peak. Or, the three data points for PSR J1023+0038 show this source show it in low and high modes in faint accretion state and also the average for this state.

### Odd sources

To have a complete database, we have also added available data for Cyg X1 (based on Gallo et al. 2003, MNRAS, 344, 60) and GRS 1915+105 (based on Rushton et al. 2010, A&A, 524, 29). However, given these systems are generally classified as "unusual", we have separated them from the rest and they are not included in the plots and constructed dataframe by default. However, the data on these sources are available in the data directory and they can be included in the dataframe and plotting via `include_oddsources=True` in the `data_reader` function.

### tMSPs

Transitional millisecond pulsars are a relatively new group of sources on this plot. There are still only a hanful of confirmed tMSPs identified and thus their behavior (on the Lr-Lx plane) is not fully explored. A recent study by [Bogdanov et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv170908574B) indicates that in the faint accretion state, PSR J1023+0038 shows a strong anti-correlation between radio and X-ray luminosity. Based on the anti-correlation, it is also suggested that the radio emission might not be (entirely) from a self-absorbed jet. Thus, it is possible that comparing their radio and X-ray emission to other systems on this plot might not be appropriate.

### Correlation lines

As shown in [Tetarenko et al. 2018](http://adsabs.harvard.edu/abs/2018arXiv180105778T) and [Gallo et al. 2018](http://adsabs.harvard.edu/doi/10.1093/mnrasl/sly083) NS XRBs and AMXPs do not seem to follow the previously suggested correlation lines. Thus, these correlation lines are not shown in the plot. However these are still included as comments in the plotting script.

- The dotted black line shows the best-fit relation for BHs [Gallo et al. 2006](http://adsabs.harvard.edu/abs/2006MNRAS.370.1351G)
- The blue dashed and dashed-dotted lines show the two suggested correlations for NS systems [Migliari & Fender 2006](http://adsabs.harvard.edu/abs/2006MNRAS.366...79M)

## Using and citing this package

If this package/database is useful to you, we request that you cite the following record:

[Arash Bahramian et al. 2018; Radio/X-ray correlation database for X-ray binaries](https://zenodo.org/record/6956521)

Bibtex:

```bibtex
@software{arash_bahramian_2022_6956521,
  author       = {Arash Bahramian and
                  Anthony Rushton},
  title        = {bersavosh/XRB-LrLx\_pub: 2022 script update},
  month        = aug,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v0.2},
  doi          = {10.5281/zenodo.6956521},
  url          = {https://doi.org/10.5281/zenodo.6956521}
}
```

This repository is maintained and updated by [Arash Bahramian](https://bersavosh.github.io/). Feel free to contact me if you have suggestions/comments/questions.

Contributors: [Alex Tetarenko](https://sites.ualberta.ca/~tetarenk/), [James Miller-Jones](https://staffportal.curtin.edu.au/staff/profile/view/James.Miller-Jones), [Jay Strader](http://web.pa.msu.edu/people/strader/), [Richard Plotkin](https://staffportal.curtin.edu.au/staff/profile/view/Richard.Plotkin), [Anthony Rushton](http://www2.physics.ox.ac.uk/contacts/people/rushton), [Vlad Tudor](https://www.icrar.org/people/vtudor/), [Laura Shishkovsky](https://astro.natsci.msu.edu/people/laura-shishkovsky/), [Sara Motta](https://www.wadham.ox.ac.uk/people/fellows-and-academic-staff/m/sara-motta), [Nina Gusinskaia](https://www.astro.utoronto.ca/people/post-docs/name/nina-gusinskaia/).

## Plot

<img src="https://raw.githubusercontent.com/bersavosh/XRB-LrLx_pub/master/lrlx_plot.jpg" width="800">
