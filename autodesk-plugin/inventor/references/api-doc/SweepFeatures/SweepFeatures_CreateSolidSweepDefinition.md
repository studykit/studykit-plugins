# SweepFeatures.CreateSolidSweepDefinition Method

Parent Object: [SweepFeatures](../SweepFeatures/SweepFeatures.md)

## Description

Method that creates the SolidSweepDefinition object.

## Syntax

SweepFeatures.**CreateSolidSweepDefinition**( ***ToolBody*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***Path*** As [Path](../Path/Path.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md), ***AffectedBodies*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***KeepToolbody***] As Boolean ) As [SolidSweepDefinition](../SolidSweepDefinition/SolidSweepDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToolBody | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object indicates which surfacebody will be used as tool body to sweep. |
| Path | [Path](../Path/Path.md) | Input entity that defines the path of the sweep. Use the CreatePath or CreateSpecifiedPath methods on the PartFeatures object to create a Path. The path can be a combination of 2D and 3D sketch elements and can be open or closed. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation or kNewBodyOperation. |
| AffectedBodies | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that specifies which surface bodies will be affected. When the Operation is set to kJoinOperation only one surface body should be specified, when the operation is set to kCutOperation or kIntersectOperation more than one surface bodies can be specified, when the operation is set to kNewBodyOperation an empty ObjectCollection should be provided. Anyway the ToolBody should not be provided in this argument. |
| KeepToolbody | Boolean | Optional input Boolean that specifies whether to keep the source tool body or not. This defaults to False if not provided. |

## Version

Introduced in version 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |