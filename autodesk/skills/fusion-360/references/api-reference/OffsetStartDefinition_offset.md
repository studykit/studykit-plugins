# OffsetStartDefinition.offset Property

Parent Object: [OffsetStartDefinition](OffsetStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetStartDefinition.h>

## Description

Gets the currently defined offset value. If the ProfilePlaneWithOffsetDefinition object was created statically and is not associated with a feature, this will return a ValueInput object. if the ProfilePlaneWithOffsetDefinition is associated with an existing feature, this will return the parameter that was created when the feature was created. To edit the offset, use properties on the parameter to change the value of the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetStartDefinition\_var" is a variable referencing an OffsetStartDefinition object. |

"offsetStartDefinition\_var" is a variable referencing an OffsetStartDefinition object. ```` ``` #include <Fusion/Features/OffsetStartDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = offsetStartDefinition_var->offset(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |