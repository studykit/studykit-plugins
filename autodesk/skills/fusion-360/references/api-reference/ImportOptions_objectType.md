# ImportOptions.objectType Property

Parent Object: [ImportOptions](ImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ImportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"importOptions\_var" is a variable referencing an ImportOptions object.  ```` ``` # Get the value of the property. propertyValue = importOptions_var.objectType ``` ```` |

"importOptions\_var" is a variable referencing an ImportOptions object. ```` ``` #include <Core/Application/ImportOptions.h>  // Get the value of the property. string propertyValue = importOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |