# ConstructionPlane.entityToken Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Returns a token for the ConstructionPlane object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object.  ```` ``` # Get the value of the property. propertyValue = constructionPlane_var.entityToken ``` ```` |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. string propertyValue = constructionPlane_var->entityToken(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |