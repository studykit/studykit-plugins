# SweepFeatures.CreateSweepDefinition Method

Parent Object: [SweepFeatures](../SweepFeatures/SweepFeatures.md)

## Description

Method that creates the SweepDefinition object.

## Syntax

SweepFeatures.**CreateSweepDefinition**( ***SweepType*** As [SweepTypeEnum](../SweepTypeEnum.md), ***Profile*** As [Profile](../Profile/Profile.md), ***Path*** As [Path](../Path/Path.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) ) As [SweepDefinition](../SweepDefinition/SweepDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SweepType | [SweepTypeEnum](../SweepTypeEnum.md) | Input SweepTypeEnum indicates which sweep type you will use to create the sweep feature. |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object used to define the shape of the sweep. |
| Path | [Path](../Path/Path.md) | Input entity that defines the path of the sweep. Use the CreatePath or CreateSpecifiedPath methods on the PartFeatures object to create a Path. The path can be a combination of 2D and 3D sketch elements and can be open or closed. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, kSurfaceOperation or kNewBodyOperation. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |