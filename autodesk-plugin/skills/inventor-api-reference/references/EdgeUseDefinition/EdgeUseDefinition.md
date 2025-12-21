# EdgeUseDefinition Object

## Description

The FaceDefinition represents a transient definition of a Face object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeUseDefinition/EdgeUseDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EdgeDefinition](../EdgeUseDefinition/EdgeUseDefinition_EdgeDefinition.md) | Gets and set the associated EdgeDefinition object. |
| [IsOpposedToEdge](../EdgeUseDefinition/EdgeUseDefinition_IsOpposedToEdge.md) | Gets and sets if the orientation of this EdgeUse is in the same direction or not relative to the associated EdgeDefinition object. |
| [Type](../EdgeUseDefinition/EdgeUseDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EdgeUseDefinitions.Add](../EdgeUseDefinitions/EdgeUseDefinitions_Add.md), [EdgeUseDefinitions.Item](../EdgeUseDefinitions/EdgeUseDefinitions_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011
