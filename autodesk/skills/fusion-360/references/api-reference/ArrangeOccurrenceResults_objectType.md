# ArrangeOccurrenceResults.objectType Property

Parent Object: [ArrangeOccurrenceResults](ArrangeOccurrenceResults.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeOccurrenceResults.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeOccurrenceResults\_var" is a variable referencing an ArrangeOccurrenceResults object.  ```` ``` # Get the value of the property. propertyValue = arrangeOccurrenceResults_var.objectType ``` ```` |

"arrangeOccurrenceResults\_var" is a variable referencing an ArrangeOccurrenceResults object. ```` ``` #include <Fusion/Arrange/ArrangeOccurrenceResults.h>  // Get the value of the property. string propertyValue = arrangeOccurrenceResults_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |