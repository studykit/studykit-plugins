# ExtrudeFeatureInput.extentOne Property

Parent Object: [ExtrudeFeatureInput](ExtrudeFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

Gets the extent assigned for a single sided extrude or side one of a two-sided extrusion. To set the extent, use one of the set methods on the ExtrudeFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. |

"extrudeFeatureInput\_var" is a variable referencing an ExtrudeFeatureInput object. ```` ``` #include <Fusion/Features/ExtrudeFeatureInput.h>  // Get the value of the property. Ptr<ExtentDefinition> propertyValue = extrudeFeatureInput_var->extentOne(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExtentDefinition](ExtentDefinition.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |