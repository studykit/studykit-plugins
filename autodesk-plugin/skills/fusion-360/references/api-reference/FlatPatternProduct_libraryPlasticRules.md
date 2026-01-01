# FlatPatternProduct.libraryPlasticRules Property

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Gets the collection of plastic rules in the plastic rule library.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. |

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Get the value of the property. Ptr<PlasticRules> propertyValue = flatPatternProduct_var->libraryPlasticRules(); ``` ```` |

## Property Value

This is a read only property whose value is a [PlasticRules](PlasticRules.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |