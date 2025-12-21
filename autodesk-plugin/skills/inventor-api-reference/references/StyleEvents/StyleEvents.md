# StyleEvents Object

## Description

The StyleEvents object provides notification of style events including new, activated, changed or deleted styles.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../StyleEvents/StyleEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../StyleEvents/StyleEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../StyleEvents/StyleEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivateStyle](../StyleEvents/StyleEvents_OnActivateStyle.md) | Event that is fired whenever a style is activated in a document. |
| [OnDelete](../StyleEvents/StyleEvents_OnDelete.md) | Event that is fired whenever an object within this events set is deleted in a document. |
| [OnNewStyle](../StyleEvents/StyleEvents_OnNewStyle.md) | Event that is fired whenever a new style is created in a document. |
| [OnStyleChange](../StyleEvents/StyleEvents_OnStyleChange.md) | Event that is fired whenever a style changes. |

## Accessed From

[Application.StyleEvents](../Application/Application_StyleEvents.md), [InventorServer.StyleEvents](InventorServer_StyleEvents.md), [InventorServerObject.StyleEvents](InventorServerObject_StyleEvents.md)

## Version

Introduced in version 11
