# FlatPatternProduct.allParameters Property

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Returns a read only list of all parameters in the design. This includes the user parameters and model parameters from all components in this design. The parameters from Externally Referenced components are NOT included because they are in actuality, separate designs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. |

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Get the value of the property. Ptr<ParameterList> propertyValue = flatPatternProduct_var->allParameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [ParameterList](ParameterList.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |