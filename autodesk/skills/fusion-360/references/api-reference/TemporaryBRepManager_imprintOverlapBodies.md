# TemporaryBRepManager.imprintOverlapBodies Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Method that finds regions of faces on two bodies which overlap and creates new bodies where the faces are split at the edges of the overlaps. This does not modify the original bodies but creates new temporary bodies that contain the imprints.

## Remarks

The picture below shows an example of imprinting. The picture on the left shows the initial two bodies that are positioned so there are coincident faces. The picture on the right shows the two bodies individually so you can see the result of the imprint and how the coincident faces were split.