# FlatPatternProduct.createConfiguredDesign Method

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Converts this design into a configured design. The returned ConfigurationTable has a single row and no columns. You can use it to add columns and rows to define the configuration.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.```` ``` returnValue = flatPatternProduct_var.createConfiguredDesign() ``` ```` |

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationTopTable](ConfigurationTopTable.htm) | Returns the ConfigurationTable that defines the configurations for this design. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |