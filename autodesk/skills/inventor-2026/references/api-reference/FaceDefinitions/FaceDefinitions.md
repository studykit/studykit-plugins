# FaceDefinitions Object

## Description

The FaceDefinitions collection provides access to exisitng FaceDefinition objects and allows creation of new FaceDefinition objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FaceDefinitions/FaceDefinitions_Add.md) | Method that creates a new FaceDefinition within the associated SurfaceBodyDefinition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FaceDefinitions/FaceDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../FaceDefinitions/FaceDefinitions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../FaceDefinitions/FaceDefinitions_Item.md) | Property that returns an item from the collection. The index of the first item in the collection is 1. |
| [Type](../FaceDefinitions/FaceDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FaceShellDefinition.FaceDefinitions](../FaceShellDefinition/FaceShellDefinition_FaceDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |

## Version

Introduced in version 2011
