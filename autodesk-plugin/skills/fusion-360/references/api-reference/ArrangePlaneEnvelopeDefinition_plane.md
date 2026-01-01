# ArrangePlaneEnvelopeDefinition.plane Property

Parent Object: [ArrangePlaneEnvelopeDefinition](ArrangePlaneEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneEnvelopeDefinition.h>

## Description

Gets and sets the ConstructionPlane the envelope is defined on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangePlaneEnvelopeDefinition\_var" is a variable referencing an ArrangePlaneEnvelopeDefinition object. |

"arrangePlaneEnvelopeDefinition\_var" is a variable referencing an ArrangePlaneEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangePlaneEnvelopeDefinition.h>  // Get the value of the property. Ptr<ConstructionPlane> propertyValue = arrangePlaneEnvelopeDefinition_var->plane();  // Set the value of the property, where value_var is a ConstructionPlane. bool returnValue = arrangePlaneEnvelopeDefinition_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConstructionPlane](ConstructionPlane.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |