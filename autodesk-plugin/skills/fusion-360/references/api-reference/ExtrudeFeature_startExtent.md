# ExtrudeFeature.startExtent Property

Parent Object: [ExtrudeFeature](ExtrudeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeature.h>

## Description

Gets and sets the extent used to define the start of the extrusion. You can set this property with either a ProfilePlaneStartDefinition, OffsetStartDefinition or a EntityStartDefinition object. You can get any of those objects by using the static create method on the class.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object.  ```` ``` # Get the value of the property. propertyValue = extrudeFeature_var.startExtent  # Set the value of the property. extrudeFeature_var.startExtent = propertyValue ``` ```` |

"extrudeFeature\_var" is a variable referencing an ExtrudeFeature object. ```` ``` #include <Fusion/Features/ExtrudeFeature.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = extrudeFeature_var->startExtent();  // Set the value of the property, where value_var is an ExtentDefinition. bool returnValue = extrudeFeature_var->startExtent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ExtentDefinition](ExtentDefinition.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |