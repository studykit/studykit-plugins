# Camera.ComputeWithMouseInput Method

Parent Object: [Camera](../Camera/Camera.md)

## Description

Method that changes the view according mouse movement and view operation.

## Syntax

Camera.**ComputeWithMouseInput**( ***FromPoint*** As [Point2d](../Point2d/Point2d.md), ***ToPoint*** As [Point2d](../Point2d/Point2d.md), ***WheelDelta*** As Long, ***ViewOperation*** As [ViewOperationTypeEnum](../ViewOperationTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromPoint | [Point2d](../Point2d/Point2d.md) | Input point that specifies the starting point from which to move the view. |
| ToPoint | [Point2d](../Point2d/Point2d.md) | Input point that specifies the destination to which to move the view. |
| WheelDelta | Long | Input Long that specifies the number of clicks (to zoom in or out) that have been made with the center mouse wheel. The WheelDelta is for the middle button wheel on the mouse. We use that for zoom in/out. The WheelDelta should represent the number of clicks that have been made with the wheel. |
| ViewOperation | [ViewOperationTypeEnum](../ViewOperationTypeEnum.md) | Input constant that specifies the type of view operation (pan, rotate, or zoom). |

## Version

Introduced in version 6
