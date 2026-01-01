# FlatPatternProduct.exportManager Property

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Returns the ExportManager for this design. You use the ExportManager to export the current design in various formats.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. |

"flatPatternProduct\_var" is a variable referencing a FlatPatternProduct object. ```` ``` #include <Fusion/SheetMetal/FlatPatternProduct.h>  // Get the value of the property. Ptr<ExportManager> propertyValue = flatPatternProduct_var->exportManager(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExportManager](ExportManager.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |