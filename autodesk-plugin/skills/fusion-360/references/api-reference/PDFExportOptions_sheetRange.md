# PDFExportOptions.sheetRange Property

Parent Object: [PDFExportOptions](PDFExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/PDFExportOptions.h>

## Description

Defines the range of sheets to export. This can be a string like "1-3" or "1-2,5" where you can define a range of sheets and also specific sheets. Setting this property will automatically set the sheetsToExport setting to SelectedPDFSheets.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. |

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. ```` ``` #include <Drawing/Drawing/PDFExportOptions.h>  // Get the value of the property. string propertyValue = pDFExportOptions_var->sheetRange();  // Set the value of the property, where value_var is a string. bool returnValue = pDFExportOptions_var->sheetRange(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |