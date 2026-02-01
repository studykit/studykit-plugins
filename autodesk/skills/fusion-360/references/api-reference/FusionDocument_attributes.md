# FusionDocument.attributes Property

Parent Object: [FusionDocument](FusionDocument.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDocument.h>

## Description

Returns the collection of attributes associated with this document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDocument\_var" is a variable referencing a FusionDocument object. |

"fusionDocument\_var" is a variable referencing a FusionDocument object. ```` ``` #include <Fusion/Fusion/FusionDocument.h>  // Get the value of the property. Ptr<Attributes> propertyValue = fusionDocument_var->attributes(); ``` ```` |

## Property Value

This is a read only property whose value is an [Attributes](Attributes.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |