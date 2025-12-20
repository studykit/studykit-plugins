# Wire.OffsetPlanarWire Method

Parent Object: [Wire](../Wire/Wire.md)

## Description

Method that computes the offset for a planar wire. A SurfaceBody containing the resulting Wire object(s) is returned. It’s possible that the offset result of a single wire can result in multiple wires.

## Syntax

Wire.**OffsetPlanarWire**( ***Normal*** As [UnitVector](../UnitVector/UnitVector.md), ***Distance*** As Double, ***CornerClosureType*** As [OffsetCornerClosureTypeEnum](../OffsetCornerClosureTypeEnum.md) ) As [Wires](../Wires/Wires.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Normal | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that defines the normal of the wire. This vector must be normal to the plane of the wire and is used to specify the positive side of the plane. This is used to determine the side to offset the curves to. A positive offset distance is in the direction of the cross product (wire\_tangent x wire\_plane\_normal). A negative offset is in the opposite direction. |
| Distance | Double | Input double in centimeters that specifies the offset distance of the new wire. See the description for the Normal argument to see how a positive or negative value for the distance specifies the direction of the offset. |
| CornerClosureType | [OffsetCornerClosureTypeEnum](../OffsetCornerClosureTypeEnum.md) | Input enum value that defines how to close the external corners of the offset. The valid values are listed below:  kCircularCornerClosure - Circular arcs are attached tangentially to the offset edges so that gaps are replaced by rounded corners. In the picture below, the original curves are black, the offset curves are green and the circular rounded corner is red. ![](../images/kCircularCornerClosure.png) kLinearCornerClosure - Linear extensions are attached tangentially to offset edges where there is a gap. The gap is closed where the extensions intersect, giving a sharp corner. In the picture below, the original curves are black, the offset curves are green and the linear extended corner is red. ![](../images/kLinearCornerClosure.png) kExtendCornerClosure - Offset edges are extended smoothly where there is a gap, with the extension depending on the curve type. The gap is closed where the extensions intersect, giving a sharp corner. This method may fall back to using linear extensions or circular arcs if there is a problem. ![](../images/kExtendCornerClosure.png) |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |