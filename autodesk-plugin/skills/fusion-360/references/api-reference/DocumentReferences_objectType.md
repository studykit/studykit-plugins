# DocumentReferences.objectType Property

Parent Object: [DocumentReferences](DocumentReferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReferences\_var" is a variable referencing a DocumentReferences object.  ```` ``` # Get the value of the property. propertyValue = documentReferences_var.objectType ``` ```` |

"documentReferences\_var" is a variable referencing a DocumentReferences object. ```` ``` #include <Core/Application/DocumentReferences.h>  // Get the value of the property. string propertyValue = documentReferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |