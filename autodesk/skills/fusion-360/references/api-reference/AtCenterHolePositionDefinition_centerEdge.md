# AtCenterHolePositionDefinition.centerEdge Property

Parent Object: [AtCenterHolePositionDefinition](AtCenterHolePositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AtCenterHolePositionDefinition.h>

## Description

Returns the circular or elliptical edge the hole is centered at.

## Syntax

* [Python](#Python)
* [C++](#C++)

"atCenterHolePositionDefinition\_var" is a variable referencing an AtCenterHolePositionDefinition object. |

"atCenterHolePositionDefinition\_var" is a variable referencing an AtCenterHolePositionDefinition object. ```` ``` #include <Fusion/Features/AtCenterHolePositionDefinition.h>  // Get the value of the property. Ptr<BRepEdge> propertyValue = atCenterHolePositionDefinition_var->centerEdge(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepEdge](BRepEdge.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |