# MAVEN MAG Calibrated Data Bundle - Errata

This document describes known errors or deficiencies in the MAVEN MAG Calibrated Data Bundle.

===============================================================================================

During MAVEN Release 21, released on 2020-05-15, minor updates were made to the PDS4 labels of
previously released data products. These updates did not change the previously released data.

During later review of the bundle, an inconsistency was found in the `version_id` values of some
PDS4 product labels. Labels for products released through 2019-11-14 were expected to have their
`version_id` incremented to 1.1 as part of the MAVEN Release 21 label updates. However, some
labels for products released after that date also had their `version_id` incremented to 1.1,
even though no version 1.0 existed. This resulted in inconsistent label versioning for some
products.

The data products themselves were not changed as part of this versioning inconsistency. Beginning
with MAVEN Release 45, the affected labels are being updated with a version 1.2 to account
for current label metadata updates, including the addition of units to applicable label fields.
The existing versioning inconsistency is documented here for user awareness.

===============================================================================================

For questions or problems regarding this bundle, please contact the PDS/PPI operator:

Email [pds_operator@igpp.ucla.edu](mailto:pds_operator@igpp.ucla.edu)
