# FlatPatternProduct.activeOccurrence Property

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Returns the occurrence that is currently activated, if any. This can return null in the case where no occurrence is activated and the root component is active.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. |

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = flatPatternProduct_var->activeOccurrence(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| Â© Copyright 2025 Autodesk, Inc. | Comment on this page. |