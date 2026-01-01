# ThroughAllExtentDefinition.isPositiveDirection Property

Parent Object: [ThroughAllExtentDefinition](ThroughAllExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThroughAllExtentDefinition.h>

## Description

Gets and sets if the direction is positive or negative. A value of true indicates it is in the same direction as the z direction of the profile's sketch plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"throughAllExtentDefinition\_var" is a variable referencing a ThroughAllExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = throughAllExtentDefinition_var.isPositiveDirection  # Set the value of the property. throughAllExtentDefinition_var.isPositiveDirection = propertyValue ``` ```` |

"throughAllExtentDefinition\_var" is a variable referencing a ThroughAllExtentDefinition object. ```` ``` #include <Fusion/Features/ThroughAllExtentDefinition.h>  // Get the value of the property. boolean propertyValue = throughAllExtentDefinition_var->isPositiveDirection();  // Set the value of the property, where value_var is a boolean. bool returnValue = throughAllExtentDefinition_var->isPositiveDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

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