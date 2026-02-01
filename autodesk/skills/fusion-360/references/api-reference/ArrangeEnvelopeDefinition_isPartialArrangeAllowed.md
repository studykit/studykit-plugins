# ArrangeEnvelopeDefinition.isPartialArrangeAllowed Property

Parent Object: [ArrangeEnvelopeDefinition](ArrangeEnvelopeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeEnvelopeDefinition.h>

## Description

Gets and sets if a partial arrange is allowed for this envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeEnvelopeDefinition\_var" is a variable referencing an ArrangeEnvelopeDefinition object. |

"arrangeEnvelopeDefinition\_var" is a variable referencing an ArrangeEnvelopeDefinition object. ```` ``` #include <Fusion/Arrange/ArrangeEnvelopeDefinition.h>  // Get the value of the property. boolean propertyValue = arrangeEnvelopeDefinition_var->isPartialArrangeAllowed();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeEnvelopeDefinition_var->isPartialArrangeAllowed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |