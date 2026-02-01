# Arrange2DEnvelopeInput.objectSpacing Property

Parent Object: [Arrange2DEnvelopeInput](Arrange2DEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DEnvelopeInput.h>

## Description

Specifies the minimum clearance between components in the arrangement. for a 3D layout this also specified the distance between the components in the Z direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DEnvelopeInput\_var" is a variable referencing an Arrange2DEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrange2DEnvelopeInput_var.objectSpacing  # Set the value of the property. arrange2DEnvelopeInput_var.objectSpacing = propertyValue ``` ```` |

"arrange2DEnvelopeInput\_var" is a variable referencing an Arrange2DEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrange2DEnvelopeInput_var->objectSpacing();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrange2DEnvelopeInput_var->objectSpacing(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |