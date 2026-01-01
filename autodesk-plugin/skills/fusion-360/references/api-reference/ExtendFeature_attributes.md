# ExtendFeature.attributes Property

Parent Object: [ExtendFeature](ExtendFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtendFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"extendFeature\_var" is a variable referencing an ExtendFeature object. |

"extendFeature\_var" is a variable referencing an ExtendFeature object. ```` ``` #include <Fusion/Features/ExtendFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = extendFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |