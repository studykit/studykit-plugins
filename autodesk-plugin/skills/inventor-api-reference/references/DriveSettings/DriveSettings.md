# DriveSettings Object

## Description

The DriveSettings object provides access to various drive relationship related settings for assembly constraints and joints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetIncrement](../DriveSettings/DriveSettings_GetIncrement.md) | Method that returns how the increment was specified and the value. |
| [GoToEnd](../DriveSettings/DriveSettings_GoToEnd.md) | Method that got to the ending frame of the animation. |
| [GoToStart](../DriveSettings/DriveSettings_GoToStart.md) | Method that got to the starting frame of the animation. |
| [PlayForward](../DriveSettings/DriveSettings_PlayForward.md) | Method that drives the relationship forward. This will fail if start and end values are not set. |
| [PlayReverse](../DriveSettings/DriveSettings_PlayReverse.md) | Read-write property that gets and sets the delay between steps in seconds. |
| [SetIncrement](../DriveSettings/DriveSettings_SetIncrement.md) | Method that sets the increment type and the value. |
| [StartAVIRecording](../DriveSettings/DriveSettings_StartAVIRecording.md) | Method that starts recording the drive relationship animation for saving to an avi file. Use the StopRecording method to stop recording and generate the animation file. |
| [StartWMVRecording](../DriveSettings/DriveSettings_StartWMVRecording.md) | Method that starts recording the drive relationship animation for saving to a wmv file. Use the StopRecording method to stop recording and generate the animation file. |
| [StepForward](../DriveSettings/DriveSettings_StepForward.md) | Method that advances the animation by one step. |
| [StepReverse](../DriveSettings/DriveSettings_StepReverse.md) | Method that reverses the animation by one step. |
| [StopRecording](../DriveSettings/DriveSettings_StopRecording.md) | Method that stops recording the drive relationship animation and generates the animation file. Use the StartWMVRecording or StartAVIRecording method to start recording the animation. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DriveSettings/DriveSettings_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CollisionDetection](../DriveSettings/DriveSettings_CollisionDetection.md) | Read-write property that gets and sets whether to drive the constrained assembly until a collision is detected. |
| [DriveAdaptivity](../DriveSettings/DriveSettings_DriveAdaptivity.md) | Read-write property that gets and sets whether to adapt components while maintaining constraint or connection relationships. |
| [DriveType](../DriveSettings/DriveSettings_DriveType.md) | Read-write property that gets and sets the drive type to specify which value to drive. |
| [EndValue](../DriveSettings/DriveSettings_EndValue.md) | Read-write property that gets and sets the expression for the end value. |
| [FrameRate](../DriveSettings/DriveSettings_FrameRate.md) | Read-write property that gets and sets the increments at which a snapshot is taken for inclusion as a frame in a recorded animation. |
| [IsInitialized](../DriveSettings/DriveSettings_IsInitialized.md) | Read-only property that returns whether the drive parameters have been set for this relationship. If this property returns False, the properties on this object will return hard-coded default values and the methods will fail. Calling properties and methods to set drive parameters will automatically toggle this property to True. |
| [Parent](../DriveSettings/DriveSettings_Parent.md) | Read-only property that returns the parent assembly constraint or joint object. |
| [PauseDelay](../DriveSettings/DriveSettings_PauseDelay.md) | Read-write property that gets and sets the delay between steps in seconds. |
| [RepetitionCount](../DriveSettings/DriveSettings_RepetitionCount.md) | Read-write property that gets and sets the number of repetitions for the Start/End sequence and the number of cycles for the Start/End/Start sequence. |
| [RepetitionStartEndStart](../DriveSettings/DriveSettings_RepetitionStartEndStart.md) | Read-write property that gets and sets whether to drive the relationship from the start value to the end value and then in reverse to the start value. |
| [StartValue](../DriveSettings/DriveSettings_StartValue.md) | Read-write property that gets and sets the expression for the start value. |
| [Type](../DriveSettings/DriveSettings_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnCollision](../DriveSettings/DriveSettings_OnCollision.md) | Event that is fired whenever a collision occurs during the animation/play of the relationship. The event only fires if the CollisionDetection property is set to True. |

## Accessed From

[AngleConstraint.DriveSettings](../AngleConstraint/AngleConstraint_DriveSettings.md), [AngleConstraintProxy.DriveSettings](../AngleConstraintProxy/AngleConstraintProxy_DriveSettings.md), [AssemblyConstraint.DriveSettings](../AssemblyConstraint/AssemblyConstraint_DriveSettings.md), [AssemblyJoint.DriveSettings](../AssemblyJoint/AssemblyJoint_DriveSettings.md), [AssemblyJointProxy.DriveSettings](../AssemblyJointProxy/AssemblyJointProxy_DriveSettings.md), [AssemblySymmetryConstraint.DriveSettings](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_DriveSettings.md), [AssemblySymmetryConstraintProxy.DriveSettings](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_DriveSettings.md), [CustomConstraint.DriveSettings](CustomConstraint_DriveSettings.md), [CustomConstraintProxy.DriveSettings](CustomConstraintProxy_DriveSettings.md), [FlushConstraint.DriveSettings](../FlushConstraint/FlushConstraint_DriveSettings.md), [FlushConstraintProxy.DriveSettings](../FlushConstraintProxy/FlushConstraintProxy_DriveSettings.md), [InsertConstraint.DriveSettings](../InsertConstraint/InsertConstraint_DriveSettings.md), [InsertConstraintProxy.DriveSettings](../InsertConstraintProxy/InsertConstraintProxy_DriveSettings.md), [MateConstraint.DriveSettings](../MateConstraint/MateConstraint_DriveSettings.md), [MateConstraintProxy.DriveSettings](../MateConstraintProxy/MateConstraintProxy_DriveSettings.md), [RotateRotateConstraint.DriveSettings](../RotateRotateConstraint/RotateRotateConstraint_DriveSettings.md), [RotateRotateConstraintProxy.DriveSettings](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_DriveSettings.md), [RotateTranslateConstraint.DriveSettings](../RotateTranslateConstraint/RotateTranslateConstraint_DriveSettings.md), [RotateTranslateConstraintProxy.DriveSettings](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_DriveSettings.md), [TangentConstraint.DriveSettings](../TangentConstraint/TangentConstraint_DriveSettings.md), [TangentConstraintProxy.DriveSettings](../TangentConstraintProxy/TangentConstraintProxy_DriveSettings.md), [TransitionalConstraint.DriveSettings](../TransitionalConstraint/TransitionalConstraint_DriveSettings.md), [TransitionalConstraintProxy.DriveSettings](../TransitionalConstraintProxy/TransitionalConstraintProxy_DriveSettings.md), [TranslateTranslateConstraint.DriveSettings](../TranslateTranslateConstraint/TranslateTranslateConstraint_DriveSettings.md), [TranslateTranslateConstraintProxy.DriveSettings](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_DriveSettings.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create rotational assembly joint](../../sample-programs/AssemblyRotationalJoint_Sample.md) | This sample demonstrates creating an assembly joint. It connects the midpoints of the edges of two faces using a rotational joint. To do this it first creates a geometry intent object of the midpoint of the edge and then creates another intent using the face and the midpoint intent. It does this to create to midpoint intents which it then uses to create the rotational connection.  The sample uses and existing part that must be set up to allow it to work correctly. To create the sample part you can use any part that has a planar face and a linear edge connected to that planar face. A simple box is sufficient. In this part Add a mate iMate to the planar face and rename the iMate to "Face1". Also add a mate iMate to a linear edge that is on the face previously named and rename this iMate to "Edge1". Save the part to "C:\Temp\SamplePart.ipt" or any other name and edit the code below to reference the file. You can then run the sample code which will create a new assembly, insert two instances of the part and create a rotational connection between them. Then it will animation the rotation by driving the connection. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |