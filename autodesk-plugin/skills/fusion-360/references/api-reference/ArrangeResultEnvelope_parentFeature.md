# ArrangeResultEnvelope.parentFeature Property

Parent Object: [ArrangeResultEnvelope](ArrangeResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeResultEnvelope.h>

## Description

Returns the ArrangeFeature object this result is for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object. |

"arrangeResultEnvelope\_var" is a variable referencing an ArrangeResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangeResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeFeature> propertyValue = arrangeResultEnvelope_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeFeature](ArrangeFeature.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |