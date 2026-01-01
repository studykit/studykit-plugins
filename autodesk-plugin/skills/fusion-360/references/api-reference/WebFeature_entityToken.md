# WebFeature.entityToken Property

Parent Object: [WebFeature](WebFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeature.h>

## Description

Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeature\_var" is a variable referencing a WebFeature object.  ```` ``` # Get the value of the property. propertyValue = webFeature_var.entityToken ``` ```` |

"webFeature\_var" is a variable referencing a WebFeature object. ```` ``` #include <Fusion/Features/WebFeature.h>  // Get the value of the property. string propertyValue = webFeature_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |