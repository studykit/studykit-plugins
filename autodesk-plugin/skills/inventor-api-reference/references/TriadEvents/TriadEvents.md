# TriadEvents Object

## Description

Event object that provides Triad (3D Move/Rotate tool) events.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Reposition](../TriadEvents/TriadEvents_Reposition.md) | Repositions the specified triad to the specified object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TriadEvents/TriadEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DegreesOfFreedom](../TriadEvents/TriadEvents_DegreesOfFreedom.md) | Gets/sets the allowed translation and rotation directions. |
| [Enabled](../TriadEvents/TriadEvents_Enabled.md) | Gets/Sets the flag indicating whether the Triad is enabled. |
| [GlobalTransform](../TriadEvents/TriadEvents_GlobalTransform.md) | Gets/Sets the current position of the Triad. |
| [IsInRedefineMode](../TriadEvents/TriadEvents_IsInRedefineMode.md) | Read-only property that indicates whether the triad is currently in redefine mode. |
| [MoveTriadOnly](../TriadEvents/TriadEvents_MoveTriadOnly.md) | Gets/sets a flag indicating whether to move the triad independent of the object that the triad is being used to move. |
| [MoveTriadOnlyEnabled](../TriadEvents/TriadEvents_MoveTriadOnlyEnabled.md) | Gets/sets a flag indicating whether to provide the 'Move Triad Only' option to the end user. |
| [Parent](../TriadEvents/TriadEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Repeat](../TriadEvents/TriadEvents_Repeat.md) | Gets and sets a flag indicating whether the triad should be terminated after one sequence of moves. |
| [Type](../TriadEvents/TriadEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivate](../TriadEvents/TriadEvents_OnActivate.md) | Event that occurs when the triad is activated. |
| [OnEndMove](../TriadEvents/TriadEvents_OnEndMove.md) | Fired when the user ends a mouse drag, after repositioning the triad by aligning or when the user selects another triad segment after entering translation/rotation values in the dialog. |
| [OnEndSequence2](../TriadEvents/TriadEvents_OnEndSequence2.md) | Fires when the user ends a move sequence of the triad. |
| [OnMove](../TriadEvents/TriadEvents_OnMove.md) | Event that occurs when the triad moves as a result of a drag, a reposition or user entering values for translation or rotation. A 'reposition' move is always immediately followed by the OnEndMove event. |
| [OnMoveTriadOnlyToggle2](../TriadEvents/TriadEvents_OnMoveTriadOnlyToggle2.md) | Fires when the 'Move Triad Only' option is toggled. |
| [OnSegmentSelectionChange](../TriadEvents/TriadEvents_OnSegmentSelectionChange.md) | Event that occurs every time a segment of a triad is selected. |
| [OnStartMove](../TriadEvents/TriadEvents_OnStartMove.md) | Event that occurs when the triad begins to move as a result of a drag, a reposition or user entering values for translation or rotation. The event provides information of the state of the triad before the move actually occurs. |
| [OnStartSequence](../TriadEvents/TriadEvents_OnStartSequence.md) | Event that fires indicating the logical start of a sequence of triad moves. |
| [OnTerminate2](../TriadEvents/TriadEvents_OnTerminate2.md) | Fires when the triad is terminated. |

## Accessed From

[InteractionEvents.TriadEvents](../InteractionEvents/InteractionEvents_TriadEvents.md)

## Version

Introduced in version 9
