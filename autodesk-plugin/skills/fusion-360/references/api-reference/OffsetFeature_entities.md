# OffsetFeature.entities Property

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

Gets and sets the faces to be offset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an OffsetFeature object.  ```` ``` # Get the value of the property. propertyValue = offsetFeature_var.entities  # Set the value of the property. offsetFeature_var.entities = propertyValue ``` ```` |

"offsetFeature\_var" is a variable referencing an OffsetFeature object. ```` ``` #include <Fusion/Features/OffsetFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = offsetFeature_var->entities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = offsetFeature_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |