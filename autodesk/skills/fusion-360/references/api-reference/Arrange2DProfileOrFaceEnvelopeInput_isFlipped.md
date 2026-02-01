# Arrange2DProfileOrFaceEnvelopeInput.isFlipped Property

Parent Object: [Arrange2DProfileOrFaceEnvelopeInput](Arrange2DProfileOrFaceEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DProfileOrFaceEnvelopeInput.h>

## Description

Specifies if the arrangement of objects is so they are above or X-Y plane of the envelope. Defaults to false so the objects are above the construction plane, profile or face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DProfileOrFaceEnvelopeInput\_var" is a variable referencing an Arrange2DProfileOrFaceEnvelopeInput object. |

"arrange2DProfileOrFaceEnvelopeInput\_var" is a variable referencing an Arrange2DProfileOrFaceEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DProfileOrFaceEnvelopeInput.h>  // Get the value of the property. boolean propertyValue = arrange2DProfileOrFaceEnvelopeInput_var->isFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrange2DProfileOrFaceEnvelopeInput_var->isFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |