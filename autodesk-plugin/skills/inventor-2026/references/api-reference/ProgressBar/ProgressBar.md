# ProgressBar Object

## Description

The ProgressBar object represents an Inventor dialog to show the progress of a certain operation or a series of operations.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ProgressBar/ProgressBar_Close.md) | Terminates the progress bar. |
| [UpdateProgress](../ProgressBar/ProgressBar_UpdateProgress.md) | Updates the progress bar by incrementing the progress step by one. This method should be called as many times as the number of steps provided in the CreateProgressBar method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProgressBar/ProgressBar_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Message](../ProgressBar/ProgressBar_Message.md) | Gets and sets the string specifying the message for the progress bar. The string can contain multiple prompt strings (“%s”) the actual values for which are specified in the MessagePrompts property before each call to UpdateProgress. |
| [Type](../ProgressBar/ProgressBar_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnCancel](../ProgressBar/ProgressBar_OnCancel.md) | Event that is fired when the user chooses the cancel button on the progress bar. |

## Accessed From

[Application.CreateProgressBar](../Application/Application_CreateProgressBar.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using Inventor's progress bars](../../sample-programs/ProgressBar_Sample.md) | Demonstrates using Inventor's progress bar. |

## Version

Introduced in version 2010
