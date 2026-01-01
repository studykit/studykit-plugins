# ArrangeProfileOrFaceResultEnvelope.envelopeDefinition Property

Parent Object: [ArrangeProfileOrFaceResultEnvelope](ArrangeProfileOrFaceResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeProfileOrFaceResultEnvelope.h>

## Description

Returns the envelope definition that provides the settings for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeProfileOrFaceResultEnvelope\_var" is a variable referencing an ArrangeProfileOrFaceResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrangeProfileOrFaceResultEnvelope_var.envelopeDefinition ``` ```` |

"arrangeProfileOrFaceResultEnvelope\_var" is a variable referencing an ArrangeProfileOrFaceResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangeProfileOrFaceResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeEnvelopeDefinition> propertyValue = arrangeProfileOrFaceResultEnvelope_var->envelopeDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |