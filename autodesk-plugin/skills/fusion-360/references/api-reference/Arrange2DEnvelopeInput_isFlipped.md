# Arrange2DEnvelopeInput.isFlipped Property

Parent Object: [Arrange2DEnvelopeInput](Arrange2DEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DEnvelopeInput.h>

## Description

Specifies if the arrangement of objects is so they are above or X-Y plane of the envelope. Defaults to false so the objects are above the construction plane, profile or face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DEnvelopeInput\_var" is a variable referencing an Arrange2DEnvelopeInput object. |

"arrange2DEnvelopeInput\_var" is a variable referencing an Arrange2DEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DEnvelopeInput.h>  // Get the value of the property. boolean propertyValue = arrange2DEnvelopeInput_var->isFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrange2DEnvelopeInput_var->isFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |