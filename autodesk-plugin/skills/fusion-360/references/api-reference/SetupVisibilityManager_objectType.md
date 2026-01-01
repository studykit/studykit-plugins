# SetupVisibilityManager.objectType Property

Parent Object: [SetupVisibilityManager](SetupVisibilityManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Visibility/SetupVisibilityManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupVisibilityManager\_var" is a variable referencing a SetupVisibilityManager object.  ```` ``` # Get the value of the property. propertyValue = setupVisibilityManager_var.objectType ``` ```` |

"setupVisibilityManager\_var" is a variable referencing a SetupVisibilityManager object. ```` ``` #include <Cam/Visibility/SetupVisibilityManager.h>  // Get the value of the property. string propertyValue = setupVisibilityManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |