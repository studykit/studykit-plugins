# ThreadFeatures.objectType Property

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a ThreadFeatures object.  ```` ``` # Get the value of the property. propertyValue = threadFeatures_var.objectType ``` ```` |

"threadFeatures\_var" is a variable referencing a ThreadFeatures object. ```` ``` #include <Fusion/Features/ThreadFeatures.h>  // Get the value of the property. string propertyValue = threadFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |