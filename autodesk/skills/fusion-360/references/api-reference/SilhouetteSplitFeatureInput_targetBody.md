# SilhouetteSplitFeatureInput.targetBody Property

Parent Object: [SilhouetteSplitFeatureInput](SilhouetteSplitFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatureInput.h>

## Description

Gets and sets the solid body to split.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. |

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeatureInput.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = silhouetteSplitFeatureInput_var->targetBody();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = silhouetteSplitFeatureInput_var->targetBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |