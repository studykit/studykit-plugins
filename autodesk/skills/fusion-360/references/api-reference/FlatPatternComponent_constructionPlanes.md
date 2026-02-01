# FlatPatternComponent.constructionPlanes Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the construction planes collection associated with this component. This provides access to the existing construction planes and supports the creation of new construction planes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<ConstructionPlanes> propertyValue = flatPatternComponent_var->constructionPlanes(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionPlanes](ConstructionPlanes.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |