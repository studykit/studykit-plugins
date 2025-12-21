# WireDefinition Object

## Description

WireDefinition Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WireDefinition/WireDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Type](../WireDefinition/WireDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WireEdgeDefinitions](../WireDefinition/WireDefinition_WireEdgeDefinitions.md) | Gets the collection of EdgeDefinition objects associated with this WireDefinition object. |

## Accessed From

[WireDefinitions.Add](../WireDefinitions/WireDefinitions_Add.md), [WireDefinitions.Item](../WireDefinitions/WireDefinitions_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |