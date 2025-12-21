# PartEvents Object

## Description

The PartEvents object provides notification of part events including changes to surface bodies.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartEvents/PartEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../PartEvents/PartEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../PartEvents/PartEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnSurfaceBodyChanged](../PartEvents/PartEvents_OnSurfaceBodyChanged.md) | The OnSurfaceBodyChanged event notifies the client when the surface and solid geometry of a part geometrically changes. |

## Accessed From

[FlatPattern.PartEvents](../FlatPattern/FlatPattern_PartEvents.md), [PartComponentDefinition.PartEvents](../PartComponentDefinition/PartComponentDefinition_PartEvents.md), [SheetMetalComponentDefinition.PartEvents](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_PartEvents.md)

## Version

Introduced in version 4
