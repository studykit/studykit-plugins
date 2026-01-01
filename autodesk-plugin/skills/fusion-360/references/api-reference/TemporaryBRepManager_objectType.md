# TemporaryBRepManager.objectType Property

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a TemporaryBRepManager object.  ```` ``` # Get the value of the property. propertyValue = temporaryBRepManager_var.objectType ``` ```` |

"temporaryBRepManager\_var" is a variable referencing a TemporaryBRepManager object. ```` ``` #include <Fusion/BRep/TemporaryBRepManager.h>  // Get the value of the property. string propertyValue = temporaryBRepManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |