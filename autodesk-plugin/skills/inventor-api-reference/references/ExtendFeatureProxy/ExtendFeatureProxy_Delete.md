# ExtendFeatureProxy.Delete Method

Parent Object: [ExtendFeatureProxy](../ExtendFeatureProxy/ExtendFeatureProxy.md)

## Description

Method that deletes the feature. The arguments allow control over which dependent objects are also deleted.

## Syntax

ExtendFeatureProxy.**Delete**( [***RetainConsumedSketches***] As Boolean, [***RetainDependentFeaturesAndSketches***] As Boolean, [***RetainDependentWorkFeatures***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RetainConsumedSketches | Boolean | Optional input Boolean indicating if consumed sketches within the feature should be deleted. If the feature being deleted is not a sketch based feature this argument is ignored. |
| RetainDependentFeaturesAndSketches | Boolean | Optional input Boolean that specifies if dependent features should be deleted. If there are no dependent features this argument is ignored.   This is an optional argument whose default value is False. |
| RetainDependentWorkFeatures | Boolean | Optional input Boolean that specifies if dependent work features should be deleted. If there are no dependent work features this argument is ignored.   This is an optional argument whose default value is False. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |