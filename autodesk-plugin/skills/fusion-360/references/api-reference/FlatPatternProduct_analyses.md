# FlatPatternProduct.analyses Property

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Gets the collection of design analyses associated with this design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. |

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Get the value of the property. Ptr<Analyses> propertyValue = flatPatternProduct_var->analyses(); ``` ```` |

## Property Value

This is a read only property whose value is an [Analyses](Analyses.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |