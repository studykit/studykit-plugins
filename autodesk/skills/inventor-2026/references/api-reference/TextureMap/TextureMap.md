# TextureMap Object

## Description

Each TextureMap references a TextureCoordinateSet that defines the coordinates of the map on the face. Several TextureMaps could reference a single TextureCoordinateSet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GenerateImage](../TextureMap/TextureMap_GenerateImage.md) | Generates an image at the specified location. |
| [GetTextureCoordinateSet](../TextureMap/TextureMap_GetTextureCoordinateSet.md) | Gets the TextureCoordinateSet for the input tolerance. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TextureMap/TextureMap_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Image](../TextureMap/TextureMap_Image.md) | Gets the image for the texture map. |
| [MaskColor](../TextureMap/TextureMap_MaskColor.md) | Gets the mask color for the texture map image. |
| [Parent](../TextureMap/TextureMap_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Transformation](../TextureMap/TextureMap_Transformation.md) | A matrix that defines how the coordinates map to the actual face coordinates. |
| [Type](../TextureMap/TextureMap_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseMask](../TextureMap/TextureMap_UseMask.md) | Gets whether the texture map mask is in use. |

## Accessed From

[TextureMaps.Item](../TextureMaps/TextureMaps_Item.md)

## Version

Introduced in version 10
