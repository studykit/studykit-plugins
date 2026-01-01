# FaceShellDefinition Object

## Description

The FaceShellDefinition represents a transient definition of a FaceShell object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FaceShellDefinition/FaceShellDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FaceDefinitions](../FaceShellDefinition/FaceShellDefinition_FaceDefinitions.md) | Property that returns the collection of FaceDefinition objects associated with this FaceShellDefinition object. |
| [Type](../FaceShellDefinition/FaceShellDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WireDefinitions](../FaceShellDefinition/FaceShellDefinition_WireDefinitions.md) | Gets the collection of WireDefinition objects associated with this SurfaceBodyDefinition object. The primary use of the WireDefinitions collection is to create new WireDefinition objects. |

## Accessed From

[FaceShellDefinitions.Add](../FaceShellDefinitions/FaceShellDefinitions_Add.md), [FaceShellDefinitions.Item](../FaceShellDefinitions/FaceShellDefinitions_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2011
