
***************************************************
    Caveats for End Users of IUVS Data Products   
***************************************************

Last updated 2017-11-14
Appropriate for v07 data release


***********  Cosmic Ray Detector Events  **********

The image-intensified 2-D active pixel sensors used in IUVS are sensitive to cosmic radiation. Such events result in 'splashes' and 'streaks' with random orientations on the detector images. The impact is often negligible when observing bright targets (e.g. the Martian disk) but can become a major source of noise for sensitive observations (e.g. coronal scans). A unified method for cleaning the data of these events is still under development. The user should be aware that most transient unexpected features they find in the data are attributable to these cosmic ray events.


************  Calibration Uncertainty  ************

The IUVS instrument currently maintains systematic absolute calibration uncertainties of 25% and 30% for the FUV and MUV channels respectively. This makes retrievals using many emission features unreliable, with optically thick emissions being particularly impacted due to non-linear responses. Only retrievals which have been found robust to the current calibration uncertainty are included in the current data release.

A calibration correction factor has been applied for disk observations that use the electronic shutter. The correction factor has inaccuracies in the 315-325 nm region on the order of 17%.


************  Slit Tilt and Wavelength Shift in L1C MLR  ***********

The image of the slit on the IUVS detectors has a significant tilt relative to the detector pixel columns, especially in the FUV channel. This produces artifacts during multiple linear regression (MLR) fitting of emission brightnesses in L1C apoapse products, causing significant artificial structure in FUV the disk maps. The variations in brightness associated with these artifacts are currently captured by adding a fixed factor of 10% to the reported random uncertainty.

The position of the slit image on the detector can also shift due to thermal gradients across the instrument case, with movements of ~ 1 detector pixel over the course of an orbit being common. This results in small but occasionally significant shifting of the wavelength scale in both channels. This is currently accounted for only in the L1C periapse data products with a per-orbit wavelength shift correction.


******  MUV Contamination in FUV Data  *******

When IUVS makes observations of the Martian surface or lower atmosphere, the FUV channel experiences significant contamination by 1st order MUV sunlight reflected from the planet. This most significantly impacts stellar occultations on the dayside and disk mapping observations. For disk observations, the multiple-linear-regression (MLR) fitting of FUV features in apoapse L1C products incorporates a term to remove this artifact, with generally good results. However, variations in disk MUV spectrum due to aerosol loading and ozone absorption from observation to observation are currently not accounted for. Data products at L1A and L1B are uncorrected, and the user is urged to exercise appropriate caution when working with them.


************  Side Segment Timing Accuracy   ***********

During observations of limb airglow on the MAVEN orbit side segments, reconstructed tangent altitudes are highly sensitive to the reconstructed timing relative to periapsis. There is evidence that the current reconstructions in some cases contain inaccuracies that translate to altitude translations of up to 1 atmospheric scale height. The absolute altitude of the airglow features should therefore be treated with caution, though relative changes (e.g. scale heights) are robust. The limb scans obtained during the periapse segment of the orbit are much less sensitive to the timing reconstruction and the reported altitudes are expected to be accurate.


***********  Observational Constraints  ***********

The IUVS instrument is occasionally constrained from running certain commands due to observational constraints, e.g. the Sun being too close to its field of view. Subtle timing discrepancies in predicting when these constrains occur can result in unexpected commanding behavior for scheduled observations. For example, the echelle grating may not be commanded out of the optical path, the MCP voltage may remain off or at a low default value, or the scan mirror may remain in a stowed position. Unfortunately, this behavior is not reflected in the science telemetry stored in the current FITS files, as this is derived from commanded values, not those actually executed by the hardware or measured by sensors. An automated process is being developed to identify and correct this issue.

Below is a list of orbits with observations known to be affected by at least one of the above commanding issues. The list is grouped by orbit segment, and each line is indicates a range of orbit numbers with commanding issues. For an isolated problematic orbit the start and end orbits will be the same. This list is not necessarily complete.


Periapse:

     346     348
     356     360
     368     368
     449     449
     458     526
     566     566
     624     624
     690     690
     808     808
     828     828
     945     950
     955     970
    1216    1232
    1244    1244
    1295    1295
    1554    1556
    1581    1582
    1656    1656
    1670    1670
    1855    1858
    1890    1926
    1959    1960
    1993    1994
    2029    2030
    2194    2194
    2230    2230
    2287    2287
    2503    2503
    2520    2520
    2540    2554
    2558    2574
    2594    2594
    2892    2892
    3201    3201
    3205    3205
    3210    3210
    3320    3323
    3518    3518
    3600    3600
    3611    3611
    3634    3666
    3669    3681
    3687    3687
    3691    3691
    3709    3709
    3711    3715
    3717    3717
    3719    3719
    3721    3725
    3731    3732
    3962    3962
    3964    3964
    3980    3980
    3998    3998
    4683    4683
    4840    4840

Outbound:

     346     346
     356     358
     464     464
     512     516
     536     572
     604     620
     672     672
     700     700
     730     748
     768     780
     816     886
     948     968
    1218    1232
    1274    1274
    1710    1710
    1818    1818
    1890    1926
    2024    2028
    2194    2194
    2230    2230
    2542    2542
    2558    2558
    2612    2612
    2728    2736
    2940    2940
    3557    3557
    3559    3563
    3565    3569
    4840    4840

Apoapse:

     337     337
     345     347
     355     359
     367     367
     419     419
     429     429
     464     465
     509     509
     512     517
     534     535
     569     569
     623     623
     688     689
     806     807
     826     827
     945     950
     955     969
    1214    1215
    1218    1233
    1244    1245
    1273    1273
    1295    1295
    1325    1327
    1346    1348
    1350    1350
    1362    1365
    1384    1385
    1401    1402
    1422    1423
    1581    1581
    1710    1711
    1854    1857
    1890    1925
    1959    1959
    1992    1993
    2028    2029
    2405    2409
    2692    2699
    2891    2891
    2893    2893
    3009    3009
    3043    3043
    3074    3074
    3458    3458
    3496    3517
    3521    3521
    3610    3610
    3632    3632
    3687    3688
    5445    5446
    5465    5465
    5481    5482
    5500    5501
    5519    5519

Inbound:

     248     248
     346     346
     356     361
     366     366
     434     434
     464     464
     508     512
     568     568
     948     968
    1214    1232
    1468    1468
    1580    1580
    1710    1710
    1752    1752
    1854    1854
    1890    1924
    2028    2028
    2764    2764
    2780    2780
    3458    3458


**************  Special Observations  *************

During the nominal science mission, IUVS has occasionally carried out special calibration activities and opportunistic scientific observations. For the most part, these currently lack any special identification in the file names. Below are a list of these observations with segment name and orbit identified. Not all experiments were successful.

Stray Light Experiments:
	outbound-orbit00676
	apoapse-orbit00676
	inbound-orbit00676
	apoapse-orbit01293
	apoapse-orbit01795

Stellar Occultation of Opportunity:
	outbound-orbit00516
	outbound-orbit00700

Shutter Experiments:
	inbound-orbit00759
	apoapse-orbit00823
	inbound-orbit00898
	inbound-orbit01585

Star Raster:
	apoapse-orbit01236
	apoapse-orbit01597

IPH Echelle Experiment:
	apoapse-orbit01274
	apoapse-orbit01992
	apoapse-orbit02692 to apoapse-orbit02698
	apoapse-orbit05042 to apoapse-orbit05055

Solar Occultation Experiment:
	periapse-orbit02503
	periapse-orbit02540 to periapse-orbit02574
	inbound-orbit05060 to inbound-orbit05094
	inbound-orbit05114 to inbound-orbit05304

Stray Light/Detector Background Experiment:
	inbound-orbit04252 to inbound-orbit04286

Airglow Slit Stellar Calibration:
	inspace-orbit04876
	inspace-orbit04886
	inspace-orbit04896
	inspace-orbit04906
	inspace-orbit04912 to inspace-orbit04946
	star-orbit05170 to star-orbit05290
	star-orbit05306 to star-orbit05396


********* Occultation Campaigns *********

Not all stellar occultation events are suitable for retrievals. This is due to various issues, such as unanticipated observational constraints or contamination from stray sunlight. The table below enumerates the useful events from each occultation campaign.

 Campaign (orbit)	FUV & MUV	only FUV	only MUV #1 (orbit 009xx)	3		6		- #2 (orbit 012xx)	-		-		25 #3 (orbit 016xx)	4		14		- #4 (orbit 019xx)	-		-		- #5 (orbit 021xx)	12		25		- #6 (orbit 025xx)	-		5		- #7 (orbit 028xx)	15		-		- #8 (orbit 032xx)	-		10		- #9 (orbit 034xx)	5		-		-#10 (orbit 038xx)	-		5		-#11 (orbit 041xx)	40		-		-#12 (orbit 044xx)	10		-		-
#13 (orbit 048xx)	30		-		-
#14 (orbit N/A)		N/A		N/A		N/A
#15 (orbit 052xx)	27		-		-
#16 (orbit 053xx)	36		-		-


*********  L1C and L2 Product Limitations  ********

Level 2 contains derived data products with physical values retrieved from radiances in L1C. Many retrievals are limited to particular illumination conditions or altitude coverage.

L1C limb scan brightnesses are currently limited to dayside observations (SZA < 80), and do not attempt to fit nitric oxide night glow.

L2 limb scan retrievals utilize neutral atmospheric structure from the Mars Climate Database for initialization purposes. It has been found that the retrieved temperature of the limb scans has high sensitivity to the details of this initialization. More robust methods of retrieving the temperature are in development.

L1C and L2 coronal observations are not processed during seasons with small phase angles due to solar contamination and off-nominal pointing. Orbits with “inward” looking coronal scans on both the outbound and inbound side segments are not handled by the current pipeline.

L1C disk scans currently have FUV brightnesses set to NaN when the spectral binning is 36, 43, 72, or 96, as these have coarse binning which is not properly handled by the reduction pipeline. Most data uses 1024, 512, 256, 200, and 184 bins.

L2 limb scan retrievals are limited to solar zenith angles < 60 deg. When the spacecraft uses a Fly-Z orientation at periapse (Science Scenarios 2b and 4b) the APP does not perform the “nod” necessary for IUVS to capture complete profiles of the airglow layer, and retrievals are not attempted. This occurred during the following periods:
	2015-Aug-25 to 2015-Aug-31
	2015-Sep-15 to 2015-Oct-12

L2 nadir viewing disk retrievals are limited to solar zenith angles < 80 degrees. The current look-up table used for the retrieval is also limited in the range of solar EUV fluxes it has indexed. As result, some orbits in the Nov 15 2015 - Feb 15 2016 time range when Mars was near apoapse are not current processed to L2.

L2 nadir viewing disk retrievals are limited to solar zenith angles < 80 degrees. 

For v07 L1C disk products pixels near the limb which do not actually intersect the disk are geographically mapped using the geometry beneath the tangent point of the line-of-sight. This can introduce artifacts in the latitude/longitude maps at high emission angle. Also note that all geometry for disk observations is reported for a surface intercept, which introduces artifacts at high emission angles for airglow occurring at altitude.

L1C and L2 disk scans are not produced for high spatial resolution observations (beginning in 2016). Validation of pipeline processing for these products is ongoing.


****************  L2 Periapse FUV  ****************
The following caveats apply to L2 Periapse FUV retrievals:

2202 	very slight striping in CO 4PG intensities
2206 	striping in all intensities
2213 	striping in all intensities
2224 	very slight striping most apparent in vv=0/vv>0 intensity ratio
2240 	slight striping in all intensities
2360 	striping in all intensities
2399 	slight striping in all intensities
2400 	striping apparent in all intensities
2404 	striping apparent in all intensities
2418 	striping in all intensities
2487 	striping most apparent in CO/CO2 intensity ratio
2551 	very slight striping most apparent in error of CO/CO2 density ratio or 1356/CO4PG vv>0 intensity ratio 
2552 	very slight striping most apparent in error of CO/CO2 density ratio or 1356/CO4PG vv>0 intensity ratio 
2553 	very slight striping most apparent in error of CO/CO2 density ratio or 1356/CO4PG vv>0 intensity ratio 
2559 	very slight striping most apparent in error of CO/CO2 density ratio or 1356/CO4PG vv>0 intensity ratio 
2560 	slight striping most apparent in error of CO/CO2 density ratio or 1356/CO4PG vv>0 intensity ratio 

******************  Other Issues  *****************

A geometry bug causes the solar zenith angle (incidence angle) to be 0 deg for the first integration of echelle scans.
