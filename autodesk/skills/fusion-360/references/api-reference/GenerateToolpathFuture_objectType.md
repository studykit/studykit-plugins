# GenerateToolpathFuture.objectType Property

Parent Object: [GenerateToolpathFuture](GenerateToolpathFuture.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/GenerateToolpathFuture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generateToolpathFuture\_var" is a variable referencing a GenerateToolpathFuture object.  ```` ``` # Get the value of the property. propertyValue = generateToolpathFuture_var.objectType ``` ```` |

"generateToolpathFuture\_var" is a variable referencing a GenerateToolpathFuture object. ```` ``` #include <Cam/CAM/GenerateToolpathFuture.h>  // Get the value of the property. string propertyValue = generateToolpathFuture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |