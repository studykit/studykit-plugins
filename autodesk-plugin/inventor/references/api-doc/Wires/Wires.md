# Wires Object

## Description

The Wires collection object provides access to a set of Wire objects.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../Wires/Wires_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Wires/Wires_Item.md) | Allows integer-indexed access to items in the collection. |
| [Type](../Wires/Wires_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Path.Wires](../Path/Path_Wires.md), [PathProxy.Wires](../PathProxy/PathProxy_Wires.md), [Profile.Wires](../Profile/Profile_Wires.md), [Profile3D.Wires](../Profile3D/Profile3D_Wires.md), [Profile3DProxy.Wires](../Profile3DProxy/Profile3DProxy_Wires.md), [ProfileProxy.Wires](../ProfileProxy/ProfileProxy_Wires.md), [SurfaceBody.Wires](../SurfaceBody/SurfaceBody_Wires.md), [SurfaceBodyProxy.Wires](../SurfaceBodyProxy/SurfaceBodyProxy_Wires.md), [Wire.OffsetPlanarWire](../Wire/Wire_OffsetPlanarWire.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |