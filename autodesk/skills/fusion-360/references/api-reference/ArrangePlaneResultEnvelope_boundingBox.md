# ArrangePlaneResultEnvelope.boundingBox Property

Parent Object: [ArrangePlaneResultEnvelope](ArrangePlaneResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangePlaneResultEnvelope.h>

## Description

The bounding box of the this result. The coordinates are defined using the coordinate system of the construction plane used to define the envelope.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object. |

"arrangePlaneResultEnvelope\_var" is a variable referencing an ArrangePlaneResultEnvelope object. ```` ``` #include <Fusion/Arrange/ArrangePlaneResultEnvelope.h>  // Get the value of the property. Ptr<BoundingBox2D> propertyValue = arrangePlaneResultEnvelope_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox2D](BoundingBox2D.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |