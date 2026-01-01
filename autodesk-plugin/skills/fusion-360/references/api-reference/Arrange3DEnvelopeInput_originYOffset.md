# Arrange3DEnvelopeInput.originYOffset Property

Parent Object: [Arrange3DEnvelopeInput](Arrange3DEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DEnvelopeInput.h>

## Description

Gets and sets the Y offset of the envelope from the origin of the construction plane. This value defaults to zero.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DEnvelopeInput\_var" is a variable referencing an Arrange3DEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrange3DEnvelopeInput_var.originYOffset  # Set the value of the property. arrange3DEnvelopeInput_var.originYOffset = propertyValue ``` ```` |

"arrange3DEnvelopeInput\_var" is a variable referencing an Arrange3DEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange3DEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrange3DEnvelopeInput_var->originYOffset();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrange3DEnvelopeInput_var->originYOffset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |