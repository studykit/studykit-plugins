# RevolveFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The RevolveFeature object represents revolved modeling features. The properties and methods listed below are in addition to those supported by the Feature object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../RevolveFeature/RevolveFeature_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../RevolveFeature/RevolveFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RevolveFeature/RevolveFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RevolveFeature/RevolveFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RevolveFeature/RevolveFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RevolveFeature/RevolveFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetAngleExtent](../RevolveFeature/RevolveFeature_SetAngleExtent.md) | Method that changes the extents of the revolution to the given angle |
| [SetEndOfPart](../RevolveFeature/RevolveFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetFromToExtent](../RevolveFeature/RevolveFeature_SetFromToExtent.md) | Method that changes the extents to be 'from and to face' extents. |
| [SetFullExtent](../RevolveFeature/RevolveFeature_SetFullExtent.md) | Method that changes the angle of the revolve to a full (360-degree) revolution. |
| [SetSuppressionCondition](../RevolveFeature/RevolveFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetToFaceExtent](../RevolveFeature/RevolveFeature_SetToFaceExtent.md) | Method that changes the extents to be 'to face' extents. |
| [SetToNextExtent](../RevolveFeature/RevolveFeature_SetToNextExtent.md) | Method that changes the extents to be 'to next face' extents. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RevolveFeature/RevolveFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RevolveFeature/RevolveFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RevolveFeature/RevolveFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RevolveFeature/RevolveFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RevolveFeature/RevolveFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisEntity](../RevolveFeature/RevolveFeature_AxisEntity.md) | Gets and sets the entity used to define the axis of revolution. |
| [ConsumeInputs](../RevolveFeature/RevolveFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [EndFaces](../RevolveFeature/RevolveFeature_EndFaces.md) | Property that returns the set of that cap one end of the revolution that are coincident with the sketch plane. The end faces are those not coincident to the sketch plane of the feature's profile. In the case of a symmetric revolution these faces are the ones on the negative normal side of the sketch plane. In the cases where there aren't any end faces this property will return Nothing. |
| [ExtendedName](../RevolveFeature/RevolveFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Extent](../RevolveFeature/RevolveFeature_Extent.md) | Property that returns the object that defines how the extent of the feature is defined. The type of extent object that this property will return can be determined by using the ExtentType property. |
| [ExtentTwo](../RevolveFeature/RevolveFeature_ExtentTwo.md) | Property that returns the PartFeatureExtent object that defines how the second direction extent of the feature is defined. The type of extent object returned can be determined by using the ExtentTwoType property. This property returns Nothing if the IsTwoDirectional property returns False. |
| [ExtentTwoType](../RevolveFeature/RevolveFeature_ExtentTwoType.md) | Property that returns an enum indicating how the second direction extent of the feature is defined. This indicates the type of object returned by the Extent property. This property returns a failure if the IsTwoDirectional property \returns False. |
| [ExtentType](../RevolveFeature/RevolveFeature_ExtentType.md) | Property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent property. The valid possibilities returned are kAngleExtent and kFullSweepExtent. |
| [Faces](../RevolveFeature/RevolveFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RevolveFeature/RevolveFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RevolveFeature/RevolveFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RevolveFeature/RevolveFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsTwoDirectional](../RevolveFeature/RevolveFeature_IsTwoDirectional.md) | Property that returns whether extents have been defined in two directions for the revolve. If this property returns True, the ExtentTwoType and ExtentTwo properties can be used to query details about the second direction extent. |
| [Name](../RevolveFeature/RevolveFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [Operation](../RevolveFeature/RevolveFeature_Operation.md) | Property that gets and sets the type of operation used to add the feature to the model. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, or kSurfaceOperation. |
| [OwnedBy](../RevolveFeature/RevolveFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RevolveFeature/RevolveFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RevolveFeature/RevolveFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RevolveFeature/RevolveFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [Profile](../RevolveFeature/RevolveFeature_Profile.md) | Gets and sets the Profile that defines the shape of the feature. |
| [RangeBox](../RevolveFeature/RevolveFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RevolveFeature/RevolveFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../RevolveFeature/RevolveFeature_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [StartFaces](../RevolveFeature/RevolveFeature_StartFaces.md) | Property that returns the set of that cap one end of the revolution that are coincident with the sketch plane. In the case of a symmetric revolution these faces are the ones on the positive normal side of the sketch plane. In the cases where there aren't any start faces this property will return Nothing. |
| [Suppressed](../RevolveFeature/RevolveFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RevolveFeature/RevolveFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RevolveFeature/RevolveFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[RevolveFeatureProxy.NativeObject](../RevolveFeatureProxy/RevolveFeatureProxy_NativeObject.md), [RevolveFeatures.AddByAngle](../RevolveFeatures/RevolveFeatures_AddByAngle.md), [RevolveFeatures.AddByFromToExtent](../RevolveFeatures/RevolveFeatures_AddByFromToExtent.md), [RevolveFeatures.AddByToFaceExtent](../RevolveFeatures/RevolveFeatures_AddByToFaceExtent.md), [RevolveFeatures.AddByToNextExtent](../RevolveFeatures/RevolveFeatures_AddByToNextExtent.md), [RevolveFeatures.AddFull](../RevolveFeatures/RevolveFeatures_AddFull.md), [RevolveFeatures.Item](../RevolveFeatures/RevolveFeatures_Item.md)

## Derived Classes

[RevolveFeatureProxy](../RevolveFeatureProxy/RevolveFeatureProxy.md)

## Version

Introduced in version 5
