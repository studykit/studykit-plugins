# BaseFeature.attributes Property

Parent Object: [BaseFeature](BaseFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BaseFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseFeature\_var" is a variable referencing a BaseFeature object. |

"baseFeature\_var" is a variable referencing a BaseFeature object. ```` ``` #include <Fusion/Features/BaseFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = baseFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |