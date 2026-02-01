# ArrangeFeature.envelopeDefinition Property

Parent Object: [ArrangeFeature](ArrangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeature.h>

## Description

Returns the envelope definition associated with this arrangement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object.  ```` ``` # Get the value of the property. propertyValue = arrangeFeature_var.envelopeDefinition ``` ```` |

"arrangeFeature\_var" is a variable referencing an ArrangeFeature object. ```` ``` #include <Fusion/Arrange/ArrangeFeature.h>  // Get the value of the property. Ptr<ArrangeEnvelopeDefinition> propertyValue = arrangeFeature_var->envelopeDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |