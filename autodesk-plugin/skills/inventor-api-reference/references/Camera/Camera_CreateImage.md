# Camera.CreateImage Method

Parent Object: [Camera](../Camera/Camera.md)

## Description

Creates an image based on the current camera view.

## Remarks

The exported image background color is ignored if the application color set the background to an image, this can be checked using ColorSchemes.BackgroundType.

## Syntax

Camera.**CreateImage**( ***Width*** As Long, ***Height*** As Long, [***topColor***] As Variant, [***bottomColor***] As Variant ) As IPictureDisp

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Long | Specifies the number of horizontal pixels in the output image. |
| Height | Long | Specifies the number of vertical pixels in the output image. |
| topColor | Variant | Optional argument that specifies the background color at the top of the image. If a bottom background color is supplied, then the background will be a gradient between the top and bottom colors. If only a top background color is supplied, the background will be a solid color using this color. If no color is defined a default color will be used. |
| bottomColor | Variant | Optional argument that specified the background color at the bottom of the image. This argument is only valid when the TopBackgroundColor argument has been supplied. This argument defines the color of the background at the bottom of the image and a gradient background is created that varies from the top color to the bottom color.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |