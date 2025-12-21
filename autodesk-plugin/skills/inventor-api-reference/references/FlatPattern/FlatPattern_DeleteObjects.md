# FlatPattern.DeleteObjects Method

Parent Object: [FlatPattern](../FlatPattern/FlatPattern.md)

## Description

Method that deletes a collection of objects that belong to the flat pattern.

## Syntax

FlatPattern.**DeleteObjects**( ***Objects*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***RetainConsumedSketches***] As Boolean, [***RetainDepFeatsAndSketches***] As Boolean, [***RetainDepWorkFeats***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Objects | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Collection of objects to delete from the part. Valid objects are part features, work features, sketches and 3d sketches. |
| RetainConsumedSketches | Boolean | Optional input Boolean indicating if consumed sketches within the feature should be deleted. If the feature being deleted is not a sketch based feature this argument is ignored. |
| RetainDepFeatsAndSketches | Boolean | Optional input Boolean that specifies if dependent features and sketches should be deleted. If there are no such dependents this argument is ignored.     This is an optional argument whose default value is False. |
| RetainDepWorkFeats | Boolean | Optional input Boolean that specifies if dependent work features should be deleted. If there are no dependent work features this argument is ignored.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |