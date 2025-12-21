# MirrorFeatures.CreateDefinition Method

Parent Object: [MirrorFeatures](../MirrorFeatures/MirrorFeatures.md)

## Description

Method that creates a new MirrorFeatureDefinition object.

## Syntax

MirrorFeatures.**CreateDefinition**( ***ParentFeatures*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***MirrorPlaneEntity*** As Object, [***ComputeType***] As [PatternComputeTypeEnum](../PatternComputeTypeEnum.md) ) As [MirrorFeatureDefinition](../MirrorFeatureDefinition/MirrorFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentFeatures | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the features or solids to be patterned. The collection could contain the various part features, sheet metal features, work planes, work axes, work points, or SurfaceBody objects. If SurfaceBody objects are supplied, the only other objects that can be in the collection are work planes, work axes, work points, and surface part features. Finish features such as fillets and chamfers may be included only if their parent feature is also included. |
| MirrorPlaneEntity | Object | Input planar entity that defines the mirror plane. This can be either a planar face or a work plane. |
| ComputeType | [PatternComputeTypeEnum](../PatternComputeTypeEnum.md) | Optional input enum that indicates the method of solution for the pattern. If specified as kOptimizedCompute, patterns are optimized for faster calculation. If kIdenticalCompute is specified, all occurrences in the pattern use an identical termination, regardless of where they intersect another feature. Use this method to efficiently pattern large numbers of features when the feature being duplicated has a distance termination or terminates on a work plane. If kAdjustToModelCompute is specified, the termination of each occurrence is calculated individually. Computation time can be lengthy for patterns with a large number of occurrences. You must use this method if the parent feature terminates on a model face. |

## Version

Introduced in version 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |