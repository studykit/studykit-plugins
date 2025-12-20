# Camera.CreateImageWithOptions Method

Parent Object: [Camera](../Camera/Camera.md)

## Description

Creates an image based on the current camera view with options.

## Remarks

The exported image background color is ignored if the application color set the background to an image, this can be checked using ColorSchemes.BackgroundType.

## Syntax

Camera.**CreateImageWithOptions**( ***Width*** As Long, ***Height*** As Long, ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As IPictureDisp

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Long | Specifies the number of horizontal pixels in the output image. |
| Height | Long | Specifies the number of vertical pixels in the output image. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Optional input NameValueMap that specifies more options to create the image. The valid values for the options are:  | Name | Value Type | Description | | --- | --- | --- | | TopBackgroundColor | Color | Specifies the background color at the top of the image. If a bottom background color is supplied, then the background will be a gradient between the top and bottom colors. If only a top background color is supplied, the background will be a solid color using this color. If no color is defined a default color will be used. | | BottomBackgroundColor | Color | Specified the background color at the bottom of the image. This argument is only valid when the TopBackgroundColor argument has been supplied. This argument defines the color of the background at the bottom of the image and a gradient background is created that varies from the top color to the bottom color. | | AntiAliasing | Boolean | Specifies whether apply the anti-aliasing effect for the image. If not specified this will default to False. | | IncludeEdits | Boolean | Specifies whether the saved image will include the edits to current camera even the edits are not applied yet. If not specified this will default to False. | |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |