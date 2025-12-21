# FaceFeatureDefinition Object

## Description

The FaceFeatureDefinition object represents all of the information that defines a face feature.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedBodies](../FaceFeatureDefinition/FaceFeatureDefinition_AffectedBodies.md) | Gets and sets the collection of bodies affected by this feature. If this property is not set for multi-body parts, the default solid body is used as the affected body. |
| [Application](../FaceFeatureDefinition/FaceFeatureDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendDefinition](../FaceFeatureDefinition/FaceFeatureDefinition_BendDefinition.md) | Get and sets the BendDefinition object that defines the bend information for this face feature. |
| [Direction](../FaceFeatureDefinition/FaceFeatureDefinition_Direction.md) | Gets and sets the extent direction which indicates which side of the sketch the projection of the face is in. |
| [Operation](../FaceFeatureDefinition/FaceFeatureDefinition_Operation.md) | Gets and sets the type of operation used to add the feature to the model. Valid inputs are kNewBodyOperation, kJoinOperation. |
| [Parent](../FaceFeatureDefinition/FaceFeatureDefinition_Parent.md) | Property that returns the parent FaceFeature object of this FaceFeatureDefinition object. |
| [Profile](../FaceFeatureDefinition/FaceFeatureDefinition_Profile.md) | Gets and sets the Profile object that defines the shape of the face feature. |
| [SheetMetalRule](../FaceFeatureDefinition/FaceFeatureDefinition_SheetMetalRule.md) | Read-write property that gets and sets the sheet metal style for the body the feature is in. Set this property is applicable only when the feature is the first feature in a solid body. When set this property the default sheet metal rule will be overridden and. |
| [Type](../FaceFeatureDefinition/FaceFeatureDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseDefaultSheetMetalRule](../FaceFeatureDefinition/FaceFeatureDefinition_UseDefaultSheetMetalRule.md) | Read-write property that gets and sets whether to use the document active sheet metal style for the body the feature is in. Set this property is applicable only when the feature is the first feature in a solid body and this can only be set to True from False. |

## Accessed From

[FaceFeature.Definition](../FaceFeature/FaceFeature_Definition.md), [FaceFeatureProxy.Definition](../FaceFeatureProxy/FaceFeatureProxy_Definition.md), [FaceFeatures.CreateFaceFeatureDefinition](../FaceFeatures/FaceFeatures_CreateFaceFeatureDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 2009
