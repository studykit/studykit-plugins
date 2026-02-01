# EmbossFeatureProxy Object

Derived from: [EmbossFeature](../EmbossFeature/EmbossFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../EmbossFeatureProxy/EmbossFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../EmbossFeatureProxy/EmbossFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../EmbossFeatureProxy/EmbossFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../EmbossFeatureProxy/EmbossFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../EmbossFeatureProxy/EmbossFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEmbossEngraveFromPlane](../EmbossFeatureProxy/EmbossFeatureProxy_SetEmbossEngraveFromPlane.md) | Method that redefines the emboss feature by embossing and/or engraving a profile on one or more faces in the model. |
| [SetEmbossFromFace](../EmbossFeatureProxy/EmbossFeatureProxy_SetEmbossFromFace.md) | Method that redefines the emboss feature by embossing a profile on one or more faces in the model. |
| [SetEndOfPart](../EmbossFeatureProxy/EmbossFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetEngraveFromFace](../EmbossFeatureProxy/EmbossFeatureProxy_SetEngraveFromFace.md) | Method that redefines the emboss feature by engraving a profile on one or more faces in the model. |
| [SetSuppressionCondition](../EmbossFeatureProxy/EmbossFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../EmbossFeatureProxy/EmbossFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../EmbossFeatureProxy/EmbossFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../EmbossFeatureProxy/EmbossFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../EmbossFeatureProxy/EmbossFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EmbossFeatureProxy/EmbossFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../EmbossFeatureProxy/EmbossFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../EmbossFeatureProxy/EmbossFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Depth](../EmbossFeatureProxy/EmbossFeatureProxy_Depth.md) | Property returns the parameter controlling the depth of the emboss feature. |
| [Direction](../EmbossFeatureProxy/EmbossFeatureProxy_Direction.md) | Gets and sets the direction of the emboss feature relative to the sketch plane that contains the emboss profile. |
| [EmbossType](../EmbossFeatureProxy/EmbossFeatureProxy_EmbossType.md) | Property that returns the type of emboss feature. |
| [ExtendedName](../EmbossFeatureProxy/EmbossFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../EmbossFeatureProxy/EmbossFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../EmbossFeatureProxy/EmbossFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../EmbossFeatureProxy/EmbossFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../EmbossFeatureProxy/EmbossFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../EmbossFeatureProxy/EmbossFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../EmbossFeatureProxy/EmbossFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../EmbossFeatureProxy/EmbossFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../EmbossFeatureProxy/EmbossFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../EmbossFeatureProxy/EmbossFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../EmbossFeatureProxy/EmbossFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [Profile](../EmbossFeatureProxy/EmbossFeatureProxy_Profile.md) | Gets and sets the Profile object that defines the shape of the emboss. |
| [RangeBox](../EmbossFeatureProxy/EmbossFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../EmbossFeatureProxy/EmbossFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../EmbossFeatureProxy/EmbossFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../EmbossFeatureProxy/EmbossFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Taper](../EmbossFeatureProxy/EmbossFeatureProxy_Taper.md) | Property that returns the parameter controlling the taper angle of the emboss feature. |
| [TopFaceAppearance](../EmbossFeatureProxy/EmbossFeatureProxy_TopFaceAppearance.md) | Gets and sets the top face appearance of the emboss feature. |
| [TopFaceAppearanceSourceType](../EmbossFeatureProxy/EmbossFeatureProxy_TopFaceAppearanceSourceType.md) | Gets and sets the source of the appearance for the top face of the emboss feature. |
| [Type](../EmbossFeatureProxy/EmbossFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WrapFace](../EmbossFeatureProxy/EmbossFeatureProxy_WrapFace.md) | Gets and sets the face around which the emboss feature is wrapped. |
| [WrapToFace](../EmbossFeatureProxy/EmbossFeatureProxy_WrapToFace.md) | Property that returns a Boolean indicating if the emboss feature is wrapped around a face. |

## Version

Introduced in version 9
