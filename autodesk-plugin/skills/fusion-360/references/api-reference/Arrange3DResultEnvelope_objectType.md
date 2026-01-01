# Arrange3DResultEnvelope.objectType Property

Parent Object: [Arrange3DResultEnvelope](Arrange3DResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DResultEnvelope.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrange3DResultEnvelope_var.objectType ``` ```` |

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. ```` ``` #include <Fusion/Arrange/Arrange3DResultEnvelope.h>  // Get the value of the property. string propertyValue = arrange3DResultEnvelope_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |