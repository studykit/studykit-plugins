# Arrange2DProfileOrFaceEnvelopeInput.objectSpacing Property

Parent Object: [Arrange2DProfileOrFaceEnvelopeInput](Arrange2DProfileOrFaceEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DProfileOrFaceEnvelopeInput.h>

## Description

Specifies the minimum clearance between components in the arrangement. for a 3D layout this also specified the distance between the components in the Z direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DProfileOrFaceEnvelopeInput\_var" is a variable referencing an Arrange2DProfileOrFaceEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrange2DProfileOrFaceEnvelopeInput_var.objectSpacing  # Set the value of the property. arrange2DProfileOrFaceEnvelopeInput_var.objectSpacing = propertyValue ``` ```` |

"arrange2DProfileOrFaceEnvelopeInput\_var" is a variable referencing an Arrange2DProfileOrFaceEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DProfileOrFaceEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrange2DProfileOrFaceEnvelopeInput_var->objectSpacing();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrange2DProfileOrFaceEnvelopeInput_var->objectSpacing(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |