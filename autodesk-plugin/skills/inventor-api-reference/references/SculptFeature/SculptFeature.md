# SculptFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The SculptFeature object represents sculpt modeling features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SculptFeature/SculptFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../SculptFeature/SculptFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../SculptFeature/SculptFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../SculptFeature/SculptFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../SculptFeature/SculptFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../SculptFeature/SculptFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../SculptFeature/SculptFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../SculptFeature/SculptFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../SculptFeature/SculptFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../SculptFeature/SculptFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../SculptFeature/SculptFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SculptFeature/SculptFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../SculptFeature/SculptFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../SculptFeature/SculptFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../SculptFeature/SculptFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../SculptFeature/SculptFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../SculptFeature/SculptFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../SculptFeature/SculptFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../SculptFeature/SculptFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [Operation](../SculptFeature/SculptFeature_Operation.md) | Gets and sets the type of operation used to add the feature to the model. |
| [OwnedBy](../SculptFeature/SculptFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../SculptFeature/SculptFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../SculptFeature/SculptFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../SculptFeature/SculptFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../SculptFeature/SculptFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../SculptFeature/SculptFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../SculptFeature/SculptFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../SculptFeature/SculptFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Surfaces](../SculptFeature/SculptFeature_Surfaces.md) | Gets and sets the set of surfaces and their respective directions associated with the sculpt feature. |
| [Type](../SculptFeature/SculptFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SculptFeatureProxy.NativeObject](../SculptFeatureProxy/SculptFeatureProxy_NativeObject.md), [SculptFeatures.Add](../SculptFeatures/SculptFeatures_Add.md), [SculptFeatures.Item](../SculptFeatures/SculptFeatures_Item.md)

## Derived Classes

[SculptFeatureProxy](../SculptFeatureProxy/SculptFeatureProxy.md)

## Version

Introduced in version 11
