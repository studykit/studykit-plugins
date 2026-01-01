# Arrange2DPlaneEnvelopeInput.plane Property

Parent Object: [Arrange2DPlaneEnvelopeInput](Arrange2DPlaneEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>

## Description

Gets and sets the construction plane that will be used for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object. |

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>  // Get the value of the property. Ptr<ConstructionPlane> propertyValue = arrange2DPlaneEnvelopeInput_var->plane();  // Set the value of the property, where value_var is a ConstructionPlane. bool returnValue = arrange2DPlaneEnvelopeInput_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConstructionPlane](ConstructionPlane.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |