# FormFeature.attributes Property

Parent Object: [FormFeature](FormFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FormFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"formFeature\_var" is a variable referencing a FormFeature object. |

"formFeature\_var" is a variable referencing a FormFeature object. ```` ``` #include <Fusion/Features/FormFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = formFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |