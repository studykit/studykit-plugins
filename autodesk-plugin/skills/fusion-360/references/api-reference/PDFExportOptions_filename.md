# PDFExportOptions.filename Property

Parent Object: [PDFExportOptions](PDFExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/PDFExportOptions.h>

## Description

Gets and sets the filename that the exported file will be written to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. |

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. ```` ``` #include <Drawing/Drawing/PDFExportOptions.h>  // Get the value of the property. string propertyValue = pDFExportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = pDFExportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |