# PlaneAndOffsetsHolePositionDefinition.offsetTwo Property

Parent Object: [PlaneAndOffsetsHolePositionDefinition](PlaneAndOffsetsHolePositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PlaneAndOffsetsHolePositionDefinition.h>

## Description

Returns the model parameter controlling the distance from the center of the hole to EdgeTwo. This property returns null in the case where only one edge is used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"planeAndOffsetsHolePositionDefinition\_var" is a variable referencing a PlaneAndOffsetsHolePositionDefinition object. |

"planeAndOffsetsHolePositionDefinition\_var" is a variable referencing a PlaneAndOffsetsHolePositionDefinition object. ```` ``` #include <Fusion/Features/PlaneAndOffsetsHolePositionDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = planeAndOffsetsHolePositionDefinition_var->offsetTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |