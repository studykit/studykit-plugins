# ModelStateEvents Object

## Description

The Model State Events Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelStateEvents/ModelStateEvents_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Parent](../ModelStateEvents/ModelStateEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ModelStateEvents/ModelStateEvents_Type.md) | Gets the constant that indicates the type of this object. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivateModelState](../ModelStateEvents/ModelStateEvents_OnActivateModelState.md) | Event that fires when a model state is activated. |
| [OnDeleteModelState](../ModelStateEvents/ModelStateEvents_OnDeleteModelState.md) | Event that fires when a model state is deleted. |
| [OnNewModelState](../ModelStateEvents/ModelStateEvents_OnNewModelState.md) | Event that fires when a model state is created. |

## Accessed From

[Application.ModelStateEvents](../Application/Application_ModelStateEvents.md)

## Version

Introduced in version 2022
