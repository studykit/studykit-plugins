# EdgeLoop Object

## Description

The EdgeLoop object. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../EdgeLoop/EdgeLoop_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeLoop/EdgeLoop_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EdgeLoop/EdgeLoop_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Edges](../EdgeLoop/EdgeLoop_Edges.md) | Gets the referenced by this EdgeLoop. |
| [EdgeUses](../EdgeLoop/EdgeLoop_EdgeUses.md) | Gets the referenced by this EdgeLoop. |
| [Face](../EdgeLoop/EdgeLoop_Face.md) | Gets the containing this EdgeLoop. |
| [IsOuterEdgeLoop](../EdgeLoop/EdgeLoop_IsOuterEdgeLoop.md) | Gets whether this EdgeLoop is an external loop, or a loop that encloses material as opposed to a void. |
| [Parent](../EdgeLoop/EdgeLoop_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [RangeBox](../EdgeLoop/EdgeLoop_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [TransientKey](../EdgeLoop/EdgeLoop_TransientKey.md) | Property that obtains an ID key that can be used to bind back to the live object. This transient key is only valid as long as the document state has not changed. For more information, see the ReferenceKeys overview. |
| [Type](../EdgeLoop/EdgeLoop_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EdgeLoopProxy.NativeObject](../EdgeLoopProxy/EdgeLoopProxy_NativeObject.md), [EdgeLoops.Item](../EdgeLoops/EdgeLoops_Item.md), [EdgeUse.EdgeLoop](../EdgeUse/EdgeUse_EdgeLoop.md), [EdgeUseProxy.EdgeLoop](../EdgeUseProxy/EdgeUseProxy_EdgeLoop.md)

## Derived Classes

[EdgeLoopProxy](../EdgeLoopProxy/EdgeLoopProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4
