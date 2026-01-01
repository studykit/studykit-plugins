# ArrangePlaneResultEnvelope.envelopeDefinition Property

Parent Object: [ArrangePlaneResultEnvelope](ArrangePlaneResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneResultEnvelope.h>

## Description

Returns the envelope definition that provides the settings for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrangePlaneResultEnvelope_var.envelopeDefinition ``` ```` |

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangePlaneResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeEnvelopeDefinition> propertyValue = arrangePlaneResultEnvelope_var->envelopeDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |