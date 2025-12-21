# CombineFeatures.Add Method

Parent Object: [CombineFeatures](../CombineFeatures/CombineFeatures.md)

## Description

Method that creates a new combine feature. If the combine feature is created successfully, a CombineFeature object corresponding to the newly created combine feature is returned.

## Syntax

CombineFeatures.**Add**( ***BaseBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***ToolBodies*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md), [***KeepToolBodies***] As Boolean ) As [CombineFeature](../CombineFeature/CombineFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BaseBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that represents the blank body. This must be a solid body. |
| ToolBodies | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing one or more SurfaceBody objects that represent the tool bodies. All tool bodies must be solid. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the Boolean operation type for combine. Valid input values are kJoinOperation, kCutOperation and kIntersectOperation. |
| KeepToolBodies | Boolean | Optional input Boolean that specifies whether or not to retain the tool bodies. If not specified, the argument defaults to False and the tool bodies are consumed (i.e. not retained). |

## Version

Introduced in version 2010
