# LoftCenterLineOrRail.edgeCondition Property

Parent Object: [LoftCenterLineOrRail](LoftCenterLineOrRail.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftCenterLineOrRail.h>

## Description

Gets and sets the edge condition for this rail. This value is only applicable when a BRepEdge is used as the rail entity. If sketch geometry is used, this value is ignored. The property defaults to G0LoftRailEdgeCondition.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftCenterLineOrRail\_var" is a variable referencing a LoftCenterLineOrRail object.  ```` ``` # Get the value of the property. propertyValue = loftCenterLineOrRail_var.edgeCondition  # Set the value of the property. loftCenterLineOrRail_var.edgeCondition = propertyValue ``` ```` |

"loftCenterLineOrRail\_var" is a variable referencing a LoftCenterLineOrRail object. ```` ``` #include <Fusion/Features/LoftCenterLineOrRail.h>  // Get the value of the property. LoftRailEdgeConditions propertyValue = loftCenterLineOrRail_var->edgeCondition();  // Set the value of the property, where value_var is a LoftRailEdgeConditions. bool returnValue = loftCenterLineOrRail_var->edgeCondition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [LoftRailEdgeConditions](LoftRailEdgeConditions.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |