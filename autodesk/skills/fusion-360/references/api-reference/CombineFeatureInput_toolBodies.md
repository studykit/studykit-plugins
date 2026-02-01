# CombineFeatureInput.toolBodies Property

Parent Object: [CombineFeatureInput](CombineFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CombineFeatureInput.h>

## Description

## Syntax

* [Python](#Python)
* [C++](#C++)

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. |

"combineFeatureInput\_var" is a variable referencing a CombineFeatureInput object. ```` ``` #include <Fusion/Features/CombineFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = combineFeatureInput_var->toolBodies();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = combineFeatureInput_var->toolBodies(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |