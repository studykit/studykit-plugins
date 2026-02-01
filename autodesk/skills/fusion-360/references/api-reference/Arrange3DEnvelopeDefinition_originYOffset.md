# Arrange3DEnvelopeDefinition.originYOffset Property

Parent Object: [Arrange3DEnvelopeDefinition](Arrange3DEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DEnvelopeDefinition.h>

## Description

Returns the parameter that controls the Y offset of the envelope volume from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DEnvelopeDefinition\_var" is a variable referencing an Arrange3DEnvelopeDefinition object. |

"arrange3DEnvelopeDefinition\_var" is a variable referencing an Arrange3DEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/Arrange3DEnvelopeDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = arrange3DEnvelopeDefinition_var->originYOffset(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |