# Arrange3DEnvelopeInput.plane Property

Parent Object: [Arrange3DEnvelopeInput](Arrange3DEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DEnvelopeInput.h>

## Description

Gets and sets the construction plane that will be used for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DEnvelopeInput\_var" is a variable referencing an Arrange3DEnvelopeInput object. |

"arrange3DEnvelopeInput\_var" is a variable referencing an Arrange3DEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange3DEnvelopeInput.h>  // Get the value of the property. Ptr<ConstructionPlane> propertyValue = arrange3DEnvelopeInput_var->plane();  // Set the value of the property, where value_var is a ConstructionPlane. bool returnValue = arrange3DEnvelopeInput_var->plane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConstructionPlane](ConstructionPlane.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |