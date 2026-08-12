PDS_VERSION_ID        = PDS3                                                  
RECORD_TYPE           = STREAM                                                
                                                                              
OBJECT                = TEXT                                                  
  INTERCHANGE_FORMAT  = ASCII                                                 
  PUBLICATION_DATE    = 2008-05-20                                            
  NOTE                = "N/A"                                                 
END_OBJECT            = TEXT                                                  
END                                                                           
                                                                              
MRO MARS CLIMATE SOUNDER DDR, VOLUME 2104:  APRIL, 2015                       
                                                                              
                                                                              
INTRODUCTION                                                                  
============                                                                  
                                                                              
This volume contains one month of derived sensor-level data (NASA level 2, 
CODMAC level 5) from the Mars Climate Sounder (MCS), flying aboard the Mars   
Reconnaissance Orbiter (MRO) spacecraft. These measurements include instrument
engineering and housekeeping data, as well as detector science measurements of
scene views and of calibration targets.                                       
                                                                              
This volume conforms to the Planetary Data System (PDS) Standards, Version    
3.6, Jet Propulsion Laboratory (JPL) document JPL D-7669.                     
                                                                              
Additional information regarding this data set, including a description of the
instrument, a description of the observational strategy, and a description of 
the data processing, can be found in MCCLEESE_ET_AL_2007.PDF in the DOCUMENT  
directory of this volume.                                                     
                                                                              
VOLUME FORMAT                                                                   
=============                                                                 
                                                                              
This volume is formatted according to the ISO 9660-Level 2 Interchange Standard,
as described in the ISO 9660 Standard Document:  RF# ISO 9660-1988, 16 April  
1988.  This volume should be accessible from most computer systems, including,  
but not limited to, Sun/Solaris, IBM/Windows, IBM/Linux, and Macintosh.       
                                                                              
FILE FORMATS                                                                  
============                                                                  
                                                                              
There are several different types of files in this archive volume, with several
different file formats.  All files are ASCII files with records ending with   
the carriage return (ASCII 13) and linefeed (ASCII 10) characters.            
Differences between the file formats are described below.                     
                                                                              
All .TXT files are PDS text objects with attached labels, formatted as ASCII  
files.                                                                        
                                                                              
The detached label files ("*.LBL") and the MCS_DDR.FMT files are ASCII files   
with stream-type (variable length) records.                                   
                                                                              
The INDEX.TAB and CUMINDEX.TAB files are ASCII tables made of 174-byte        
records.  The detailed format specification for these files can be found in   
the files INDEX.LBL and CUMINDEX.LBL.  INDXINFO.TXT provides additional       
information.                                                                  
                                                                              
Data product files YYYYMMDDHH_DDR.TAB contain a variable-length header,       
followed by a variable number of 17954-byte records.  The detailed format      
specification for these files is in the files MCS_DDR1.FMT & MCS_DDR2.FMT.                     
                                                                              
.PDF files in the DOCUMENTS directory are Adobe Acrobat Portable Document     
Files, and can be read with free Adobe Acrobat Reader software.               
                                                                              
.HTM files in the DOCUMENTS directory are hypertext markup language files and 
can be read with a web browser (e.g., Netscape or Microsoft Explorer).        
                                                                              
.ASC files in the DOCUMENTS directory are plain ASCII text and can be read    
with any text editor.                                                         
                                                                              
All data files in the archive have detached PDS labels. The PDS label provides
descriptive information about the associated file. The PDS label is an        
object-oriented structure consisting of sets of 'keyword=value' declarations. 
The object to which the label refers (e.g. IMAGE, TABLE, etc.) is denoted by a
statement of the form:                                                        
                                                                              
^object = location                                                            
                                                                              
in which the carat caret character (^, also called a pointer in this context) 
indicates where to find the object. For all MCS detached labels, the location 
contains the name of the file containing the object. For most labels the      
location consists only of the name of the file being referenced, but for the  
label files corresponding to data product files, it also includes a byte      
offset indicating how far into the file to read before the table itself       
begins. (Each data product file has a variable-length header.) along with the 
starting record or byte number, if there is more than one object in the file. 
For example:                                                                  
                                                                              
^PDF_DOCUMENT = ("DP_SIS.PDF")                                                
                                                                              
^TABLE = ("2007061804_DDR.TAB",2698 <BYTES>)                                  
                                                                              
The first indicates that the PDF document is the file "DP_SIS.PDF" The second 
indicates that a data product table can be found in the file                  
"2007061804_DDR.TAB", beginning at the 2698'th byte of the file (counting from
one).                                                                         
                                                                              
VOLUME CONTENTS                                                               
===============                                                               
                                                                              
                                                                              
The diagram below shows the organization of this volume, starting from        
the root directory.                                                           
            root                                                              
            |- AAREADME.TXT          The file you are reading.                
            |                                                                 
            |- ERRATA.TXT            A listing of known errors/problems on    
            |                        this volume. (Not present if empty.)     
            |                                                                 
            |- VOLDESC.CAT           A description of the contents of this    
            |                        volume in a format readable by           
            |                        both humans and computers.               
            |                                                                 
            |- [CALIB]               A directory containing calibration       
            |     |                  information about this data set.         
            |     |                                                           
            |     |- CALINFO.TXT     Descriptions of files in the CALIB       
            |     |                  directory.                               
            |     |                                                           
            |     |- MCS_SPECTRAL_RESPONSE.ASC    Spectral response of the    
            |     |                               instrument detectors.       
            |     |                                                           
            |     |- MCS_SPECTRAL_RESPONSE.LBL    PDS label for ASCII file.   
            |     |                                                           
            |                                                                 
            |- [CATALOG]             A directory containing descriptive       
            |     |                  information about this data set.         
            |     |                                                           
            |     |- CATINFO.TXT     Descriptions of files in the CATALOG     
            |     |                  directory.                               
            |     |                                                           
            |     |- DATASET.CAT     A description of the RDR                 
            |     |                  data files and the data processing.      
            |     |                                                           
            |     |- INSTHOST.CAT    A description of the MRO spacecraft.     
            |     |                                                           
            |     |- INST.CAT        A description of MCS & its operation.    
            |     |                                                           
            |     |- MISSION.CAT     A description of the MRO mission.        
            |     |                                                           
            |     |- PERSON.CAT      A listing of the people involved in the  
            |     |                  production of this data set and          
            |     |                  this volume.                             
            |     |                                                           
            |     |- REF.CAT         A list of pertinent references.          
            |                                                                 
            |- [DOCUMENT]            A directory containing related documents.
            |     |                                                           
            |     |- DOCINFO.TXT     Description of files in the DOCUMENT     
            |     |                  directory.                               
            |     |                                                           
            |     |- DP_ARCHSIS.ASC  The software interface specification     
            |     |                  document for this archive volume, as a   
            |     |                  plain ASCII file.                        
            |     |                                                           
            |     |- DP_ARCHSIS.PDF  The software interface specification     
            |     |                  document for this archive volume, as an  
            |     |                  Adobe PDF file.                          
            |     |                                                           
            |     |- DP_ARCHSIS.LBL  The PDS detached label file for          
            |     |                  DP_ARCHSIS files.                        
            |     |                                                           
            |     |- DP_SIS.ASC      The software interface specification for 
            |     |                  the MCS DDR data products, as a plain    
            |     |                  ASCII file.                              
            |     |                                                           
            |     |- DP_SIS.PDF      The software interface specification for 
            |     |                  the MCS DDR data products, as an Acrobat 
            |     |                  PDF file.                                
            |     |                                                           
            |     |- DP_SIS.LBL      The PDS detached label file for          
            |     |                  DP_SIS files.                           
            |     |                                                           
            |     |- MCCLEESE_ET_AL_2007.PDF                                  
            |     |                  A survey paper describing the MCS        
            |     |                  instrument and operations.               
            |     |                                                           
            |     |- MCCLEESE_ET_AL_2007.LBL                                  
            |     |                  The detached PDS label for               
            |     |                  MCCLEESE_ET_AL_2007.PDF.                 
            |     |                                                           
            |     |- MCS_ACTIVITY_LOG.PDF                                     
            |     |                  A log of significant instrument          
            |     |                  operation time periods.                  
            |     |                                                           
            |     |- MCS_ACTIVITY_LOG.LBL                                     
            |                        The detached PDS label for               
            |                        MCS_ACTIVITY_LOG.PDF.                    
            |                                                                 
            |- [INDEX]               A directory containing indices of data   
            |     |                  products in this data product set.       
            |     |                                                           
            |     |- INDXINFO.TXT    A description of files in the INDEX      
            |     |                  directory.                               
            |     |                                                           
            |     |- INDEX.TAB       An index of data files on this volume.   
            |     |                                                           
            |     |- INDEX.LBL       The detached PDS label for INDEX.TAB.    
            |     |                                                           
            |     |- CUMINDEX.TAB    An index of all the data files on this   
            |     |                  archive volume set, including those on   
            |     |                  this volume.                             
            |     |                                                           
            |     |- CUMINDEX.LBL    The detached PDS label for CUMINDEX.TAB. 
            |                                                                 
            |- [DATA]                A directory containing the data files    
            |     |                  and PDS labels describing the contents   
            |     |                  of those files.                          
            |     |                                                           
            |     - [2006]           The year of this archive volume.         
            |         |                                                       
            |         - [06]         The month of this archive volume.        
            |            |                                                    
            |            - [DD]      A series of subdirectories organized by  
            |               |        day of month.                            
            |               |                                                 
            |               - YYYYMMDDHH_RDR.TAB                              
            |               |        A four hour MCS RDR data product file.   
            |               |                                                 
            |               - YYYYMMDDHH_RDR.LBL                              
            |                        The corresponding detached label file.   
            |                                                                 
            |- [LABEL]               A directory containing the format        
                  |                  structure files.                         
                  |                                                           
                  |- LABINFO.TXT     Description of files in the LABEL        
                  |                  directory.                               
                  |                                                           
                  |- MCS_DDR1.FMT     A format file describing the columns     
                  |                   in record 1 of MCS DDR data product tables.      
                  |                                                           
                  |- MCS_DDR2.FMT     A format file describing the columns     
                                      in record 2 of MCS DDR data product tables.      
                                                                             
======                                                                        
ERRATA                                                                        
======                                                                        
                                                                              
==========                                                                    
DISCLAIMER                                                                    
==========                                                                    
                                                                              
Although care has gone into making this volume set, errors are possible.      
Reports of errors or difficulties would be appreciated. Please report any     
errors you detect to:                                                         
                                                                              
James R. Murphy                                                               
New Mexico State University                                                   
Department of Astronomy                                                       
P.O. Box 30001/MSC 4500                                                       
Las Cruces, NM 88003                                                          
Tel: 575-646-5333                                                             
FAX: 575-646-1602                                                             
murphy@nmsu.edu                                                               
                                                                              
