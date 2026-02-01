# SketchImages.Add Method

Parent Object: [SketchImages](../SketchImages/SketchImages.md)

## Description

Method that creates an image based on an input picture file name.

## Remarks

Insert a SketchImange into planar sketches in assembly or drawing sketches under a Sheet or DrawingView is not applicable.

## Syntax

SketchImages.**Add**( ***FullFileName*** As String, ***Position*** As [Point2d](../Point2d/Point2d.md), [***Link***] As Boolean ) As [SketchImage](../SketchImage/SketchImage.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Specifies the full file name of a picture file that contains the image to be inserted. |
| Position | [Point2d](../Point2d/Point2d.md) | Object that specifies the position on the sketch to insert the image at. |
| Link | Boolean | Boolean that specifies whether or not to link the input source file. The default value is True indicating the file will be linked. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |

## Version

Introduced in version 11
