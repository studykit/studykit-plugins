# ArrangeResultEnvelope.envelopeDefinition Property

Parent Object: [ArrangeResultEnvelope](ArrangeResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeResultEnvelope.h>

## Description

Returns the envelope definition that provides the settings for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrangeResultEnvelope_var.envelopeDefinition ``` ```` |

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangeResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeEnvelopeDefinition> propertyValue = arrangeResultEnvelope_var->envelopeDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |