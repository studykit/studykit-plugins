# FlatPatternProduct.isContactSetAnalysis Property

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Gets and sets whether contact analysis is done using contact sets or between all bodies, independent of any contact sets. If True and the isContactAnalysisEnabled property is True then contact analysis is performed using contact sets. If False and isContactAnalysisEnabled is True, then contact analysis is performed between all bodies. If isContactAnalysisEnabled is False then no contact analysis is performed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. |

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Get the value of the property. boolean propertyValue = flatPatternProduct_var->isContactSetAnalysis();  // Set the value of the property, where value_var is a boolean. bool returnValue = flatPatternProduct_var->isContactSetAnalysis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |