# Arrange2DPlaneEnvelopeInput.width Property

Parent Object: [Arrange2DPlaneEnvelopeInput](Arrange2DPlaneEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>

## Description

Gets and sets the width of the envelope. This is the size of the envelope as measured along the Y axis of the specified construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrange2DPlaneEnvelopeInput_var.width  # Set the value of the property. arrange2DPlaneEnvelopeInput_var.width = propertyValue ``` ```` |

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrange2DPlaneEnvelopeInput_var->width();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrange2DPlaneEnvelopeInput_var->width(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |