# View.SaveAsBitmapWithOptions Method

Parent Object: [View](../View/View.md)

## Description

Method that saves the view as a bitmap with more options. The width and height arguments define the aspect ratio and the number of pixels in the output image. The Options argument allow you to define more effects for the bitmap.

## Syntax

View.**SaveAsBitmapWithOptions**( ***FullFileName*** As String, ***Width*** As Long, ***Height*** As Long, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that specifies the full filename of the file to which to save the view. The extension of this filename controls the type of file that’s created. Valid extensions are bmp, jpg, png, tiff, and gif. |
| Width | Long | Input Long that specifies the width of the view. A value of 0 will use the current width of the view. |
| Height | Long | Input Long that specifies the height of the view. A value of 0 will use the current height of the view. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies more options to create the bitmap. The valid values for the options are:  | Name | Value Type | Description | | --- | --- | --- | | TransparentBackground | Boolean | Specifies whether the saved bitmap will have transparent background. If not specified this will default to False. | |

## Version

Introduced in version 2019
