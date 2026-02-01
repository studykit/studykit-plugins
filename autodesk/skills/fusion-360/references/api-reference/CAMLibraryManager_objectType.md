# CAMLibraryManager.objectType Property

Parent Object: [CAMLibraryManager](CAMLibraryManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibraryManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object.  ```` ``` # Get the value of the property. propertyValue = cAMLibraryManager_var.objectType ``` ```` |

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. ```` ``` #include <Cam/Global/CAMLibraryManager.h>  // Get the value of the property. string propertyValue = cAMLibraryManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |