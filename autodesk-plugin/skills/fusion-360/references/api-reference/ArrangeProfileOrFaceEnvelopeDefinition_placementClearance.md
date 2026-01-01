# ArrangeProfileOrFaceEnvelopeDefinition.placementClearance Property

Parent Object: [ArrangeProfileOrFaceEnvelopeDefinition](ArrangeProfileOrFaceEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeProfileOrFaceEnvelopeDefinition.h>

## Description

Returns the parameter that controls the offset of the objects from the base plane of the arrangement (the "up" direction). You can modify the value by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeProfileOrFaceEnvelopeDefinition\_var" is a variable referencing an ArrangeProfileOrFaceEnvelopeDefinition object. |

"arrangeProfileOrFaceEnvelopeDefinition\_var" is a variable referencing an ArrangeProfileOrFaceEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangeProfileOrFaceEnvelopeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = arrangeProfileOrFaceEnvelopeDefinition_var->placementClearance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |