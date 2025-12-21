# UserInputEvents.OnDrag Event

Parent Object: [UserInputEvents](../UserInputEvents/UserInputEvents.md)

## Description

The OnDrag event notifies the client whenever the end-user performs a drag operation in the graphics window. Using this event, the client can override Inventor's standard drag behavior.

## Remarks

The following discusses the principles a client needs to understand in order to take advantage of the full capabilities of this event. The OnDrag event notification is sent whenever the end-user begins to perform a drag operation in the graphics window. When the drag is initiated the DragState argument is equal to kDragStateDragHandlerSelection. The client can determine what object is being dragged by checking the contents of the SelectSet object of the active document. If the client wants to override Inventor's standard drag behavior for the object, they need to set the HandlingCode argument to kEventHandled indicating they will handle the drag. If the HandlingCode is set to kEventNotHandled then Inventor will handle the drag. A handling code of kEventCanceled is not supported and will result in the same thing as kEventNotHandled. If the HandlingCode has been set to kEventHandled then the OnDrag event notification will continue to be sent as the end-user continues the drag operation. The DrageState argument will be equal to kDragStateOnDrag while the end-user continues to drag. When the end-user releases the mouse button to stop the drag operation, the DragState argument will be equal to kDragStateEndDrag. By handling the drag, Inventor expects the client to handle all aspects of the drag. The only thing that Inventor does is change the icon to a drag icon and continues to fire the OnDrag event notification. It is up to the client to provide any dynamic feedback during the drag and to perform whatever the final action of the drag is expected to produce, (typically the repositioning of an entity). Using the ModelPosition and ViewPosition arguments Inventor notifies the client of the current position of the mouse to allow them to create any preview graphics.

## Syntax

UserInputEvents.**OnDrag**( ***DragState*** As [DragStateEnum](../DragStateEnum.md), ***ShiftKeys*** As [ShiftStateEnum](../ShiftStateEnum.md), ***ModelPosition*** As [Point](../Point/Point.md), ***ViewPosition*** As [Point2d](../Point2d/Point2d.md), ***View*** As [View](../View/View.md), ***AdditionalInfo*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***HandlingCode*** As [HandlingCodeEnum](../HandlingCodeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DragState | [DragStateEnum](../DragStateEnum.md) | indicating the current state of the drag operation. When the drag is initially started this value is kDragStateDragHandlerSelection, indicating the selection of an entity to be dragged. During the drag, this value is kDragStateOnDrag. When the mouse button is released to stop the drag operation this value is kDragStateEndDrag. |
| ShiftKeys | [ShiftStateEnum](../ShiftStateEnum.md) | A value indicating what combinations of the Shift, Control, and Alt keys are currently pressed. This allows you to use combinations of these keys to control options for the command implementing the drag. For example, a Control drag might result in copying the entity. |
| ModelPosition | [Point](../Point/Point.md) | The current position of the mouse in model space. |
| ViewPosition | [Point2d](../Point2d/Point2d.md) | The current position of the mouse in view space. The coordinates are pixels where the upper-left corner of the view is (0,0). |
| View | [View](../View/View.md) | The View object the drag is taking place within. |
| AdditionalInfo | [NameValueMap](../NameValueMap/NameValueMap.md) | Input  object that contains additional information about why the context menu is being displayed. No additional information is provided for this event. |
| HandlingCode | [HandlingCodeEnum](../HandlingCodeEnum.md) | Output  that indicates how you are handling the event. Setting this argument to kEventHandled results in turning off Inventor's standard behavior for the drag operation and causing additional OnDrag event notifications to be sent as the end-user continues the drag operation. By responding to these events the client can define their own behavior for the entity being dragged. Setting this to kEventNotHandled will cause Inventor to use its standard drag behavior for the entity being dragged. kEventCanceled is not supported and will result in the same behavior as kEventNotHandled. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |