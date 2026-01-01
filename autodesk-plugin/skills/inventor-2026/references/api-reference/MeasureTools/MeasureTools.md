# MeasureTools Object

## Description

The MeasureTools object provides methods for various measurement related utilities.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetAngle](../MeasureTools/MeasureTools_GetAngle.md) | Method that returns the angle between the input entities. The input entities must all belong to the same document, unless they are transient objects. |
| [GetAnglePrecision](../MeasureTools/MeasureTools_GetAnglePrecision.md) | Get angle precision. |
| [GetLengthPrecision](../MeasureTools/MeasureTools_GetLengthPrecision.md) | Get length precision. |
| [GetLoopLength](../MeasureTools/MeasureTools_GetLoopLength.md) | Method that returns the total length of a loop. |
| [GetMinimumDistance](../MeasureTools/MeasureTools_GetMinimumDistance.md) | Method that returns the minimum distance between the two input entities and also returns the closest points associated with both entities (not necessarily on the entity). |
| [SetAnglePrecision](../MeasureTools/MeasureTools_SetAnglePrecision.md) | Set angle precision. |
| [SetLengthPrecision](../MeasureTools/MeasureTools_SetLengthPrecision.md) | Set length precision. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MeasureTools/MeasureTools_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../MeasureTools/MeasureTools_Parent.md) | Property that returns the parent object. It can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServerComponent' when running with the Apprentice Server. |
| [Type](../MeasureTools/MeasureTools_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.MeasureTools](../Application/Application_MeasureTools.md), [InventorServer.MeasureTools](InventorServer_MeasureTools.md), [InventorServerObject.MeasureTools](InventorServerObject_MeasureTools.md)

## Version

Introduced in version 11
