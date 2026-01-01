# MoveFeaturePointToPositionDefinition.point Property

Parent Object: [MoveFeaturePointToPositionDefinition](MoveFeaturePointToPositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeaturePointToPositionDefinition.h>

## Description

Gets and sets the entity that defines a point in space. This can be a sketch point, a construction point, or a BRepVertex.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeaturePointToPositionDefinition\_var" is a variable referencing a MoveFeaturePointToPositionDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeaturePointToPositionDefinition_var.point  # Set the value of the property. moveFeaturePointToPositionDefinition_var.point = propertyValue ``` ```` |

"moveFeaturePointToPositionDefinition\_var" is a variable referencing a MoveFeaturePointToPositionDefinition object. ```` ``` #include <Fusion/Features/MoveFeaturePointToPositionDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = moveFeaturePointToPositionDefinition_var->point();  // Set the value of the property, where value_var is a Base. bool returnValue = moveFeaturePointToPositionDefinition_var->point(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |