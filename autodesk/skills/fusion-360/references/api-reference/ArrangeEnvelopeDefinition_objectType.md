# ArrangeEnvelopeDefinition.objectType Property

Parent Object: [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeEnvelopeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeEnvelopeDefinition\_var" is a variable referencing an ArrangeEnvelopeDefinition object.  ```` ``` # Get the value of the property. propertyValue = arrangeEnvelopeDefinition_var.objectType ``` ```` |

"arrangeEnvelopeDefinition\_var" is a variable referencing an ArrangeEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangeEnvelopeDefinition.h>  // Get the value of the property. string propertyValue = arrangeEnvelopeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |