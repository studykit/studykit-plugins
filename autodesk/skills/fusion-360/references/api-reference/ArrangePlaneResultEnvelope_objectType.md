# ArrangePlaneResultEnvelope.objectType Property

Parent Object: [ArrangePlaneResultEnvelope](ArrangePlaneResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneResultEnvelope.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrangePlaneResultEnvelope_var.objectType ``` ```` |

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangePlaneResultEnvelope.h>  // Get the value of the property. string propertyValue = arrangePlaneResultEnvelope_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |