# ChainSelection Object

Derived from: [CurveSelection](CurveSelection.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ChainSelection.h>

## Description

Represents a chain type of curve selection. Allows B-Rep edges and sketch geometry for the inputGeometry property. The automatic tool side detection is currently disabled when using the API, thus the side is determined based on the direction of the first edge and the z-axis of the tool orientation.