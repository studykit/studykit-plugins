# PostConfigurationQuery.objectType Property

Parent Object: [PostConfigurationQuery](PostConfigurationQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostConfigurationQuery.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object.  ```` ``` # Get the value of the property. propertyValue = postConfigurationQuery_var.objectType ``` ```` |

"postConfigurationQuery\_var" is a variable referencing a PostConfigurationQuery object. ```` ``` #include <Cam/Post/PostConfigurationQuery.h>  // Get the value of the property. string propertyValue = postConfigurationQuery_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |