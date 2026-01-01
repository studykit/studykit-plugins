# ArrangePlaneEnvelopeDefinition.originXOffset Property

Parent Object: [ArrangePlaneEnvelopeDefinition](ArrangePlaneEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneEnvelopeDefinition.h>

## Description

Returns the parameter that controls the X offset of the frame from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangePlaneEnvelopeDefinition\_var" is a variable referencing an ArrangePlaneEnvelopeDefinition object. |

"arrangePlaneEnvelopeDefinition\_var" is a variable referencing an ArrangePlaneEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangePlaneEnvelopeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = arrangePlaneEnvelopeDefinition_var->originXOffset(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |