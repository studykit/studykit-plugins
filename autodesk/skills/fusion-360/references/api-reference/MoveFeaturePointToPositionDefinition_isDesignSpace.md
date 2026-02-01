# MoveFeaturePointToPositionDefinition.isDesignSpace Property

Parent Object: [MoveFeaturePointToPositionDefinition](MoveFeaturePointToPositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeaturePointToPositionDefinition.h>

## Description

Gets and sets if the translation is defined with respect to the design or component space. Design space is the same as the root component space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeaturePointToPositionDefinition\_var" is a variable referencing a MoveFeaturePointToPositionDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeaturePointToPositionDefinition_var.isDesignSpace  # Set the value of the property. moveFeaturePointToPositionDefinition_var.isDesignSpace = propertyValue ``` ```` |

"moveFeaturePointToPositionDefinition\_var" is a variable referencing a MoveFeaturePointToPositionDefinition object. ```` ``` #include <Fusion/Features/MoveFeaturePointToPositionDefinition.h>  // Get the value of the property. boolean propertyValue = moveFeaturePointToPositionDefinition_var->isDesignSpace();  // Set the value of the property, where value_var is a boolean. bool returnValue = moveFeaturePointToPositionDefinition_var->isDesignSpace(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |