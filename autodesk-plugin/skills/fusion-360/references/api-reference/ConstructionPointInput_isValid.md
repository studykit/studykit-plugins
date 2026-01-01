# ConstructionPointInput.isValid Property

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object. |

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object. ```` ``` #include <Fusion/Construction/ConstructionPointInput.h>  // Get the value of the property. boolean propertyValue = constructionPointInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |