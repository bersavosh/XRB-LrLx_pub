# Radio/X-ray correlation database for X-ray binaries

*[Bahramian et al. 2018](http://doi.org/10.5281/zenodo.1252035)*

This is a database for radio and X-ray observation of X-ray binaries based on published data in the literature. There is also a simple python script to make the plot.

*Last update: May 24, 2018 (Version 0.1)*

## Contents:
   - [Introduction](https://github.com/bersavosh/XRB-LrLx_pub#introduction)
   - [Package Description](https://github.com/bersavosh/XRB-LrLx_pub#Package-Description)
   - [List of sources](https://github.com/bersavosh/XRB-LrLx_pub#list-of-sources)
   - [List of updates](https://github.com/bersavosh/XRB-LrLx_pub#list-of-updates)
   - [Warnings and cautions](https://github.com/bersavosh/XRB-LrLx_pub#warnings-and-cautions)
      - [Sampling issues](https://github.com/bersavosh/XRB-LrLx_pub#sampling-issues)
      - [Odd sources](https://github.com/bersavosh/XRB-LrLx_pub#odd-sources)
      - [tMSPs](https://github.com/bersavosh/XRB-LrLx_pub#tmsps)
      - [Correlation lines](https://github.com/bersavosh/XRB-LrLx_pub#correlation-lines)
   - [Acknowledgment](https://github.com/bersavosh/XRB-LrLx_pub#Acknowledgment)
   - [Plots](https://github.com/bersavosh/XRB-LrLx_pub#plots)

## Introduction:
The radio-X-ray correlation in accreting neutron stars and black holes has been discussed in detail in the literature. BH X-ray binaries (XRBs) show compact partially self-absorbed jet emission in quiescence and in the hard state during outbursts, making them brighter in radio compared to NS LMXBs with similar X-ray luminosities (Fender,Gallo & Jonker 2003; Gallo, Fender & Pooley 2003; Maccarone 2005, Migliari & Fender 2006). Since, there have been numerous efforts at further exploring and understanding this correlation. Numerous sources (both known and newly identified) have been observed in radio and X-rays. Here, we have compiled a collection of these measurements from the literature and we actively add new measurements as we notice new publications. 

Many of these measurements have been done/reported in different radio and X-ray bands. To allow comparison, we convert all of these measurements to 5 GHz (in radio) and 1-10 keV (in X-rays). For these conversions, we assume a flat radio spectrum in radio and use the best known photon index (assuming a power-law model) in X-rays.

## Package Description:
This package contains a catalog of radio and X-ray observations of Galactic X-ray binaries. The catalog is available in form of a `csv` file ([lrlx_data.csv](https://github.com/bersavosh/XRB-LrLx_pub/blob/master/lrlx_data.csv)) and a python [pickle](https://docs.python.org/3/library/pickle.html) file ([lrlx_data.p](https://github.com/bersavosh/XRB-LrLx_pub/blob/master/lrlx_data.p)). The pickle contains each source as an object with defined attributes such as name, class (BH-XRB, NS-XRB, tMSP, CV, etc.), reference, and measurements and uncertainties as arrays.

Additionally, there are sources which are considered "unusual" for their accretion behavior (see [Odd sources](https://github.com/bersavosh/XRB-LrLx_pub#odd-sources)). For completeness, we have included these sources in a different file ([lrlx_odd_srcs.csv](https://github.com/bersavosh/XRB-LrLx_pub/blob/master/lrlx_odd_srcs.csv)).

There is also a simple python script available ([lrlx_plot_script.py](https://github.com/bersavosh/XRB-LrLx_pub/blob/master/lrlx_plot_script.py)) which utilizes [Matplotlib](https://matplotlib.org/) to produces [this plot](https://github.com/bersavosh/XRB-LrLx_pub#the-lr-lx-plot-with-sources-markedcolored-by-class).

## List of sources:
All the sources included in this database and plot are tabulated below. Additionally, a version of the plot with all sources labeled is available [here](https://raw.githubusercontent.com/bersavosh/XRB-LrLx_pub/master/lrlx_plot_byname.jpg).

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
|               M62-VLA1 | LrLx_BH |              M62 |                                             Chomiuk et al. 2013, ApJ, 777, 69; Bahramian et al., in prep. |
|             M22-VLA1,2 | LrLx_BH |              M22 |                                                                       Strader et al. 2012, Natur, 490, 71 |
|               47Tuc X9 | LrLx_BH |            47Tuc |                       Miller-Jones et al. 2015, MNRAS, 453, 3918; Bahramian et al. 2017, MNRAS, 467, 2199 |
|           VLA J2130+12 | LrLx_BH |             None |                                                                    B. Tetarenko et al. 2016, ApJ, 825, 10 |
|               M10-VLA1 | LrLx_BH |              M10 |                                                                  Shishkovsky et al. 2018, ApJ., in press. |
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
| Swift J175233.9-290952 | LrLx_NS |             None |                                                                        Tetarenko et al. 2017, ATel, 10422 |
|            4U 1543-624 | LrLx_NS |             None |                                                                           Ludham et al. 2017, ATel, 10690 |
|       SAX J1808.4-3658 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|        IGR J00291+5934 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|        IGR J00291+5934 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|        IGR J17511-3057 |    AMXP |             None |                                                                        Tudor et al. 2017, MNRAS, 470, 324 |
|       SAX J1748.9-2021 |    AMXP |         NGC 6440 |                                 Miller-Jones et al., 2010, ATel, 2377; Tetarenko et al. 2017, ATel, 10843 |
|        IGR J16597-3704 |    AMXP |         NGC 6256 |                                                                        Tetarenko et al. 2017, ATel, 10894 |
|         MAXI J0911-635 |    AMXP |         NGC 2808 |                                                                             Tudor et al. 2016, ATel, 8914 |
|          XTE J0929-314 |    AMXP |             None |                                                                    Migliari et al. 2011, MNRAS, 415, 2407 |
|        IGR J17379-3747 |    AMXP |             None |                             van den Eijnden et al. 2018, ATel, 11487; Strohmayer et al. 2018, ATel, 11507 |
|                 SS Cyg |      CV |             None |                                                                     Russell et al. 2016, MNRAS, 460, 3720 |
|                 AE Aqr |      CV |             None |                              Eracleous et al. 1991, ApJ, 382, 290; Abada-Simon et al. 1993, ApJ, 406, 692 |
|                 AR Sco |      CV |             None |                                                                        Marsh et al. 2016, Natur, 537, 374 |

## List of updates:
Since publication of the version published in [TetarBenko, B., et al. 2016](http://adsabs.harvard.edu/abs/2016ApJ...825...10T), the following updates have been applied (in chronological order):
- **MWC 656** updated based on [Ribo et al. 2017](http://adsabs.harvard.edu/abs/2017ApJ...835L..33R). Previous measurements (X-rays from [Munar-Adrover et al. 2014](http://adsabs.harvard.edu/abs/2014ApJ...786L..11M) and radio from [Dzib et al. 2015](http://adsabs.harvard.edu/abs/2015A&amp;A...580L...6D) were non-simultaneous).
- **EXO 1745-248** added based on [Tetarenko, A., et al. 2016](http://adsabs.harvard.edu/abs/2016MNRAS.460..345T).
- **M62 VLA1** updated based on Bahramian et al. in prep.
- **Swift J1753.5−0127** more data added based on [Rushton et al. 2016](http://adsabs.harvard.edu/abs/2016MNRAS.463..628R) and [Plotkin et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv170905242P).
- **New AMXPs and NSs added** Data for AMXPs IGR J00291+5934, SAX J1808.4-3658, IGR J17511-3057 and NS Cen X-4 (in quiescence) added from [Tudor et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470..324T).
- **SAX J1748.9-2021** added based on [Tetarenko et al. 2017](http://adsabs.harvard.edu/abs/2017ATel10843....1). Note: The observed X-ray activity (which Tetarenko et al.'s results are based on), is not yet been confirmed to be from SAX J1748.9-2021 (as opposed to other X-ray sources in globular cluster NGC 6440). However, this source is the most likely origin.
- **1RXS J180408.9-34205** added based on [Gusinskaia et al. 2017](http://adsabs.harvard.edu/abs/2017MNRAS.470.1871G).
- **Major update (Jan 2018)**:
    - New data points for MAXI J0911−635, SAX J1748.9−2021, Swift J175233.9-290952, 4U 1543−624, MAXI J0556−332, MXB 1730−335 based on [Tetarenko et al. 2018]().
    - AR Scorpii added based on [Marsh et al. 2016](http://adsabs.harvard.edu/abs/2016Natur.537..374M). 
    - New data points for "active" and "passive" accretion modes of PSR J1023+0038 addded based on [Bogdanov et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv170908574B).
    - Data for A0620-00	updated based on [Dincer et al. 2018](http://adsabs.harvard.edu/abs/2018ApJ...852....4D).
- **M10 VLA1** data added based on [Shishkovsky et al. 2018](http://adsabs.harvard.edu/abs/2018arXiv180201704S).
- **IGR J17379-3747** added based on [van den Eijnden et al. 2018](http://www.astronomerstelegram.org/?read=11487). NICER observations identified this transient as an AMXP ([Strohmayer et al. 2018](http://www.astronomerstelegram.org/?read=11507)).
- **Major update (Apr 2018)** We have now added multiple sources and more data to some exisiting sources based on archival studies ([Motta et al., in prep.]()).
- **Release of Version 0.1 (May 2018)** 

## Warnings and cautions:

### Sampling issues:
**Simultaneity** - For most of these measurements, X-ray and radio observations have been simultaneous or quasi-simultaneous (within 1-2 days). However, we warn the user to check the original reference as some of these measurements might have been far apart in time.

**Bands, sensitivity, number of observations** - The data quality, depth of observations, number of observations per source, observatories (and hence the observation bands) vary strongly in this catalog. Some sources like XTE J1118+480 or Swift J1753.5-0127 have been covered over a broad range of luminosities and are also observed numerous times, while many other sources are not observed more than a handful of times.

**Distance** - Another issue in sampling is large distances (combined with telescope sensitivity limits), which hampers study of many of these sources at lower luminosities. This is a dominant factor as to why there are very few data points at Lr < 1e28 erg/s and Lx < 1e34 erg/s. It is also important to note that many of these distance measurements are extremely uncertain.

**Short-timescale variability** - It is important to note that almost all of the sources in this catalog show short-timescale variability. This can impcat observations and sampling, specially if observations are short. For example, the data points included for the CVs are specifically chosen to show these sources at their flare peak. Or, the three data points for PSR J1023+0038 show this source show it in low and high modes in faint accretion state and also the average for this state.

### Odd sources:
To have a complete database, we have also added available data for Cyg X1 (based on Gallo et al. 2003, MNRAS, 344, 60) and GRS 1915+105 (based on Rushton et al. 2010, A&A, 524, 29). However, given these systems are generally classified as "unusual", we have separated them from the rest and they are not included in the plots. The data on these sources are available in the file [lrlx_odd_srcs.csv](https://github.com/bersavosh/XRB-LrLx_pub/blob/master/lrlx_odd_srcs.csv). 

### tMSPs:
Transitional millisecond pulsars are a relatively new group of sources on this plot. There are still only a hanful of confirmed tMSPs identified and thus their behavior (on the Lr-Lx plane) is not fully explored. A recent study by [Bogdanov et al. 2017](http://adsabs.harvard.edu/abs/2017arXiv170908574B) indicates that in the faint accretion state, PSR J1023+0038 shows a strong anti-correlation between radio and X-ray luminosity. Based on the anti-correlation, it is also suggested that the radio emission might not be (entirely) from a self-absorbed jet. Thus, it is possible that comparing their radio and X-ray emission to other systems on this plot might not be appropriate.

### Correlation lines:
WARNING: As shown in [Tetarenko et al. 2018](http://adsabs.harvard.edu/abs/2018arXiv180105778T), NS XRBs and AMXPs do not seem to follow the previously suggested correlation lines. Thus, these correlation lines are not shown in the plot. However these are still included as comments in the plotting script.
  - The dotted black line shows the best-fit relation for BHs [Gallo et al. 2006](http://adsabs.harvard.edu/abs/2006MNRAS.370.1351G)
  - The blue dashed and dashed-dotted lines show the two suggested correlations for NS systems [Migliari & Fender 2006](http://adsabs.harvard.edu/abs/2006MNRAS.366...79M)

## Acknowledgment:
If you use this package, we request that you cite the following record:

[Arash Bahramian et al. 2018; Radio/X-ray correlation database for X-ray binaries](http://doi.org/10.5281/zenodo.1252035)

Bibtex:
```
@misc{arash_bahramian_2018_1252036,
  author       = {Arash Bahramian and
                  James Miller-Jones and
                  Jay Strader and
                  Alexandra Tetarenko and
                  Richard Plotkin and
                  Anthony Rushton and
                  Vlad Tudor and
                  Sara Motta and
                  Laura Shishkovsky},
  title        = {{Radio/X-ray correlation database for X-ray 
                   binaries}},
  month        = may,
  year         = 2018,
  doi          = {10.5281/zenodo.1252036},
  url          = {https://doi.org/10.5281/zenodo.1252036}
}
```

This repository is maintained and updated by [Arash Bahramian](https://bersavosh.github.io/). Feel free to contact me if you have suggestions/comments/questions. 

Contributors: [Alex Tetarenko](https://sites.ualberta.ca/~tetarenk/), [James Miller-Jones](https://staffportal.curtin.edu.au/staff/profile/view/James.Miller-Jones), [Jay Strader](http://web.pa.msu.edu/people/strader/), [Richard Plotkin](https://staffportal.curtin.edu.au/staff/profile/view/Richard.Plotkin), [Anthony Rushton](http://www2.physics.ox.ac.uk/contacts/people/rushton), [Vlad Tudor](https://www.icrar.org/people/vtudor/), [Laura Shishkovsky](https://astro.natsci.msu.edu/people/laura-shishkovsky/), [Sara Motta](https://www.wadham.ox.ac.uk/people/fellows-and-academic-staff/m/sara-motta).

## Plots:
### The Lr-LX plot with sources marked/colored by class:
<img src="https://raw.githubusercontent.com/bersavosh/XRB-LrLx_pub/master/lrlx_plot_byclass.jpg" width="800">

### The Lr-LX plot with sources marked/colored by name:
<img src="https://raw.githubusercontent.com/bersavosh/XRB-LrLx_pub/master/lrlx_plot_byname.jpg" width="1000">
