# ExtrudeFeatureInput.startExtent Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Gets and sets the extent used to define the start of the extrusion. When a new ExtrudeFeatureInput object is created the start extent is initialized to be the profile plane but you can change it to a profile plane with offset or from an object by setting this property with either a OffsetStartDefinition or an EntityStartDefinition object. You can get either one of those objects by using the static create method on the class.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = extrudeFeatureInput_var->startExtent();  // Set the value of the property, where value_var is an ExtentDefinition. bool returnValue = extrudeFeatureInput_var->startExtent(value_var); ``` ```` |

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