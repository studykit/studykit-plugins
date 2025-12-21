# RepresentationEvents Object

## Description

The RepresentationEvents object provides notification of representation events including creation, activation or deletion of design views or positional representations.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RepresentationEvents/RepresentationEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../RepresentationEvents/RepresentationEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../RepresentationEvents/RepresentationEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivateDesignView](../RepresentationEvents/RepresentationEvents_OnActivateDesignView.md) | Event that is fired whenever a DesignViewRepresentation changes. |
| [OnActivatePositionalRepresentation](../RepresentationEvents/RepresentationEvents_OnActivatePositionalRepresentation.md) | The OnActivatePositionalRepresentation event notifies the client when a positional representation is being activated. |
| [OnDelete](../RepresentationEvents/RepresentationEvents_OnDelete.md) | The OnDelete event notifies the client when any representation related objects are deleted. These include positional representations and design views. |
| [OnNewDesignView](../RepresentationEvents/RepresentationEvents_OnNewDesignView.md) | Event that is fired whenever a DesignViewRepresentation is created. |
| [OnNewPositionalRepresentation](../RepresentationEvents/RepresentationEvents_OnNewPositionalRepresentation.md) | The OnNewPositionalRepresentation event notifies the client when a new positional representation is created. |
| [OnNewSectionView](../RepresentationEvents/RepresentationEvents_OnNewSectionView.md) | Event that is fired whenever an section view is created in part or assembly. |

## Accessed From

[Application.RepresentationEvents](../Application/Application_RepresentationEvents.md), [InventorServer.RepresentationEvents](InventorServer_RepresentationEvents.md), [InventorServerObject.RepresentationEvents](InventorServerObject_RepresentationEvents.md)

## Version

Introduced in version 11
