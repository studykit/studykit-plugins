# RemoveFeature.attributes Property

Parent Object: [RemoveFeature](RemoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeature\_var" is a variable referencing a RemoveFeature object. |

"removeFeature\_var" is a variable referencing a RemoveFeature object. ```` ``` #include <Fusion/Features/RemoveFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = removeFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |