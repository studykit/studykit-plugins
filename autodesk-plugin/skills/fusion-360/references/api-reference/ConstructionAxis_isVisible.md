# ConstructionAxis.isVisible Property

Parent Object: [ConstructionAxis](ConstructionAxis.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxis.h>

## Description

Gets if the construction plane is visible. This property is affected by the AssemblyContext of the construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. |

"constructionAxis\_var" is a variable referencing a ConstructionAxis object. ```` ``` #include <Fusion/Construction/ConstructionAxis.h>  // Get the value of the property. boolean propertyValue = constructionAxis_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |