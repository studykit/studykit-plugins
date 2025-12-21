# EdgeLoopDefinition Object

## Description

The FaceDefinition represents a transient definition of a Face object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeLoopDefinition/EdgeLoopDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EdgeUseDefinitions](../EdgeLoopDefinition/EdgeLoopDefinition_EdgeUseDefinitions.md) | Property that returns the collection of EdgeUseDefinition objects associated with this EdgeLoopDefinition object. |
| [Type](../EdgeLoopDefinition/EdgeLoopDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EdgeLoopDefinitions.Add](../EdgeLoopDefinitions/EdgeLoopDefinitions_Add.md), [EdgeLoopDefinitions.Item](../EdgeLoopDefinitions/EdgeLoopDefinitions_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011
