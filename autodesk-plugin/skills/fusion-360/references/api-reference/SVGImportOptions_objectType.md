# SVGImportOptions.objectType Property

Parent Object: [SVGImportOptions](SVGImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SVGImportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object.  ```` ``` # Get the value of the property. propertyValue = sVGImportOptions_var.objectType ``` ```` |

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object. ```` ``` #include <Core/Application/SVGImportOptions.h>  // Get the value of the property. string propertyValue = sVGImportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |