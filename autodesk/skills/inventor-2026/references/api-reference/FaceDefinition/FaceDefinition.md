# FaceDefinition Object

## Description

The FaceDefinition represents a transient definition of a Face object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FaceDefinition/FaceDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssociativeID](../FaceDefinition/FaceDefinition_AssociativeID.md) | Gets and sets the associate ID of this face. This ID will be transferred to the corresponding face when this SurfaceBodyDefinition is used to create a SurfaceBody. It is used by Inventor as the identifier for the face and is used for tracking this geometry. |
| [EdgeLoopDefinitions](../FaceDefinition/FaceDefinition_EdgeLoopDefinitions.md) | Property that returns the collection of EdgeLoopDefinition objects associated with this FaceDefinition object. |
| [IsParamReversed](../FaceDefinition/FaceDefinition_IsParamReversed.md) | Read write property that indicates if the normal of this face is reversed with respect to the geometry associated with this face definition. |
| [SurfaceGeometry](../FaceDefinition/FaceDefinition_SurfaceGeometry.md) | Gets the collection of EdgeLoopDefinition objects associated with this FaceDefinition object. |
| [Type](../FaceDefinition/FaceDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EdgeDefinition.FaceOne](../EdgeDefinition/EdgeDefinition_FaceOne.md), [EdgeDefinition.FaceTwo](../EdgeDefinition/EdgeDefinition_FaceTwo.md), [FaceDefinitions.Add](../FaceDefinitions/FaceDefinitions_Add.md), [FaceDefinitions.Item](../FaceDefinitions/FaceDefinitions_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011
