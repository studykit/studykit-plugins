# PDFExportOptions.useLineWeights Property

Parent Object: [PDFExportOptions](PDFExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/PDFExportOptions.h>

## Description

Specifies if line weights should be used in the exported PDF file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. |

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. ```` ``` #include <Drawing/Drawing/PDFExportOptions.h>  // Get the value of the property. boolean propertyValue = pDFExportOptions_var->useLineWeights();  // Set the value of the property, where value_var is a boolean. bool returnValue = pDFExportOptions_var->useLineWeights(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |