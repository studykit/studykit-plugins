# Camera.Eye Property

Parent Object: [Camera](../Camera/Camera.md)

## Description

Specifies the position of the observer's 'Eye' (View's center).

## Syntax

Camera.**Eye**() As [Point](../Point/Point.md)

## Property Value

This is a read/write property whose value is a [Point](../Point/Point.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drive the camera](../../sample-programs/DriveCamera_Sample.md) | This sample will fly the camera around the model. To simplify the code, the target is hard coded at the origin and the up vector is the positive Z. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4
