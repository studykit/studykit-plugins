# ArrangeResultEnvelope.objectType Property

Parent Object: [ArrangeResultEnvelope](ArrangeResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeResultEnvelope.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrangeResultEnvelope_var.objectType ``` ```` |

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangeResultEnvelope.h>  // Get the value of the property. string propertyValue = arrangeResultEnvelope_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |