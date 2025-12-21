# DSResult Object

## Description

The DSResult object represents a specific result from a degree of freedom.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCurrentResultValue](../DSResult/DSResult_GetCurrentResultValue.md) | Returns the value of the current result. |
| [GetResultValues](../DSResult/DSResult_GetResultValues.md) | Returns an array representing the values for this result. The array consists of time-value pairs. The unit type of the value will vary depending on the type of value this result represents. For example, getting the extent length will be a distance and is always expressed in the database length unit of centimeters. Results are available when the entire simulation has been computed (LastComputedTimeStep equals NumberOfTimeSteps). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DSResult/DSResult_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Name](../DSResult/DSResult_Name.md) | Gets the name of this result as it is displayed in the Output Grapher dialog. |
| [Parent](../DSResult/DSResult_Parent.md) | Gets the parent degree of freedom that this results object is associated with. |
| [ResultType](../DSResult/DSResult_ResultType.md) | Gets the type of result this DSResult object represents. |
| [Type](../DSResult/DSResult_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DSResults.Item](../DSResults/DSResults_Item.md), [DSResults.ItemByResultType](../DSResults/DSResults_ItemByResultType.md)

## Version

Introduced in version 2013
