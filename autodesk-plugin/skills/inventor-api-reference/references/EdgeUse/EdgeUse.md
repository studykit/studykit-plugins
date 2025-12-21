# EdgeUse Object

## Description

The EdgeUse object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../EdgeUse/EdgeUse_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeUse/EdgeUse_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CurveType](../EdgeUse/EdgeUse_CurveType.md) | Gets the type of the underlying curve geometry that this EdgeUse is defined by. |
| [Edge](../EdgeUse/EdgeUse_Edge.md) | Gets the that this EdgeUse references. |
| [EdgeLoop](../EdgeUse/EdgeUse_EdgeLoop.md) | Gets the that contains this EdgeUse. |
| [Evaluator](../EdgeUse/EdgeUse_Evaluator.md) | Gets the Curve2dEvaluator for this edge use. |
| [Geometry](../EdgeUse/EdgeUse_Geometry.md) | Property that returns the underlying geometry of the edge use. |
| [GeometryForm](../EdgeUse/EdgeUse_GeometryForm.md) | Gets the form of the underlying geometry as a combination of one or more CurveGeometryFormEnum values. |
| [IsOpposedToEdge](../EdgeUse/EdgeUse_IsOpposedToEdge.md) | Gets whether this EdgeUse is opposed to or aligned with the orientation of the referenced Edge. |
| [IsParamReversed](../EdgeUse/EdgeUse_IsParamReversed.md) | Gets whether the parameterization of the geometry obtained from the Curve property is aligned or opposed to the topological sense of this EdgeUse. |
| [Next](../EdgeUse/EdgeUse_Next.md) | Gets the next in the connected list of EdgeUses in the EdgeLoop. |
| [Parent](../EdgeUse/EdgeUse_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Partner](../EdgeUse/EdgeUse_Partner.md) | In a solid, Face objects are connected to other Face objects by virtue of sharing at least one Edge. The shared Edge is the same object. objects, however ,are unique to a particular face. The Partner property returns the corresponding EdgeUse that belongs to the connected face. |
| [Previous](../EdgeUse/EdgeUse_Previous.md) | Gets the previous . |
| [TransientKey](../EdgeUse/EdgeUse_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../EdgeUse/EdgeUse_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Wire](../EdgeUse/EdgeUse_Wire.md) | Get the Wire containing this EdgeUse. Returns Nothing if this EdgeUse does not belong to a Wire. |

## Accessed From

[EdgeUse.Next](../EdgeUse/EdgeUse_Next.md), [EdgeUse.Partner](../EdgeUse/EdgeUse_Partner.md), [EdgeUse.Previous](../EdgeUse/EdgeUse_Previous.md), [EdgeUseProxy.NativeObject](../EdgeUseProxy/EdgeUseProxy_NativeObject.md), [EdgeUseProxy.Next](../EdgeUseProxy/EdgeUseProxy_Next.md), [EdgeUseProxy.Partner](../EdgeUseProxy/EdgeUseProxy_Partner.md), [EdgeUseProxy.Previous](../EdgeUseProxy/EdgeUseProxy_Previous.md), [EdgeUses.Item](../EdgeUses/EdgeUses_Item.md)

## Derived Classes

[EdgeUseProxy](../EdgeUseProxy/EdgeUseProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |