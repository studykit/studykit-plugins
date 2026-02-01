# IGESExportOptions.objectType Property

Parent Object: [IGESExportOptions](IGESExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IGESExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"iGESExportOptions\_var" is a variable referencing an IGESExportOptions object.  ```` ``` # Get the value of the property. propertyValue = iGESExportOptions_var.objectType ``` ```` |

"iGESExportOptions\_var" is a variable referencing an IGESExportOptions object. ```` ``` #include <Fusion/Fusion/IGESExportOptions.h>  // Get the value of the property. string propertyValue = iGESExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |