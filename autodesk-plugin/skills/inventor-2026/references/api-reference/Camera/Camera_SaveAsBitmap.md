# Camera.SaveAsBitmap Method

Parent Object: [Camera](../Camera/Camera.md)

## Description

Method that saves the current camera view to the specified file. The width and height arguments define the aspect ratio and the number of pixels in the output image.

The CreateImage method is similar to this but instead of writing the image to a file it creates it in memory, which is more efficient than writing and reading if from disk if you need to use the image immediately.

## Syntax

Camera.**SaveAsBitmap**( ***FullFileName*** As String, ***Width*** As Long, ***Height*** As Long, [***topColor***] As Variant, [***bottomColor***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | The full filename (path and filename) of the bitmap to create. The type of image file to create is implied based on the extension of the filename. Valid extensions are bmp, jpg, png, tiff, and gif. |
| Width | Long | Specifies the number of horizontal pixels in the output image. |
| Height | Long | Specifies the number of vertical pixels in the output image. |
| topColor | Variant | Optional argument that specifies the background color at the top of the image. If a bottom background color is supplied, then the background will be a gradient between the top and bottom colors. If only a top background color is supplied, the background will be a solid color using this color. If no color is defined a default color will be used. |
| bottomColor | Variant | Optional argument that specified the background color at the bottom of the image. This argument is only valid when the TopBackgroundColor argument has been supplied. This argument defines the color of the background at the bottom of the image and a gradient background is created that varies from the top color to the bottom color.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2012
