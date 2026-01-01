# ArrangeEnvelopeInput.objectSpacing Property

Parent Object: [ArrangeEnvelopeInput](ArrangeEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeEnvelopeInput.h>

## Description

Specifies the minimum clearance between components in the arrangement. for a 3D layout this also specified the distance between the components in the Z direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeEnvelopeInput\_var" is a variable referencing an ArrangeEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeEnvelopeInput_var.objectSpacing  # Set the value of the property. arrangeEnvelopeInput_var.objectSpacing = propertyValue ``` ```` |

"arrangeEnvelopeInput\_var" is a variable referencing an ArrangeEnvelopeInput object. ```` ``` #include <Fusion/Arrange/ArrangeEnvelopeInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = arrangeEnvelopeInput_var->objectSpacing();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = arrangeEnvelopeInput_var->objectSpacing(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |