# EmbossFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The EmbossFeature object represents an emboss feature on a part.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../EmbossFeature/EmbossFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../EmbossFeature/EmbossFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../EmbossFeature/EmbossFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../EmbossFeature/EmbossFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../EmbossFeature/EmbossFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEmbossEngraveFromPlane](../EmbossFeature/EmbossFeature_SetEmbossEngraveFromPlane.md) | Method that redefines the emboss feature by embossing and/or engraving a profile on one or more faces in the model. |
| [SetEmbossFromFace](../EmbossFeature/EmbossFeature_SetEmbossFromFace.md) | Method that redefines the emboss feature by embossing a profile on one or more faces in the model. |
| [SetEndOfPart](../EmbossFeature/EmbossFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetEngraveFromFace](../EmbossFeature/EmbossFeature_SetEngraveFromFace.md) | Method that redefines the emboss feature by engraving a profile on one or more faces in the model. |
| [SetSuppressionCondition](../EmbossFeature/EmbossFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../EmbossFeature/EmbossFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../EmbossFeature/EmbossFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../EmbossFeature/EmbossFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../EmbossFeature/EmbossFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../EmbossFeature/EmbossFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../EmbossFeature/EmbossFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Depth](../EmbossFeature/EmbossFeature_Depth.md) | Property returns the parameter controlling the depth of the emboss feature. |
| [Direction](../EmbossFeature/EmbossFeature_Direction.md) | Gets and sets the direction of the emboss feature relative to the sketch plane that contains the emboss profile. |
| [EmbossType](../EmbossFeature/EmbossFeature_EmbossType.md) | Property that returns the type of emboss feature. |
| [ExtendedName](../EmbossFeature/EmbossFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../EmbossFeature/EmbossFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../EmbossFeature/EmbossFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../EmbossFeature/EmbossFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../EmbossFeature/EmbossFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../EmbossFeature/EmbossFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../EmbossFeature/EmbossFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../EmbossFeature/EmbossFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../EmbossFeature/EmbossFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../EmbossFeature/EmbossFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [Profile](../EmbossFeature/EmbossFeature_Profile.md) | Gets and sets the Profile object that defines the shape of the emboss. |
| [RangeBox](../EmbossFeature/EmbossFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../EmbossFeature/EmbossFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../EmbossFeature/EmbossFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../EmbossFeature/EmbossFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Taper](../EmbossFeature/EmbossFeature_Taper.md) | Property that returns the parameter controlling the taper angle of the emboss feature. |
| [TopFaceAppearance](../EmbossFeature/EmbossFeature_TopFaceAppearance.md) | Gets and sets the top face appearance of the emboss feature. |
| [TopFaceAppearanceSourceType](../EmbossFeature/EmbossFeature_TopFaceAppearanceSourceType.md) | Gets and sets the source of the appearance for the top face of the emboss feature. |
| [Type](../EmbossFeature/EmbossFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WrapFace](../EmbossFeature/EmbossFeature_WrapFace.md) | Gets and sets the face around which the emboss feature is wrapped. |
| [WrapToFace](../EmbossFeature/EmbossFeature_WrapToFace.md) | Property that returns a Boolean indicating if the emboss feature is wrapped around a face. |

## Accessed From

[EmbossFeatureProxy.NativeObject](../EmbossFeatureProxy/EmbossFeatureProxy_NativeObject.md), [EmbossFeatures.AddEmbossEngraveFromPlane](../EmbossFeatures/EmbossFeatures_AddEmbossEngraveFromPlane.md), [EmbossFeatures.AddEmbossFromFace](../EmbossFeatures/EmbossFeatures_AddEmbossFromFace.md), [EmbossFeatures.AddEngraveFromFace](../EmbossFeatures/EmbossFeatures_AddEngraveFromFace.md), [EmbossFeatures.Item](../EmbossFeatures/EmbossFeatures_Item.md)

## Derived Classes

[EmbossFeatureProxy](../EmbossFeatureProxy/EmbossFeatureProxy.md)

## Version

Introduced in version 6
