# Arrange2DPlaneEnvelopeInput.isPartialArrangeAllowed Property

Parent Object: [Arrange2DPlaneEnvelopeInput](Arrange2DPlaneEnvelopeInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>

## Description

Gets and sets if a partial arrange is allowed. If true, it will still create a result when there is not enough space on the envelope to fit all of the components. Components are arranged until all the available space is used up. The components that were not included in the partial arrangement are highlighted in the components list. If the envelope size increases, the arrangement recalculates to include the components that did not previously fit in the arrangement.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object. |

"arrange2DPlaneEnvelopeInput\_var" is a variable referencing an Arrange2DPlaneEnvelopeInput object. ```` ``` #include <Fusion/Arrange/Arrange2DPlaneEnvelopeInput.h>  // Get the value of the property. boolean propertyValue = arrange2DPlaneEnvelopeInput_var->isPartialArrangeAllowed();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrange2DPlaneEnvelopeInput_var->isPartialArrangeAllowed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |