# Arrange2DEnvelopeInput.frameWidth Property

Parent Object: [Arrange2DEnvelopeInput](Arrange2DEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DEnvelopeInput.h>

## Description

Specifies the minimum distance between the components in the arrangement and the envelope frame.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DEnvelopeInput\_var" is a variable referencing an Arrange2DEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrange2DEnvelopeInput_var.frameWidth  # Set the value of the property. arrange2DEnvelopeInput_var.frameWidth = propertyValue ``` ```` |

"arrange2DEnvelopeInput\_var" is a variable referencing an Arrange2DEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrange2DEnvelopeInput_var->frameWidth();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrange2DEnvelopeInput_var->frameWidth(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |