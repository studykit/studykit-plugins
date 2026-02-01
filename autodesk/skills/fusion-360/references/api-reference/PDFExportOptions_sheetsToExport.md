# PDFExportOptions.sheetsToExport Property

Parent Object: [PDFExportOptions](PDFExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/PDFExportOptions.h>

## Description

Defines which sheets to export. Defaults to AllPDFSheets which will create a single PDF file containing all sheets in the drawing.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object.  ```` ``` # Get the value of the property. propertyValue = pDFExportOptions_var.sheetsToExport  # Set the value of the property. pDFExportOptions_var.sheetsToExport = propertyValue ``` ```` |

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. ```` ``` #include <Drawing/Drawing/PDFExportOptions.h>  // Get the value of the property. PDFSheetsExport propertyValue = pDFExportOptions_var->sheetsToExport();  // Set the value of the property, where value_var is a PDFSheetsExport. bool returnValue = pDFExportOptions_var->sheetsToExport(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PDFSheetsExport](PDFSheetsExport.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |