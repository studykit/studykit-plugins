# ReplaceFaceFeatures.CreateDefinition Method

Parent Object: [ReplaceFaceFeatures](../ReplaceFaceFeatures/ReplaceFaceFeatures.md)

## Description

Method that creates a ReplaceFaceDefinition.

## Syntax

ReplaceFaceFeatures.**CreateDefinition**( ***ExistingFaces*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***NewFaces*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) ) As [ReplaceFaceDefinition](../ReplaceFaceDefinition/ReplaceFaceDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExistingFaces | [FaceCollection](../FaceCollection/FaceCollection.md) | Input FaceCollection object that specifies the faces that will be replaced. The faces must be part of a solid SurfaceBody and must all belong to the same SurfaceBody. All faces to be replaced need to be specified. All of the input faces must belong to the same SurfaceBody. The TangentiallyConnectedFaces method of the Face object can be useful in finding the set of faces. |
| NewFaces | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that specifies the new faces. The new faces can be work planes or Face objects, the Face objects can be from multiple SurfaceBody objects |

## Version

Introduced in version 2024.1
