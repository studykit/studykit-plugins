# USDExportOptions.objectType Property

Parent Object: [USDExportOptions](USDExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/USDExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"uSDExportOptions\_var" is a variable referencing a USDExportOptions object.  ```` ``` # Get the value of the property. propertyValue = uSDExportOptions_var.objectType ``` ```` |

"uSDExportOptions\_var" is a variable referencing a USDExportOptions object. ```` ``` #include <Fusion/Fusion/USDExportOptions.h>  // Get the value of the property. string propertyValue = uSDExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |