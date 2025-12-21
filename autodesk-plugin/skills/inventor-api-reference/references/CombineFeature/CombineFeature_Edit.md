# CombineFeature.Edit Method

Parent Object: [CombineFeature](../CombineFeature/CombineFeature.md)

## Description

Method that edits an existing combine feature.

## Syntax

CombineFeature.**Edit**( ***BaseBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***ToolBodies*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BaseBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that represents the blank body. This must be a solid body. |
| ToolBodies | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing one or more SurfaceBody objects that represent the tool bodies. All tool bodies must be solid. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the Boolean operation type for combine. Valid input values are kJoinOperation, kCutOperation and kIntersectOperation. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |