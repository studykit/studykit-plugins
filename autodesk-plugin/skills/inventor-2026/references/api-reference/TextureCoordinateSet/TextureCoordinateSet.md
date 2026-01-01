# TextureCoordinateSet Object

## Description

A TextureCoordinateSet defines the coordinates of the map on the face. The TextureMap.Transformation matrix defines how the coordinates map to the actual face coordinates. Several TextureMaps could reference a single TextureCoordinateSet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCoordinates](../TextureCoordinateSet/TextureCoordinateSet_GetCoordinates.md) | Method to obtain the coordinates to this set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TextureCoordinateSet/TextureCoordinateSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../TextureCoordinateSet/TextureCoordinateSet_Count.md) | Property that returns the number of coordinates in this set. |
| [Item](../TextureCoordinateSet/TextureCoordinateSet_Item.md) | Returns the specified coordinates from the set. |
| [Parent](../TextureCoordinateSet/TextureCoordinateSet_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../TextureCoordinateSet/TextureCoordinateSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[TextureMap.GetTextureCoordinateSet](../TextureMap/TextureMap_GetTextureCoordinateSet.md)

## Version

Introduced in version 10
