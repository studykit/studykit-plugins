# OffsetFeature.attributes Property

Parent Object: [OffsetFeature](OffsetFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetFeature\_var" is a variable referencing an OffsetFeature object. |

"offsetFeature\_var" is a variable referencing an OffsetFeature object. ```` ``` #include <Fusion/Features/OffsetFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = offsetFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |