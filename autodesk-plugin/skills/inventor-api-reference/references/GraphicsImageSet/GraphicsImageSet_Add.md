# GraphicsImageSet.Add Method

Parent Object: [GraphicsImageSet](../GraphicsImageSet/GraphicsImageSet.md)

## Description

Method that adds a new custom point to the set.

## Syntax

GraphicsImageSet.**Add**( ***Index*** As Long, ***Image*** As IPictureDisp, [***TransparentColor***] As Variant, [***HotPointX***] As Long, [***HotPointY***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long that specifies the position you want this image to have within the set. All images above the specified index will be shifted up to make room for this image. Specifying any number greater than the current count of the set will cause the new image to become the last in the set. |
| Image | IPictureDisp | Input picture to use for the image. This should be the size that you want the point to appear on the screen. |
| TransparentColor | Variant | Optional input Color object that defines the transparent color within the image. If this argument is not supplied and the image provided doesn't define a transparent color, then there won't be any transparency. |
| HotPointX | Long | Optional input Integer that defines the x coordinate of the hot spot as defined in pixels of the image where 0,0 is the top-left corner of the image. The default value of -1 will result in the center of the image being used.   This is an optional argument whose default value is -1. |
| HotPointY | Long | Optional input Integer that defines the x coordinate of the hot spot as defined in pixels of the image where 0,0 is the top-left corner of the image. The default value of -1 will result in the center of the image being used.   This is an optional argument whose default value is -1. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |

## Version

Introduced in version 2011
