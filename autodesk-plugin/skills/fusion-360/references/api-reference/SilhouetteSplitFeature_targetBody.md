# SilhouetteSplitFeature.targetBody Property

Parent Object: [SilhouetteSplitFeature](SilhouetteSplitFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeature.h>

## Description

Gets and sets the solid body to split.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object.  ```` ``` # Get the value of the property. propertyValue = silhouetteSplitFeature_var.targetBody  # Set the value of the property. silhouetteSplitFeature_var.targetBody = propertyValue ``` ```` |

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeature.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = silhouetteSplitFeature_var->targetBody();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = silhouetteSplitFeature_var->targetBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |