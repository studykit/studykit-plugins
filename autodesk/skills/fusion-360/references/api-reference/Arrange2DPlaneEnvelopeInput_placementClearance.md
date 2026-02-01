# Arrange2DPlaneEnvelopeInput.placementClearance Property

Parent Object: [Arrange2DPlaneEnvelopeInput](Arrange2DPlaneEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>

## Description

Specifies the distance of the components and the bottom of the envelope. This raises the components above the X-Y plane of the specified construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrange2DPlaneEnvelopeInput_var.placementClearance  # Set the value of the property. arrange2DPlaneEnvelopeInput_var.placementClearance = propertyValue ``` ```` |

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrange2DPlaneEnvelopeInput_var->placementClearance();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrange2DPlaneEnvelopeInput_var->placementClearance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |