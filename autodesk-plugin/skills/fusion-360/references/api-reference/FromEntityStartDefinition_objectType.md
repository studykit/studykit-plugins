# FromEntityStartDefinition.objectType Property

Parent Object: [FromEntityStartDefinition](FromEntityStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FromEntityStartDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object.  ```` ``` # Get the value of the property. propertyValue = fromEntityStartDefinition_var.objectType ``` ```` |

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. ```` ``` #include <Fusion/Features/FromEntityStartDefinition.h>  // Get the value of the property. string propertyValue = fromEntityStartDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |