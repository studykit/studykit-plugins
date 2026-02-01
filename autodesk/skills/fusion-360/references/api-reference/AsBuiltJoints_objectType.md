# AsBuiltJoints.objectType Property

Parent Object: [AsBuiltJoints](AsBuiltJoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoints.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoints\_var" is a variable referencing an AsBuiltJoints object.  ```` ``` # Get the value of the property. propertyValue = asBuiltJoints_var.objectType ``` ```` |

"asBuiltJoints\_var" is a variable referencing an AsBuiltJoints object. ```` ``` #include <Fusion/Components/AsBuiltJoints.h>  // Get the value of the property. string propertyValue = asBuiltJoints_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |