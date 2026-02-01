# Arrange3DResultEnvelope.parentFeature Property

Parent Object: [Arrange3DResultEnvelope](Arrange3DResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DResultEnvelope.h>

## Description

Returns the ArrangeFeature object this result is for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. |

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. ```` ``` #include <Fusion/Arrange/Arrange3DResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeFeature> propertyValue = arrange3DResultEnvelope_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeFeature](ArrangeFeature.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |