PDS_VERSION_ID       = PDS3

LABEL_REVISION_NOTE       = "2013-08-08, PPI Node;"

RECORD_TYPE          = STREAM
INSTRUMENT_HOST_NAME = "MARS SCIENCE LABORATORY"
INSTRUMENT_NAME      = "RADIATION ASSESSMENT DETECTOR"
OBJECT               = TEXT
  PUBLICATION_DATE   = 2013-08-08
  NOTE               = "Description of volume MSLRAD_1002"
END_OBJECT           = TEXT
END


Volume MSLRAD_1002: MSL RAD Reduced Data

1. Introduction

   This volume contains RDR data (Reduced Data Record) from the Radiation
   Assessment Detector (RAD) instrument aboard the Mars Science Laboratory
   (MSL) rover, better known as Curiosity.  The data files contain radiation
   measurements taken during interplanetary cruise and the surface mission.
   The RDR data are NASA Level 1A data that mirror the raw instrument 
   data obtained from telemetry.

   The volume also contains calibration data and documentation useful for
   the interpretation of the data.
   
   For more information about the data and about this volume, refer to the
   documentation in the DOCUMENT and CATALOG directories of the volume.


2. Volume Format

   These RDR data products are being delivered electronically to PDS.  They
   are archived in a single volume which will continue to grow as the 
   mission progresses.


3. File Formats

Data File Format
   
   The RDR data files are calibrated data reconstructed from EDR data and 
   formatted according to the RAD RDR Software Interface Specification 
   (RDR SIS).  The file naming convention is explained in the RDR SIS,
   which is in the DOCUMENT directory of the volume. 

   The RDR files are in ASCII format.  The files are in generally
   human-readable form, but some lines are very long to preserve
   machine-readability as well.

   Each data file is described by a detached PDS label as described below.  The
   fields in the data files are described by PDS format files (*.FMT), which are
   referenced in the labels.  The format files are in the LABEL directory of 
   this volume.
   
Document File Format
   
   Most of the documentation for this volume resides in the DOCUMENT and
   CATALOG directories.  The CATALOG directory contains PDS catalog files
   (*.CAT) providing information about the spacecraft, instrument, data set,
   personnel associated with the experiment, and relevant literature
   references.  The catalog files are in ASCII format.  The DOCUMENT
   directory contains the Software Interface Specification (SIS) document
   describing the RDR data, and the Volume SIS describing the volume structure.
   Documentation files also exist in most of the top-level directories
   ASCII information files (*INFO.TXT) exist in many of the directories on
   this disk; these files describe the directory contents.

   ASCII text files ion this volume have records delimited by a carriage 
   return character followed by a line feed character.  This line ending
   makes the file easier to read on a variety of operating systems.
      
PDS Label Format
   
   All data and tabular files in this volume have associated PDS labels.
   A PDS label provides descriptive information about the content and
   format of the associated file. The PDS label is an object-oriented
   structure consisting of sets of "keyword = value" declarations. The object
   to which the label refer (e.g. IMAGE, TABLE, etc.) denotes the form:
   
       ^object = location
   
   in which the caret character (^, also called a pointer in this context)
   indicates where to find the object. In an attached label, the location is
   an integer representing the starting record number of the object (the first
   record in the file is record 1). In a detached label, the location denotes
   the name of the file containing the object, along with the starting record
   or byte number, if there is more than one object in the file.
   
   For example:
   
       ^HEADER = ("F01.IMG",1)
       ^IMAGE = ("F01.IMG",1025 <BYTES>)
   
   indicates that the IMAGE object begins at byte 1025 of the file F01.IMG, in
   the same directory as the detached label file. Below is a list of the
   possible formats for the ^object definition.
   
       ^object = n
       ^object = n<BYTES>
       ^object = "filename.ext"
       ^object = ("filename.ext",n)
       ^object = ("[dirlist]filename.ext",n)
       ^object = ("filename.ext",n<BYTES>)
       ^object = ("[dirlist]filename.ext",n<BYTES>)
   
       where:
   
       n is the starting record or byte number of the object, counting from
       the beginning of the file (record 1, byte 1);
   
       <BYTES> indicates that the number given is in units of bytes;
   
       filename is a maximum 36-alphanumeric upper-case character file name,
       ext is the 3 upper-case character file extension;
   
       dirlist is an upper-case, period-delimited path-list of parent
       directories, beginning at the directory level below the archive volume
       root directory, that specifies the object file directory (used only
       when the object is not in the same directory as the label file).
   
   Detached label files have variable length lines with an end-of-line
   designator consisting of a carriage return character followed by a line 
   feed character.  This makes the files easy to read on a variety of 
   different operating systems.
   
Catalog File Format
   
   Catalog files (suffix .CAT) exist in the root and CATALOG directories.  
   They are formatted in an object-oriented structure consisting of sets of
   "keyword = value" declarations.
   
   
4. Volume Contents
   
   The files in this volume are organized in one root-level directory with
   several subdirectories. The following outline shows the structure and
   content of these directories. In the table, directory names are enclosed
   in square brackets ([]), upper-case letters indicate actual directory or
   file names, and lower-case letters indicate the general form of a set
   of directory or file names.
   

Root directory
   |
   |
   |- AAREADME.TXT     Describes volume contents, organization and disk
   |                   use (ASCII text).  The file you are now reading.
   |
   |- ERRATA.TXT       A cumulative listing of errata and other comments
   |                   pertaining to the files in the volume.
   |
   |- VOLDESC.CAT      Description of the contents of this volume.
   |
   |- [INDEX]              Contains index tables for the data products on
   |    |                  this volume.
   |    |
   |    |- INDXINFO.TXT    Description of the contents of this directory.
   |    |
   |    |- INDEX.LBL       Detached PDS label describing contents of
   |    |                  INDEX.TAB.
   |    |
   |    |- INDEX.TAB       Index table file for the data products in
   |                       the current volume.
   |
   |- [DOCUMENT]           Contains various documents that facilitate the
   |    |                  understanding of the datasets included on this
   |    |                  volume.
   |    |
   |    |- DOCINFO.TXT     Description of the contents of this directory.
   |    |
   |    |
   |    |- RAD_RDR_SIS.HTM  The SIS for the RAD RDR data set, in human-readable
   |    |                   HTML format.
   |    |
   |    |- RAD_RDR_SIS.PDF  The SIS for the RAD RDR data set, in PDF format.
   |    |
   |    |- RAD_RDR_SIS.LBL  PDS detached label for the data set SIS.
   |    |
   |    |- VOLSIS.HTM      The volume SIS for this volume, in human-readable
   |    |                  HTML format.
   |    |
   |    |- VOLSIS.PDF      The volume SIS for this volume, in PDF format.
   |    |
   |    |- VOLSIS.LBL      PDS detached label for the volume SIS.
   |    |
   |    |
   |- [CATALOG]            This directory contains the catalog files.
   |    |
   |    |- CATINFO.TXT     Description of the contents of this directory.
   |    |
   |    |- RAD_INST.CAT    Information about the RAD instrument.
   |    |
   |    |- MSL_INSTHOST.CAT Information about the MSL spacecraft.
   |    |
   |    |- MSL_MISSION.CAT  Information about the MSL mission.
   |    |
   |    |- RAD_PERSON.CAT  Contact information for RAD team members and
   |    |                  other relevant personnel.
   |    |
   |    |- MSL_REF.CAT     Literature references relevant to MSL, including
   |    |                  references mentioned in other catalog files.
   |    | 
   |    |- RAD_REF.CAT     Literature references relevant to RAD, including
   |    |                  references mentioned in other catalog files.
   |    |
   |    |- RAD_RDR_DS.CAT  Description of the RAD RDR data files.
   |    |
   | 
   |
   |- [DATA]               Contains the RDR data files.
   |
   |
   |- [CALIB]              This directory contains calibration information that
   |    |                  is relevant to the understanding and use of the data.
   |    |
   |    |- CALINFO.TXT     Description of the contents of this directory.
   |    |
   |
   |
   |- [LABEL]                  This directory contains format files (*.FMT)  
   |    |                      describing the contents of the RDR data files.
   |    |
   |    |- LABLINFO.TXT        Description of the contents of this directory.
   |    |
   |    |                      (Note: Each of the following format files begins
   |    |                      with a comment that points to the data that the
   |    |                      format file describes.)
   |    |
   |    |- D_LETCNT.FMT
   |    |
   |    |- D_LET_EVC.FMT
   |    |
   |    |- D_LET_EVW.FMT
   |    |
   |    |- HIST_PP.FMT
   |    |
   |    |- HIST_PPXC.FMT
   |    |
   |    |- HIST_PPXW.FMT
   |    |
   |    |- HIST_SP.FMT
   |    |
   |    |- HIST_SPXC.FMT
   |    |
   |    |- HIST_SPXW.FMT
   |    |
   |    |- H_N_CNT.FMT
   |    |
   |    |- H_NDE.FMT
   |    |
   |    |- H_NDE_XC.FMT
   |    |
   |    |- H_NDE_XW.FMT
   |    |
   |    |- H_N_EVC.FMT
   |    |
   |    |- H_N_EVW.FMT
   |    |
   |    |- L1_CNTR.FMT
   |    |
   |    |- L2_CNTR.FMT
   |    |
   |    |- PHA_TAB.FMT
   |    |
   |


5. Errata and Disclaimer
   
   A list of anomalies and errors is maintained in the file ERRATA.TXT at the
   root directory of this volume.
   
   Known data uncertainties and limitations are described in the data set
   catalog file located in the CATALOG subdirectory.
   
   Although considerable care has gone into making this volume, errors are
   both possible and likely. Users of the data are advised to exercise the
   same caution as they would when dealing with any other unknown data set.
   
   Reports of errors or difficulties would be appreciated. Please contact one
   of the individuals listed below.

   Use of these data is at the user's own risk.  The PDS, the PPI Node, and 
   their employees and contractors assume no legal responsibility for the 
   contents of this volume.
   
   
7. Contact Information
   
   For questions concerning this volume set, data products, and documentation,
   contact
   
       Dr. Scot Rafkin
       Asst. Director, Dept. of Space Studies
       Southwest Research Institute
       Boulder, CO 80302 USA
       Phone: +1 720-240-0116
       E-mail: rafkin@boulder.swri.edu
   
   For questions concerning PDS standards and usage, contact
   
       Dr. Steven P. Joy
       University of California
       6855 Slichter Hall
       Los Angeles, CA 90095-1567 USA
       Phone:  +1 310-825-3506
       E-mail:  sjoy@igpp.ucla.edu

