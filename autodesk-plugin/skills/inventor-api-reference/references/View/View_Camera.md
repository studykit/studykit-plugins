# View.Camera Property

Parent Object: [View](../View/View.md)

## Description

Property that returns a Camera object which contains the information that defines the current contents of the view.

## Syntax

View.**Camera**() As [Camera](../Camera/Camera.md)

## Property Value

This is a read only property whose value is a [Camera](../Camera/Camera.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drive the camera](../../sample-programs/DriveCamera_Sample.md) | This sample will fly the camera around the model. To simplify the code, the target is hard coded at the origin and the up vector is the positive Z. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4
