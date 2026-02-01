# ArrangeEnvelopeInput.objectType Property

Parent Object: [ArrangeEnvelopeInput](ArrangeEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeEnvelopeInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeEnvelopeInput\_var" is a variable referencing an ArrangeEnvelopeInput object.  ```` ``` # Get the value of the property. propertyValue = arrangeEnvelopeInput_var.objectType ``` ```` |

"arrangeEnvelopeInput\_var" is a variable referencing an ArrangeEnvelopeInput object. ```` ``` #include <Fusion/Arrange/ArrangeEnvelopeInput.h>  // Get the value of the property. string propertyValue = arrangeEnvelopeInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |