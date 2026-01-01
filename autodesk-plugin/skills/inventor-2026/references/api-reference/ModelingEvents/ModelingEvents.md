# ModelingEvents Object

## Description

The ModelingEvents object provides notification of modeling events including new feature, feature delete, changed feature, client feature or new/changed parameters.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelingEvents/ModelingEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../ModelingEvents/ModelingEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ModelingEvents/ModelingEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnClientFeatureDoubleClick](../ModelingEvents/ModelingEvents_OnClientFeatureDoubleClick.md) | Event that fires when the user double-clicks a client feature. |
| [OnDelete](../ModelingEvents/ModelingEvents_OnDelete.md) | The OnDelete event notifies the client when a modeling entity is deleted. |
| [OnFeatureChange](../ModelingEvents/ModelingEvents_OnFeatureChange.md) | Event that is fired whenever a feature changes. |
| [OnGenerateMember](../ModelingEvents/ModelingEvents_OnGenerateMember.md) | Event that fires before and after an iPart or an iAssembly member is being generated or regenerated. |
| [OnGenerateModelStateMember](../ModelingEvents/ModelingEvents_OnGenerateModelStateMember.md) | Event that fires before and after an model state member document is being generated or regenerated. |
| [OnNewFeature](../ModelingEvents/ModelingEvents_OnNewFeature.md) | Event that is fired whenever a feature is created. |
| [OnNewParameter](../ModelingEvents/ModelingEvents_OnNewParameter.md) | The OnNewParameter event notifies the client when a new parameter is created. |
| [OnParameterChange](../ModelingEvents/ModelingEvents_OnParameterChange.md) | The OnParameterChange event notifies the client when a parameter is changed. |

## Accessed From

[Application.ModelingEvents](../Application/Application_ModelingEvents.md), [InventorServer.ModelingEvents](InventorServer_ModelingEvents.md), [InventorServerObject.ModelingEvents](InventorServerObject_ModelingEvents.md)

## Version

Introduced in version 11
