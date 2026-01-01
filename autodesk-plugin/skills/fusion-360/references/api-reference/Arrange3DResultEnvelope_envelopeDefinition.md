# Arrange3DResultEnvelope.envelopeDefinition Property

Parent Object: [Arrange3DResultEnvelope](Arrange3DResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DResultEnvelope.h>

## Description

Returns the envelope definition that provides the settings for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object.  ```` ``` # Get the value of the property. propertyValue = arrange3DResultEnvelope_var.envelopeDefinition ``` ```` |

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. ```` ``` #include <Fusion/Arrange/Arrange3DResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeEnvelopeDefinition> propertyValue = arrange3DResultEnvelope_var->envelopeDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |