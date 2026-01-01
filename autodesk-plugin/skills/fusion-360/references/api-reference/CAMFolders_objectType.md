# CAMFolders.objectType Property

Parent Object: [CAMFolders](CAMFolders.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolders.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolders\_var" is a variable referencing a CAMFolders object.  ```` ``` # Get the value of the property. propertyValue = cAMFolders_var.objectType ``` ```` |

"cAMFolders\_var" is a variable referencing a CAMFolders object. ```` ``` #include <Cam/CAM/CAMFolders.h>  // Get the value of the property. string propertyValue = cAMFolders_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |