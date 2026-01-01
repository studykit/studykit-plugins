# ConstructionPointDefinition.isValid Property

Parent Object: [ConstructionPointDefinition](ConstructionPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointDefinition.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointDefinition\_var" is a variable referencing a ConstructionPointDefinition object. |

"constructionPointDefinition\_var" is a variable referencing a ConstructionPointDefinition object. ```` ``` #include <Fusion/Construction/ConstructionPointDefinition.h>  // Get the value of the property. boolean propertyValue = constructionPointDefinition_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |