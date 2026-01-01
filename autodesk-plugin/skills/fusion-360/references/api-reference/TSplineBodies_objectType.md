# TSplineBodies.objectType Property

Parent Object: [TSplineBodies](TSplineBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBodies.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tSplineBodies\_var" is a variable referencing a TSplineBodies object.  ```` ``` # Get the value of the property. propertyValue = tSplineBodies_var.objectType ``` ```` |

"tSplineBodies\_var" is a variable referencing a TSplineBodies object. ```` ``` #include <Fusion/TSpline/TSplineBodies.h>  // Get the value of the property. string propertyValue = tSplineBodies_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |