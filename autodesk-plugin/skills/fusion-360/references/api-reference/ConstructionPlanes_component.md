# ConstructionPlanes.component Property

Parent Object: [ConstructionPlanes](ConstructionPlanes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlanes.h>

## Description

Returns the component that owns this collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlanes\_var" is a variable referencing a ConstructionPlanes object. |

"constructionPlanes\_var" is a variable referencing a ConstructionPlanes object. ```` ``` #include <Fusion/Construction/ConstructionPlanes.h>  // Get the value of the property. Ptr<Component> propertyValue = constructionPlanes_var->component(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |