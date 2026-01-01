# MoveFeaturePointToPointDefinition.targetPoint Property

Parent Object: [MoveFeaturePointToPointDefinition](MoveFeaturePointToPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeaturePointToPointDefinition.h>

## Description

Gets and sets the second point that defines the direction and distance of the move.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeaturePointToPointDefinition\_var" is a variable referencing a MoveFeaturePointToPointDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeaturePointToPointDefinition_var.targetPoint  # Set the value of the property. moveFeaturePointToPointDefinition_var.targetPoint = propertyValue ``` ```` |

"moveFeaturePointToPointDefinition\_var" is a variable referencing a MoveFeaturePointToPointDefinition object. ```` ``` #include <Fusion/Features/MoveFeaturePointToPointDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = moveFeaturePointToPointDefinition_var->targetPoint();  // Set the value of the property, where value_var is a Base. bool returnValue = moveFeaturePointToPointDefinition_var->targetPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |