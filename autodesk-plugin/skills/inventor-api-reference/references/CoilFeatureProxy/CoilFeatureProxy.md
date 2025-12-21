# CoilFeatureProxy Object

Derived from: [CoilFeature](../CoilFeature/CoilFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../CoilFeatureProxy/CoilFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CoilFeatureProxy/CoilFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CoilFeatureProxy/CoilFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CoilFeatureProxy/CoilFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CoilFeatureProxy/CoilFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CoilFeatureProxy/CoilFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetPitchAndHeightExtent](../CoilFeatureProxy/CoilFeatureProxy_SetPitchAndHeightExtent.md) | Set coil feature pitch and height extent. |
| [SetPitchAndRevolutionExtent](../CoilFeatureProxy/CoilFeatureProxy_SetPitchAndRevolutionExtent.md) | Set coil feature pitch and revolution extent. |
| [SetRevolutionAndHeightExtent](../CoilFeatureProxy/CoilFeatureProxy_SetRevolutionAndHeightExtent.md) | Set coil feature revolution and height extent. |
| [SetSpiralExtent](../CoilFeatureProxy/CoilFeatureProxy_SetSpiralExtent.md) | Set coil feature spiral extent. |
| [SetSuppressionCondition](../CoilFeatureProxy/CoilFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CoilFeatureProxy/CoilFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CoilFeatureProxy/CoilFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CoilFeatureProxy/CoilFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CoilFeatureProxy/CoilFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CoilFeatureProxy/CoilFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxisDirectionReversed](../CoilFeatureProxy/CoilFeatureProxy_AxisDirectionReversed.md) | Property that gets and sets whether the axis direction of the coil is reversed. |
| [AxisEntity](../CoilFeatureProxy/CoilFeatureProxy_AxisEntity.md) | Property that gets and sets the entity used to define the axis of the coil. Valid input is either a sketch line or work axis. The axis entity must not intersect the profile. |
| [ClockwiseRotation](../CoilFeatureProxy/CoilFeatureProxy_ClockwiseRotation.md) | Property that gets and sets whether the rotation is clockwise or counter-clockwise. A value of True indicates clockwise rotation. |
| [ConsumeInputs](../CoilFeatureProxy/CoilFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../CoilFeatureProxy/CoilFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [EndFlatAngle](../CoilFeatureProxy/CoilFeatureProxy_EndFlatAngle.md) | Property that returns the parameter that controls the flat angle at the end of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatEndType is False. |
| [EndTransitionAngle](../CoilFeatureProxy/CoilFeatureProxy_EndTransitionAngle.md) | Property that returns the parameter that controls the transition angle at the end of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatEndType is False. |
| [ExtendedName](../CoilFeatureProxy/CoilFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Extent](../CoilFeatureProxy/CoilFeatureProxy_Extent.md) | Property that returns the object that defines how the extent of the feature is defined. The type of extent object that this property will return can be determined by using the ExtentType property. |
| [ExtentType](../CoilFeatureProxy/CoilFeatureProxy_ExtentType.md) | Property that returns an enum indicating how the extent of the feature is defined. This indicates the type of object returned by the Extent property. |
| [Faces](../CoilFeatureProxy/CoilFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CoilFeatureProxy/CoilFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [FlatEndType](../CoilFeatureProxy/CoilFeatureProxy_FlatEndType.md) | Property that gets and sets the coil end type at the end of the coil feature. |
| [FlatStartType](../CoilFeatureProxy/CoilFeatureProxy_FlatStartType.md) | Property that gets and sets the coil end type at the start of the coil feature. |
| [HealthStatus](../CoilFeatureProxy/CoilFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CoilFeatureProxy/CoilFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CoilFeatureProxy/CoilFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../CoilFeatureProxy/CoilFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Operation](../CoilFeatureProxy/CoilFeatureProxy_Operation.md) | Gets and sets the type of operation used to add the feature to the model. |
| [OwnedBy](../CoilFeatureProxy/CoilFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CoilFeatureProxy/CoilFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CoilFeatureProxy/CoilFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CoilFeatureProxy/CoilFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [Profile](../CoilFeatureProxy/CoilFeatureProxy_Profile.md) | Property that gets and sets the profile that defines the shape of the coil. |
| [RangeBox](../CoilFeatureProxy/CoilFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CoilFeatureProxy/CoilFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [StartFlatAngle](../CoilFeatureProxy/CoilFeatureProxy_StartFlatAngle.md) | Property that returns the parameter that controls the flat angle at the start of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatStartType is False. |
| [StartTransitionAngle](../CoilFeatureProxy/CoilFeatureProxy_StartTransitionAngle.md) | Property that returns the parameter that controls the transition angle at the start of the coil feature. This property returns Nothing if ExtentType is kSpiral or FlatStartType is False. |
| [Suppressed](../CoilFeatureProxy/CoilFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CoilFeatureProxy/CoilFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../CoilFeatureProxy/CoilFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |