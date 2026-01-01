# WebFeature.objectType Property

Parent Object: [WebFeature](WebFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeature\_var" is a variable referencing a WebFeature object.  ```` ``` # Get the value of the property. propertyValue = webFeature_var.objectType ``` ```` |

"webFeature\_var" is a variable referencing a WebFeature object. ```` ``` #include <Fusion/Features/WebFeature.h>  // Get the value of the property. string propertyValue = webFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |