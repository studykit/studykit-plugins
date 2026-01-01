# WebFeatures.objectType Property

Parent Object: [WebFeatures](WebFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeatures\_var" is a variable referencing a WebFeatures object.  ```` ``` # Get the value of the property. propertyValue = webFeatures_var.objectType ``` ```` |

"webFeatures\_var" is a variable referencing a WebFeatures object. ```` ``` #include <Fusion/Features/WebFeatures.h>  // Get the value of the property. string propertyValue = webFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |