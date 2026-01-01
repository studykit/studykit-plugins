# Arrange3DResultEnvelope.occurrences Property

Parent Object: [Arrange3DResultEnvelope](Arrange3DResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DResultEnvelope.h>

## Description

Returns a collection object of the occurrences in this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. |

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. ```` ``` #include <Fusion/Arrange/Arrange3DResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeOccurrenceResults> propertyValue = arrange3DResultEnvelope_var->occurrences(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeOccurrenceResults](ArrangeOccurrenceResults.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |