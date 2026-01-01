# RemoveFeatures.objectType Property

Parent Object: [RemoveFeatures](RemoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeatures\_var" is a variable referencing a RemoveFeatures object.  ```` ``` # Get the value of the property. propertyValue = removeFeatures_var.objectType ``` ```` |

"removeFeatures\_var" is a variable referencing a RemoveFeatures object. ```` ``` #include <Fusion/Features/RemoveFeatures.h>  // Get the value of the property. string propertyValue = removeFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |