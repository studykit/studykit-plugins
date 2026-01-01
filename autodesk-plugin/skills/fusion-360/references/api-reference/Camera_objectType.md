# Camera.objectType Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object.  ```` ``` # Get the value of the property. propertyValue = camera_var.objectType ``` ```` |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. string propertyValue = camera_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |