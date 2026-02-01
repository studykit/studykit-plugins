# ObjectCollection.objectType Property

Parent Object: [ObjectCollection](ObjectCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ObjectCollection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"objectCollection\_var" is a variable referencing an ObjectCollection object.  ```` ``` # Get the value of the property. propertyValue = objectCollection_var.objectType ``` ```` |

"objectCollection\_var" is a variable referencing an ObjectCollection object. ```` ``` #include <Core/Application/ObjectCollection.h>  // Get the value of the property. string propertyValue = objectCollection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |