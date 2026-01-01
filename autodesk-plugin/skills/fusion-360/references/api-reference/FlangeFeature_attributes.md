# FlangeFeature.attributes Property

Parent Object: [FlangeFeature](FlangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeature.h>

## Description

Returns the collection of attributes associated with this face.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeature\_var" is a variable referencing a FlangeFeature object. |

"flangeFeature\_var" is a variable referencing a FlangeFeature object. ```` ``` #include <Fusion/SheetMetal/FlangeFeature.h>  // Get the value of the property. Ptr<Attributes> propertyValue = flangeFeature_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |