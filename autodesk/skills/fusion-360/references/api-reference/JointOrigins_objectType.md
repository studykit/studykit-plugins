# JointOrigins.objectType Property

Parent Object: [JointOrigins](JointOrigins.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigins.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigins\_var" is a variable referencing a JointOrigins object.  ```` ``` # Get the value of the property. propertyValue = jointOrigins_var.objectType ``` ```` |

"jointOrigins\_var" is a variable referencing a JointOrigins object. ```` ``` #include <Fusion/Components/JointOrigins.h>  // Get the value of the property. string propertyValue = jointOrigins_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |