# ArrangeResultEnvelope.occurrences Property

Parent Object: [ArrangeResultEnvelope](ArrangeResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeResultEnvelope.h>

## Description

Returns a collection object of the occurrences in this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object. |

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangeResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeOccurrenceResults> propertyValue = arrangeResultEnvelope_var->occurrences(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeOccurrenceResults](ArrangeOccurrenceResults.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |