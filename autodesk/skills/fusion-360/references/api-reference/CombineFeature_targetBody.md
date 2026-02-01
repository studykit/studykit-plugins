# CombineFeature.targetBody Property

Parent Object: [CombineFeature](CombineFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeature.h>

## Description

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeature\_var" is a variable referencing a CombineFeature object. |

"combineFeature\_var" is a variable referencing a CombineFeature object. ```` ``` #include <Fusion/Features/CombineFeature.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = combineFeature_var->targetBody();  // Set the value of the property, where value_var is a BRepBody. bool returnValue = combineFeature_var->targetBody(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |