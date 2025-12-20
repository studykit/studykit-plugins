# DriveConstraintSettings Object

## Description

.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetIncrement](../DriveConstraintSettings/DriveConstraintSettings_GetIncrement.md) | Returns how the increment was specified and the value. |
| [GoToEnd](../DriveConstraintSettings/DriveConstraintSettings_GoToEnd.md) | Advances the constraint to the end value. |
| [GoToStart](../DriveConstraintSettings/DriveConstraintSettings_GoToStart.md) | Returns the constraint to the start value. |
| [PlayForward](../DriveConstraintSettings/DriveConstraintSettings_PlayForward.md) | Drives the constraint forward. |
| [PlayReverse](../DriveConstraintSettings/DriveConstraintSettings_PlayReverse.md) | Drives the constraint in reverse. |
| [SetIncrement](../DriveConstraintSettings/DriveConstraintSettings_SetIncrement.md) | Sets the increment type and the value. |
| [StartAVIRecording](../DriveConstraintSettings/DriveConstraintSettings_StartAVIRecording.md) | Starts recording the drive constraint animation for saving to an avi file. |
| [StartWMVRecording](../DriveConstraintSettings/DriveConstraintSettings_StartWMVRecording.md) | Starts recording the drive constraint animation for saving to a wmv file. |
| [StepForward](../DriveConstraintSettings/DriveConstraintSettings_StepForward.md) | Advances the constraint by one step. |
| [StepReverse](../DriveConstraintSettings/DriveConstraintSettings_StepReverse.md) | Reverses the constraint by one step. |
| [StopRecording](../DriveConstraintSettings/DriveConstraintSettings_StopRecording.md) | Stops recording the drive constraint animation and generates the animation file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DriveConstraintSettings/DriveConstraintSettings_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CollisionDetection](../DriveConstraintSettings/DriveConstraintSettings_CollisionDetection.md) | Gets and sets whether to drive the constrained assembly until a collision is detected. |
| [DriveAdaptivity](../DriveConstraintSettings/DriveConstraintSettings_DriveAdaptivity.md) | Gets and sets whether to adapt components while maintaining constraint relationships. |
| [EndValue](../DriveConstraintSettings/DriveConstraintSettings_EndValue.md) | Gets and sets the expression for the end value. |
| [FrameRate](../DriveConstraintSettings/DriveConstraintSettings_FrameRate.md) | Gets and sets the increments at which a "snapshot" is taken for inclusion as a frame in a recorded animation. |
| [IsInitialized](../DriveConstraintSettings/DriveConstraintSettings_IsInitialized.md) | Returns whether the drive constraint parameters have been set for this constraint. |
| [Parent](../DriveConstraintSettings/DriveConstraintSettings_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PauseDelay](../DriveConstraintSettings/DriveConstraintSettings_PauseDelay.md) | Gets and sets the delay between steps in seconds. |
| [RepetitionCount](../DriveConstraintSettings/DriveConstraintSettings_RepetitionCount.md) | Gets and sets the number of repetitions for the Start/End sequence and the number of cycles for the Start/End/Start sequence. |
| [RepetitionStartEndStart](../DriveConstraintSettings/DriveConstraintSettings_RepetitionStartEndStart.md) | Gets and sets whether to drive the constraint from the start value to the end value and then in reverse to the start value. |
| [StartValue](../DriveConstraintSettings/DriveConstraintSettings_StartValue.md) | Gets and sets the expression for the start value. |
| [Type](../DriveConstraintSettings/DriveConstraintSettings_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnCollision](../DriveConstraintSettings/DriveConstraintSettings_OnCollision.md) | Event that is fired whenever a collision occurs during the animation/play of the constraint. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |