# RevolveFeatureProxy Object

Derived from: [RevolveFeature](../RevolveFeature/RevolveFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../RevolveFeatureProxy/RevolveFeatureProxy_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../RevolveFeatureProxy/RevolveFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RevolveFeatureProxy/RevolveFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RevolveFeatureProxy/RevolveFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RevolveFeatureProxy/RevolveFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RevolveFeatureProxy/RevolveFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetAngleExtent](../RevolveFeatureProxy/RevolveFeatureProxy_SetAngleExtent.md) | Method that changes the extents of the revolution to the given angle |
| [SetEndOfPart](../RevolveFeatureProxy/RevolveFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetFromToExtent](../RevolveFeatureProxy/RevolveFeatureProxy_SetFromToExtent.md) | Method that changes the extents to be 'from and to face' extents. |
| [SetFullExtent](../RevolveFeatureProxy/RevolveFeatureProxy_SetFullExtent.md) | Method that changes the angle of the revolve to a full (360-degree) revolution. |
| [SetSuppressionCondition](../RevolveFeatureProxy/RevolveFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |
| [SetToFaceExtent](../RevolveFeatureProxy/RevolveFeatureProxy_SetToFaceExtent.md) | Method that changes the extents to be 'to face' extents. |
| [SetToNextExtent](../RevolveFeatureProxy/RevolveFeatureProxy_SetToNextExtent.md) | Method that changes the extents to be 'to next face' extents. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RevolveFeatureProxy/RevolveFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RevolveFeatureProxy/RevolveFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RevolveFeatureProxy/RevolveFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RevolveFeatureProxy/RevolveFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RevolveFeatureProxy/RevolveFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisEntity](../RevolveFeatureProxy/RevolveFeatureProxy_AxisEntity.md) | Gets and sets the entity used to define the axis of revolution. |
| [ConsumeInputs](../RevolveFeatureProxy/RevolveFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../RevolveFeatureProxy/RevolveFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EndFaces](../RevolveFeatureProxy/RevolveFeatureProxy_EndFaces.md) | Property that returns the set of that cap one end of the revolution that are coincident with the sketch plane. The end faces are those not coincident to the sketch plane of the feature's profile. In the case of a symmetric revolution these faces are the ones on the negative normal side of the sketch plane. In the cases where there aren't any end faces this property will return Nothing. |
| [ExtendedName](../RevolveFeatureProxy/RevolveFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Extent](../RevolveFeatureProxy/RevolveFeatureProxy_Extent.md) | Property that returns the object that defines how the extent of the feature is defined. The type of extent object that this property will return can be determined by using the ExtentType property. |
| [ExtentTwo](../RevolveFeatureProxy/RevolveFeatureProxy_ExtentTwo.md) | Property that returns the PartFeatureExtent object that defines how the second direction extent of the feature is defined. The type of extent object returned can be determined by using the ExtentTwoType property. This property returns Nothing if the IsTwoDirectional property returns False. |
| [ExtentTwoType](../RevolveFeatureProxy/RevolveFeatureProxy_ExtentTwoType.md) | Property that returns an enum indicating how the second direction extent of the feature is defined. This indicates the type of object returned by the Extent property. This property returns a failure if the IsTwoDirectional property \returns False. |
| [ExtentType](../RevolveFeatureProxy/RevolveFeatureProxy_ExtentType.md) | Property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent property. The valid possibilities returned are kAngleExtent and kFullSweepExtent. |
| [Faces](../RevolveFeatureProxy/RevolveFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RevolveFeatureProxy/RevolveFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RevolveFeatureProxy/RevolveFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RevolveFeatureProxy/RevolveFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsTwoDirectional](../RevolveFeatureProxy/RevolveFeatureProxy_IsTwoDirectional.md) | Property that returns whether extents have been defined in two directions for the revolve. If this property returns True, the ExtentTwoType and ExtentTwo properties can be used to query details about the second direction extent. |
| [Name](../RevolveFeatureProxy/RevolveFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../RevolveFeatureProxy/RevolveFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Operation](../RevolveFeatureProxy/RevolveFeatureProxy_Operation.md) | Property that gets and sets the type of operation used to add the feature to the model. Valid input is kJoinOperation, kCutOperation, kIntersectOperation, or kSurfaceOperation. |
| [OwnedBy](../RevolveFeatureProxy/RevolveFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RevolveFeatureProxy/RevolveFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RevolveFeatureProxy/RevolveFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RevolveFeatureProxy/RevolveFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [Profile](../RevolveFeatureProxy/RevolveFeatureProxy_Profile.md) | Gets and sets the Profile that defines the shape of the feature. |
| [RangeBox](../RevolveFeatureProxy/RevolveFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RevolveFeatureProxy/RevolveFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../RevolveFeatureProxy/RevolveFeatureProxy_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [StartFaces](../RevolveFeatureProxy/RevolveFeatureProxy_StartFaces.md) | Property that returns the set of that cap one end of the revolution that are coincident with the sketch plane. In the case of a symmetric revolution these faces are the ones on the positive normal side of the sketch plane. In the cases where there aren't any start faces this property will return Nothing. |
| [Suppressed](../RevolveFeatureProxy/RevolveFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RevolveFeatureProxy/RevolveFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RevolveFeatureProxy/RevolveFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
