# SVGImportOptions.filename Property

Parent Object: [SVGImportOptions](SVGImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SVGImportOptions.h>

## Description

Gets and sets the filename or URL of the file to be imported.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object. |

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object. ```` ``` #include <Core/Application/SVGImportOptions.h>  // Get the value of the property. string propertyValue = sVGImportOptions_var->filename();  // Set the value of the property, where value_var is a string. bool returnValue = sVGImportOptions_var->filename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |