# Arrange3DEnvelopeDefinition.plane Property

Parent Object: [Arrange3DEnvelopeDefinition](Arrange3DEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DEnvelopeDefinition.h>

## Description

Gets and sets the ConstructionPlane the envelope is defined on.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DEnvelopeDefinition\_var" is a variable referencing an Arrange3DEnvelopeDefinition object. |

"arrange3DEnvelopeDefinition\_var" is a variable referencing an Arrange3DEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/Arrange3DEnvelopeDefinition.h>  // Get the value of the property. Ptr<ConstructionPlane> propertyValue = arrange3DEnvelopeDefinition_var->plane();  // Set the value of the property, where value_var is a ConstructionPlane. bool returnValue = arrange3DEnvelopeDefinition_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConstructionPlane](ConstructionPlane.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |