# PropertyGroups.objectType Property

Parent Object: [PropertyGroups](PropertyGroups.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroups.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroups\_var" is a variable referencing a PropertyGroups object.  ```` ``` # Get the value of the property. propertyValue = propertyGroups_var.objectType ``` ```` |

"propertyGroups\_var" is a variable referencing a PropertyGroups object. ```` ``` #include <Core/Application/PropertyGroups.h>  // Get the value of the property. string propertyValue = propertyGroups_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |