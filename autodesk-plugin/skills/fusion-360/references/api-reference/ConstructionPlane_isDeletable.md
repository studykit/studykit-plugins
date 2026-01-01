# ConstructionPlane.isDeletable Property

Parent Object: [ConstructionPlane](ConstructionPlane.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

Indicates if this construction plane can be deleted. Base construction planes can not be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. |

"constructionPlane\_var" is a variable referencing a ConstructionPlane object. ```` ``` #include <Fusion/Construction/ConstructionPlane.h>  // Get the value of the property. boolean propertyValue = constructionPlane_var->isDeletable(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |