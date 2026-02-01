# Setups.objectType Property

Parent Object: [Setups](Setups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setups.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setups\_var" is a variable referencing a Setups object.  ```` ``` # Get the value of the property. propertyValue = setups_var.objectType ``` ```` |

"setups\_var" is a variable referencing a Setups object. ```` ``` #include <Cam/CAM/Setups.h>  // Get the value of the property. string propertyValue = setups_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |