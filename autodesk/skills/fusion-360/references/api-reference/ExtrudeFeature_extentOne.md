# ExtrudeFeature.extentOne Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Gets and sets the extent used for a single sided extrude or side one of a two-sided extrusion. Valid inputs are DistanceExtentDefinition, ToEntityExtentDefinition, and ThroughAllExtentDefinition object, which can be created statically using the create method on the classes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeature_var.extentOne  # Set the value of the property. extrudeFeature_var.extentOne = propertyValue ``` ```` |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = extrudeFeature_var->extentOne();  // Set the value of the property, where value_var is an ExtentDefinition. bool returnValue = extrudeFeature_var->extentOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtentDefinition](ExtentDefinition.htm).

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