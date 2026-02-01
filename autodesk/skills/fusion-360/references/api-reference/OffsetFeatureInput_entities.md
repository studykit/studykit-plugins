# OffsetFeatureInput.entities Property

Parent Object: [OffsetFeatureInput](OffsetFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatureInput.h>

## Description

An ObjectCollection containing the BRepFace objects being offset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. |

"offsetFeatureInput\_var" is a variable referencing an OffsetFeatureInput object. ```` ``` #include <Fusion/Features/OffsetFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = offsetFeatureInput_var->entities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = offsetFeatureInput_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |