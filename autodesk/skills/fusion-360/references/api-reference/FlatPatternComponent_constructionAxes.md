# FlatPatternComponent.constructionAxes Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns the construction axes collection associated with this component. This provides access to the existing construction axes and supports the creation of new construction axes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. Ptr<ConstructionAxes> propertyValue = flatPatternComponent_var->constructionAxes(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConstructionAxes](ConstructionAxes.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |