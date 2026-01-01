# ArrangeEnvelopeDefinition.frameWidth Property

Parent Object: [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeEnvelopeDefinition.h>

## Description

Returns the parameter that controls the width of the envelope frame. This defines the offset distance of the objects from the edge of the frame. You can modify the value by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeEnvelopeDefinition\_var" is a variable referencing an ArrangeEnvelopeDefinition object. |

"arrangeEnvelopeDefinition\_var" is a variable referencing an ArrangeEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangeEnvelopeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = arrangeEnvelopeDefinition_var->frameWidth(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |