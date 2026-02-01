# Camera.SetExtents Method

Parent Object: [Camera](../Camera/Camera.md)

## Description

Method that sets the current extents of the camera. The camera extents define the area within the model that is visible in the view. Setting the extents results in the camera zooming in or out. The Apply method of the camera must be called before any changes are shown in the view.

## Syntax

Camera.**SetExtents**( ***Width*** As Double, ***Height*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Double | Input Double that specifies the new width of the volume of the model to display within the view. For perspective views, the width is specified at the target point. The value is in centimeters. |
| Height | Double | Input Double that specifies the new height of the volume of the model to display within the view. For perspective views, the height is specified at the target point. The value is in centimeters. |

## Version

Introduced in version 5.3
