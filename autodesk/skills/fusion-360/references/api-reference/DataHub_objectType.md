# DataHub.objectType Property

Parent Object: [DataHub](DataHub.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHub\_var" is a variable referencing a DataHub object.  ```` ``` # Get the value of the property. propertyValue = dataHub_var.objectType ``` ```` |

"dataHub\_var" is a variable referencing a DataHub object. ```` ``` #include <Core/Dashboard/DataHub.h>  // Get the value of the property. string propertyValue = dataHub_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |