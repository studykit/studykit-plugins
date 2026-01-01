# ArrangeOccurrenceResult.objectType Property

Parent Object: [ArrangeOccurrenceResult](ArrangeOccurrenceResult.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeOccurrenceResult.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeOccurrenceResult\_var" is a variable referencing an ArrangeOccurrenceResult object.  ```` ``` # Get the value of the property. propertyValue = arrangeOccurrenceResult_var.objectType ``` ```` |

"arrangeOccurrenceResult\_var" is a variable referencing an ArrangeOccurrenceResult object. ```` ``` #include <Fusion/Arrange/ArrangeOccurrenceResult.h>  // Get the value of the property. string propertyValue = arrangeOccurrenceResult_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |