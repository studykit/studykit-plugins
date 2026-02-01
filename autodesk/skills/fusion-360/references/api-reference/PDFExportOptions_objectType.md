# PDFExportOptions.objectType Property

Parent Object: [PDFExportOptions](PDFExportOptions.htm)
Defined in namespace "adsk::drawing" and the header file is <Drawing/Drawing/PDFExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object.  ```` ``` # Get the value of the property. propertyValue = pDFExportOptions_var.objectType ``` ```` |

"pDFExportOptions\_var" is a variable referencing a PDFExportOptions object. ```` ``` #include <Drawing/Drawing/PDFExportOptions.h>  // Get the value of the property. string propertyValue = pDFExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |