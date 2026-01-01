# ExtrudeFeature.extentTwo Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Gets and sets the extent used for side two of the extrusion. If the extrude is a single sided extrude this property will return null and will fail if set. The hasTwoExtents property can be used to determine if there are two sides or not. When setting this property, valid inputs are DistanceExtentDefinition, ToEntityExtentDefinition, and ThroughAllExtentDefinition object, which can be created statically using the create method on the classes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeature_var.extentTwo  # Set the value of the property. extrudeFeature_var.extentTwo = propertyValue ``` ```` |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = extrudeFeature_var->extentTwo();  // Set the value of the property, where value_var is an ExtentDefinition. bool returnValue = extrudeFeature_var->extentTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtentDefinition](ExtentDefinition.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |