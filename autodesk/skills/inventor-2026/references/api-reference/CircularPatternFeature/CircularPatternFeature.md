# CircularPatternFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The CircularPatternFeature object represents circular pattern feature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../CircularPatternFeature/CircularPatternFeature_AddParticipant.md) | Method that adds the specified participant to the assembly feature. This method fails for features in a part. |
| [Delete](../CircularPatternFeature/CircularPatternFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../CircularPatternFeature/CircularPatternFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../CircularPatternFeature/CircularPatternFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../CircularPatternFeature/CircularPatternFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../CircularPatternFeature/CircularPatternFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../CircularPatternFeature/CircularPatternFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../CircularPatternFeature/CircularPatternFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../CircularPatternFeature/CircularPatternFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../CircularPatternFeature/CircularPatternFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../CircularPatternFeature/CircularPatternFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../CircularPatternFeature/CircularPatternFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CircularPatternFeature/CircularPatternFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../CircularPatternFeature/CircularPatternFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../CircularPatternFeature/CircularPatternFeature_Definition.md) | Read-write property that gets and sets the CircularPatternFeatureDefinition object associated with this feature. |
| [ExtendedName](../CircularPatternFeature/CircularPatternFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../CircularPatternFeature/CircularPatternFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../CircularPatternFeature/CircularPatternFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../CircularPatternFeature/CircularPatternFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../CircularPatternFeature/CircularPatternFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../CircularPatternFeature/CircularPatternFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../CircularPatternFeature/CircularPatternFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../CircularPatternFeature/CircularPatternFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../CircularPatternFeature/CircularPatternFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../CircularPatternFeature/CircularPatternFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PatternElements](../CircularPatternFeature/CircularPatternFeature_PatternElements.md) | Property that returns the collection that contains the elements created by this pattern. |
| [RangeBox](../CircularPatternFeature/CircularPatternFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../CircularPatternFeature/CircularPatternFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../CircularPatternFeature/CircularPatternFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../CircularPatternFeature/CircularPatternFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [SurfacesOpaque](../CircularPatternFeature/CircularPatternFeature_SurfacesOpaque.md) | Gets and sets whether all the resulting surfaces are opaque or transparent. |
| [SurfacesVisible](../CircularPatternFeature/CircularPatternFeature_SurfacesVisible.md) | Gets and sets whether all the resulting surfaces are visible or not. |
| [Type](../CircularPatternFeature/CircularPatternFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CircularPatternFeatureProxy.NativeObject](../CircularPatternFeatureProxy/CircularPatternFeatureProxy_NativeObject.md), [CircularPatternFeatures.AddByDefinition](../CircularPatternFeatures/CircularPatternFeatures_AddByDefinition.md), [CircularPatternFeatures.Item](../CircularPatternFeatures/CircularPatternFeatures_Item.md)

## Derived Classes

[CircularPatternFeatureProxy](../CircularPatternFeatureProxy/CircularPatternFeatureProxy.md)

## Version

Introduced in version 5
