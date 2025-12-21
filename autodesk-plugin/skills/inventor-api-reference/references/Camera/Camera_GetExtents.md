# Camera.GetExtents Method

Parent Object: [Camera](../Camera/Camera.md)

## Description

Method that gets the current extents of the camera. The camera extents define the area within the model that is visible in the view.

## Syntax

Camera.**GetExtents**( ***Width*** As Double, ***Height*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Double | Output Double that is the current width of the volume of the model shown within the view. For perspective views, the width is determined at the target point. The value is in centimeters. |
| Height | Double | Output Double that is the current height of the volume of the model shown within the view. For perspective views, the height is determined at the target point. The value is in centimeters. |

## Version

Introduced in version 5.3
