# Wire Object

## Description

A Wire object represents a set of 3D curves. They are used in several different areas within the Inventor API. The bend and fold lines on the 3D flattened model of a sheet metal part are returned as a Wire object. It is also used to define 3D curves that are used as input when using some of the functions to create transient B-Rep bodies.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [OffsetPlanarWire](../Wire/Wire_OffsetPlanarWire.md) | Method that computes the offset for a planar wire. A SurfaceBody containing the resulting Wire object(s) is returned. It’s possible that the offset result of a single wire can result in multiple wires. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Wire/Wire_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Edges](../Wire/Wire_Edges.md) | Gets the  referenced by this Wire. |
| [EdgeUses](../Wire/Wire_EdgeUses.md) | Property that returns the EdgeUses collection object associated with this Wire. |
| [IsPlanar](../Wire/Wire_IsPlanar.md) | Read-only property that indicates if this wire is planar or not. |
| [Parent](../Wire/Wire_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../Wire/Wire_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Edge.Wire](../Edge/Edge_Wire.md), [EdgeProxy.Wire](../EdgeProxy/EdgeProxy_Wire.md), [EdgeUse.Wire](../EdgeUse/EdgeUse_Wire.md), [EdgeUseProxy.Wire](../EdgeUseProxy/EdgeUseProxy_Wire.md), [Wires.Item](../Wires/Wires_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 2008
