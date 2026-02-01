# UnstitchFeatures.objectType Property

Parent Object: [UnstitchFeatures](UnstitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeatures\_var" is a variable referencing a UnstitchFeatures object.  ```` ``` # Get the value of the property. propertyValue = unstitchFeatures_var.objectType ``` ```` |

"unstitchFeatures\_var" is a variable referencing a UnstitchFeatures object. ```` ``` #include <Fusion/Features/UnstitchFeatures.h>  // Get the value of the property. string propertyValue = unstitchFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |