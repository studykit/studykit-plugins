# ArrangePlaneResultEnvelope.parentFeature Property

Parent Object: [ArrangePlaneResultEnvelope](ArrangePlaneResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneResultEnvelope.h>

## Description

Returns the ArrangeFeature object this result is for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object. |

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangePlaneResultEnvelope.h>  // Get the value of the property. Ptr<ArrangeFeature> propertyValue = arrangePlaneResultEnvelope_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is an [ArrangeFeature](ArrangeFeature.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |