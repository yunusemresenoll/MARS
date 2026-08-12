PDS_VERSION_ID               = PDS3
RECORD_TYPE                  = STREAM

OBJECT                       = TEXT
  INTERCHANGE_FORMAT         = ASCII
  PUBLICATION_DATE           = 2022-12-05
  NOTE                       = "Introduction to REMS RDR Data"
END_OBJECT                   = TEXT
END

                        Mars Science Laboratory
         Rover Environmental Monitoring Station RDR Data Archive


=======================================================================
INTRODUCTION
=======================================================================

This volume contains processed data from the REMS instrument
aboard the MSL mission. Included are data from all the
sensors that compose the instrument (wind, air temperature, ground
temperature, ultraviolet, humidity and pressure). Also ancillary data
from the rover are included in the volume (this information is 
provided by NAIF). 

=======================================================================
VOLUME INFORMATION
=======================================================================

top-level directory
|
|- AAREADME.TXT          This file.
|
|- ERRATA.TXT            Listing of known errors on this volume.
|
|- VOLDESC.CAT           A description of the contents of this volume.
|
| - [CALIB]    A directory containing files with calibration 
|     |        parameters.
|     |
|     | - CALINFO.TXT    Description of files in this directory.
|     |
|     | - *.TXT          Calibration parameters files.
|     |
|     | - *.LBL          Label files describing the calibration 
|                        parameters files.
|
|- [CATALOG]             Directory with information about the data set.
|     |
|     |- CATINFO.TXT          Description of files in this directory.
|     |
|     |- REMS_TELRDR_DS.CAT   Description of TEL RDR data set.
|     |
|     |- REMS_ENVRDR_DS.CAT   Description of ENV RDR data set.
|     |
|     |- REMS_MODRDR_DS.CAT   Description of MOD RDR data set.
|     |
|     |- REMS_ADR_DS.CAT      Description of ADR data set.
|     |
|     |- REMS_UVRDR_DS.CAT    Description of UV RDR data set.
|     |
|     |- REMS_INST.CAT        Description of the REMS instrument.
|     |
|     |- MSL_INSTHOST.CAT     Description of the MSL Curiosity rover.
|     |
|     |- MSL_MISSION.CAT      Description of the MSL mission
|     |
|     |- REMS_PERSON.CAT      Listing of people involved in the production 
|     |                       of this data set.
|     |
|     |- MSL_REF.CAT          List of references.
|     |- REMS_REF.CAT
|     
|     
|- [DATA]                REMS RDR data products, divided by release.
|     |
|     |- [SOL_XXXXX_XXXXX]     REMS RDR data products, divided by sol.
|     |         |
|     |         |-SOLXXXXX
|     |         |
|
|     
|- [DATA_UV_CORRECTED]    REMS corrected UV RDR data products
|
|
|- [DOCUMENT]                  Directory containing the documentation.
|     |
|     |- DOCINFO.TXT           Description of files in this directory.
|     |
|     |- REMS_RDR_SIS.PDF      Description of the data product content and
|     |                        formats as a PDF file.
|     |
|     |- REMS_RDR_SIS.TXT      Description of the data product content and
|     |                        formats as a text file.
|     |
|     |- REMS_RDR_SIS.LBL      Label describing both the REMS_RDR_SIS.PDF and
|     |                        REMS_RDR_SIS.TXT files.
|     |
|     |- MSL_RDR_VOLSIS.PDF    Description of the archive content and formats
|     |                        as a PDF file.
|     |
|     |- MSL_RDR_VOLSIS.TXT    Description of the archive content and formats
|     |                        as a text file.
|     |
|     |- MSL_RDR_VOLSIS.LBL    Label describing both MSL_RDR_VOLSIS.PDF and
|     |                        the MSL_RDR_VOLSIS.TXT files.
|     |
|     |- DATA_EVENTS.TXT       A list of data related events occurred to REMS
|     |                        during the mission. 
|     |
|     |- WIND_PROCESSING.LBL   Label describing both the WIND_PROCESSING.PDF
|     |                        and WIND_PROCESSING.TXT files.
|     |                        
|     |- WIND_PROCESSING.PDF   Document that explains how wind calculations are
|     |                        done, in PDF format.
|     |                        
|     |- WIND_PROCESSING.TXT   Document that explains how wind calculations are
|     |                        done, in TXT format.
|     |                        
|
|- [INDEX]     PDS index files
|     |
|     |- INDINFO.TXT     Description of files in this directory.
|     |
|     |- INDEX.LBL       A label describing the file INDEX.TAB.
|     |
|     |- INDEX.TAB       Index to the data in this volume.
|
|     
| - [LABEL]    A directory containing files with repeated label information.
|     |
|     | - LABINFO.TXT    Description of files in this directory.
|     |
|     | - *.FMT          Format files describing tables structures.
|

=======================================================================
QUICK START - BEGINNING TO USE THE VOLUME
=======================================================================

For a quick start, it would be helpful to first familiarize oneself
with the contents of the two SISes (Software Interface Specification)
documents, in the DOCUMENT directory. The data SIS (REMS_RDR_SIS.PDF)
describes the data in the archive. The volume SIS
(REMS_RDR_VOLSIS.PDF) describes the layout of REMS archive volumes,
including this one.

All the science data on this volume is stored in ASCII files, with
values separated by commas so they can be easily loaded into any
software that can read CSV files.

=======================================================================
DISK FORMAT
=======================================================================

This disk is formatted according to the ISO-9660_LEVEL2 standard, with
the exception that file names may be up to 40 characters long
(including the period and the three character extension), instead of
the 31 character limit established by the standard.

=======================================================================
FILE FORMATS
=======================================================================

The following file formats can be found in this volume:

CATALOG FILE FORMAT

.CAT files. Found in the ROOT and CATALOG directories. Object oriented
structure: `keyword = value'.  All lines terminated with carriage
return and line feed characters.

DOCUMENT FILE FORMAT

 .TXT and .PDF suffixes. Found in all top-level
directories. TXT-suffix files are ASCII files with embedded PDS
labels. Lines are terminated with carriage return and line feed
characters. PDF files are binary files written in the Portable
Document Format, a proprietary format of Adobe Software Inc.

PDS LABEL FORMAT

PDS labels are object-oriented structures consisting of `keyword =
value' statements. PDS labels are detached from the associated file 
( .LBL extension). Lines are terminated with the carriage return 
and linefeed characters.

TABULAR FILE FORMAT

File suffixes are  .TAB, and all files are provided in ASCII.

ASCII files ( .TAB) are found in the INDEX and DATA directories.
These files are formatted for direct reading into many database
management systems on various operating systems. Fields are enclosed
by double quotes, and separated by commas. Character fields are left
justified and padded to a constant length with spaces if
required. Numeric fields are right justified. The `start bytes' and
`bytes' values listed in the labels count data only, not quotes,
commas or external spaces. The records are fixed length and terminated
by the carriage return and line-feed characters.

=======================================================================
INTERFERENCES AND KNOWN ISSUES
=======================================================================

During the first 72 sols, for each 5 minute block, the following
measurement strategy was used: Wind Sensor is switched off for 60
seconds, then it is switched on for 235 seconds, and then it is
switched off again for the final 5 seconds. The rest of the
sensors are switched on all the time. This strategy was based on
results obtained during pre-flight testing. However, after
evaluating flight data, it was determined that this strategy was
not necessary, so from sol 73 onwards all sensors are switched on
for each 5 minute block.

From sol 155 onwards the degradation of the Ultraviolet Sensor is
beyond its operational functional requirements. Dust deposited over
the sensor has caused its attenuation to be above its accuracy limit
of 10%. However, a new dataset consisting of REMS UV fluxes (W/m2) 
acquired for solar zenith angles < 55° during the first 3423 sols has 
been corrected for the effects of dust deposition and inaccuracies in 
the original angular response calibration functions. This dataset is
available as MSL-M-REMS-5-UVRDR-V1.0.

From sol 793 onwards, a new measurement strategy for Humidity Sensor
was introduced. It is called HS HRIM (Humidity Sensor High Resolution
Interval Mode) and is only used on selected one-hour long
observations. This new strategy intends to minimize heating of the
Humidity Sensor, and consists of alternately switching on and off the
sensor at periodic intervals. At the same time, Boom 2 is switched
off, which means that there are no Wind Sensor and Air Temperature
Sensor measurements.

Wind Sensor boards 2 and 3 in boom 1 are not operative since they were
damaged during landing. In addition, the following Wind Sensor boards
in boom 2 are not operative starting on given sols:

- Board 1, dice 1: since sol 854
- Board 2: since sol 1485
- Board 3: since sol 1491
- Board 1: since sol 1504


=======================================================================
ERRATA AND DISCLAIMER
=======================================================================

A cumulative list of anomalies and errors is maintained in the file 
ERRATA.TXT at the root directory of this volume.

Although considerable care has gone into making this volume, errors are 
both possible and likely. Users of the data are advised to exercise
the same caution as they would when dealing with any other unknown
data set.

Reports of errors or difficulties would be appreciated. Please contact
one of the persons listed herein.

=======================================================================
WHOM TO CONTACT FOR INFORMATION
=======================================================================

For questions concerning this volume set and its data products:

Address:     Javier Gomez-Elvira
             Centro de Astrobiologia. INTA
             CTRA Ajalvir, Km 4
             28850 Torrejon de Ardoz
             Spain
Phone:       +34 91 520 6436
Email:       gomezej@cab.inta-csic.es

For questions concerning the PDS:

Address:     Lyle Huber
             New Mexico State University
             Las Cruces
             NM 88003

Phone:       (575) 646-1862
Email:       lhuber@nmsu.edu

