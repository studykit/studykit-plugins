# Arrange3DResultEnvelope.boundingBox Property

Parent Object: [Arrange3DResultEnvelope](Arrange3DResultEnvelope.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/Arrange3DResultEnvelope.h>

## Description

The bounding box of this result. The coordinates are defined with respect to the root component base coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. |

"arrange3DResultEnvelope\_var" is a variable referencing an Arrange3DResultEnvelope object. ```` ``` #include <Fusion/Arrange/Arrange3DResultEnvelope.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = arrange3DResultEnvelope_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |