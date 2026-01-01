# SculptFeatures.Add Method

Parent Object: [SculptFeatures](../SculptFeatures/SculptFeatures.md)

## Description

Method that creates a new SculptFeature. If the sculpt feature is created successfully, a SculptFeature object corresponding to the newly created sculpt feature is returned from this method.

## Syntax

SculptFeatures.**Add**( ***Surfaces*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md), [***AffectedBody***] As Variant ) As [SculptFeature](../SculptFeature/SculptFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surfaces | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection that contains SculptSurface objects that represent the set of surfaces and the corresponding directions that are required to create the sculpt feature. The CreateSculptSurface method should be used to create each of the SculptSurface objects which should then be added to an ObjectCollection. The ObjectCollection that contains these SculptSurface objects can be created using the CreateObjectCollection method of the TransientObjects object. The ObjectCollection should contain only SculptSurface objects, if the collection contains other types of objects, then the creation of the sculpt feature will fail. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input PartFeatureOperationEnum that specifies the operation type (kJoinOperation, kCutOperation and kNewBodyOperation). If kJoinOperation is specified, then the fill operation will be performed to add material. If kCutOperation is specified, then the drain operation will be performed to remove material. If kCutOperation is specified, then the part model should contain solid material that can be removed. Specifying kNewBodyOperation will result in creation of a new body. |
| AffectedBody | Variant | Optional input SurfaceBody object that specifies the body that should be affected by this sculpt operation. Applies only if kJoinOperation or kCutOperation is specified as the operation type. If not specified, a default body is used. |

## Version

Introduced in version 11
