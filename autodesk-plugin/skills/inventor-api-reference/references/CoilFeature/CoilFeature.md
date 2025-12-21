# CoilFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The CoilFeature object represents coil modeling features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CoilFeature/CoilFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CoilFeature/CoilFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CoilFeature/CoilFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CoilFeature/CoilFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CoilFeature/CoilFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CoilFeature/CoilFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetPitchAndHeightExtent](../CoilFeature/CoilFeature_SetPitchAndHeightExtent.md) | Set coil feature pitch and height extent. |
| [SetPitchAndRevolutionExtent](../CoilFeature/CoilFeature_SetPitchAndRevolutionExtent.md) | Set coil feature pitch and revolution extent. |
| [SetRevolutionAndHeightExtent](../CoilFeature/CoilFeature_SetRevolutionAndHeightExtent.md) | Set coil feature revolution and height extent. |
| [SetSpiralExtent](../CoilFeature/CoilFeature_SetSpiralExtent.md) | Set coil feature spiral extent. |
| [SetSuppressionCondition](../CoilFeature/CoilFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CoilFeature/CoilFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CoilFeature/CoilFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CoilFeature/CoilFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CoilFeature/CoilFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CoilFeature/CoilFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisDirectionReversed](../CoilFeature/CoilFeature_AxisDirectionReversed.md) | Property that gets and sets whether the axis direction of the coil is reversed. |
| [AxisEntity](../CoilFeature/CoilFeature_AxisEntity.md) | Property that gets and sets the entity used to define the axis of the coil. Valid input is either a sketch line or work axis. The axis entity must not intersect the profile. |
| [ClockwiseRotation](../CoilFeature/CoilFeature_ClockwiseRotation.md) | Property that gets and sets whether the rotation is clockwise or counter-clockwise. A value of True indicates clockwise rotation. |
| [ConsumeInputs](../CoilFeature/CoilFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [EndFlatAngle](../CoilFeature/CoilFeature_EndFlatAngle.md) | Property that returns the parameter that controls the flat angle at the end of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatEndType is False. |
| [EndTransitionAngle](../CoilFeature/CoilFeature_EndTransitionAngle.md) | Property that returns the parameter that controls the transition angle at the end of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatEndType is False. |
| [ExtendedName](../CoilFeature/CoilFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Extent](../CoilFeature/CoilFeature_Extent.md) | Property that returns the object that defines how the extent of the feature is defined. The type of extent object that this property will return can be determined by using the ExtentType property. |
| [ExtentType](../CoilFeature/CoilFeature_ExtentType.md) | Property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent property. |
| [Faces](../CoilFeature/CoilFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CoilFeature/CoilFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [FlatEndType](../CoilFeature/CoilFeature_FlatEndType.md) | Property that gets and sets the coil end type at the end of the coil feature. |
| [FlatStartType](../CoilFeature/CoilFeature_FlatStartType.md) | Property that gets and sets the coil end type at the start of the coil feature. |
| [HealthStatus](../CoilFeature/CoilFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CoilFeature/CoilFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CoilFeature/CoilFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [Operation](../CoilFeature/CoilFeature_Operation.md) | Gets and sets the type of operation used to add the feature to the model. |
| [OwnedBy](../CoilFeature/CoilFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CoilFeature/CoilFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CoilFeature/CoilFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CoilFeature/CoilFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [Profile](../CoilFeature/CoilFeature_Profile.md) | Property that gets and sets the profile that defines the shape of the coil. |
| [RangeBox](../CoilFeature/CoilFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CoilFeature/CoilFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [StartFlatAngle](../CoilFeature/CoilFeature_StartFlatAngle.md) | Property that returns the parameter that controls the flat angle at the start of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatStartType is False. |
| [StartTransitionAngle](../CoilFeature/CoilFeature_StartTransitionAngle.md) | Property that returns the parameter that controls the transition angle at the start of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatStartType is False. |
| [Suppressed](../CoilFeature/CoilFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CoilFeature/CoilFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../CoilFeature/CoilFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CoilFeatureProxy.NativeObject](../CoilFeatureProxy/CoilFeatureProxy_NativeObject.md), [CoilFeatures.AddByPitchAndHeight](../CoilFeatures/CoilFeatures_AddByPitchAndHeight.md), [CoilFeatures.AddByPitchAndRevolution](../CoilFeatures/CoilFeatures_AddByPitchAndRevolution.md), [CoilFeatures.AddByRevolutionAndHeight](../CoilFeatures/CoilFeatures_AddByRevolutionAndHeight.md), [CoilFeatures.AddSpiral](../CoilFeatures/CoilFeatures_AddSpiral.md), [CoilFeatures.Item](../CoilFeatures/CoilFeatures_Item.md)

## Derived Classes

[CoilFeatureProxy](../CoilFeatureProxy/CoilFeatureProxy.md)

## Version

Introduced in version 5
