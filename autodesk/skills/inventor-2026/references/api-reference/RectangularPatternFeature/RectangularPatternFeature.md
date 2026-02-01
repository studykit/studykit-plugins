# RectangularPatternFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The RectangularPatternFeature object represents rectangular pattern feature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../RectangularPatternFeature/RectangularPatternFeature_AddParticipant.md) | Add the specified occurrence from the list of participants for this feature. This method only applies to assembly features. |
| [Delete](../RectangularPatternFeature/RectangularPatternFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RectangularPatternFeature/RectangularPatternFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RectangularPatternFeature/RectangularPatternFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RectangularPatternFeature/RectangularPatternFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RectangularPatternFeature/RectangularPatternFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RectangularPatternFeature/RectangularPatternFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RectangularPatternFeature/RectangularPatternFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RectangularPatternFeature/RectangularPatternFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RectangularPatternFeature/RectangularPatternFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RectangularPatternFeature/RectangularPatternFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RectangularPatternFeature/RectangularPatternFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RectangularPatternFeature/RectangularPatternFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../RectangularPatternFeature/RectangularPatternFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../RectangularPatternFeature/RectangularPatternFeature_Definition.md) | Read-write property that gets and sets the RectangularPatternFeatureDefinition object associated with this feature. |
| [ExtendedName](../RectangularPatternFeature/RectangularPatternFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RectangularPatternFeature/RectangularPatternFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RectangularPatternFeature/RectangularPatternFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RectangularPatternFeature/RectangularPatternFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RectangularPatternFeature/RectangularPatternFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RectangularPatternFeature/RectangularPatternFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../RectangularPatternFeature/RectangularPatternFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RectangularPatternFeature/RectangularPatternFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RectangularPatternFeature/RectangularPatternFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RectangularPatternFeature/RectangularPatternFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PatternElements](../RectangularPatternFeature/RectangularPatternFeature_PatternElements.md) | Property that returns the collection that contains the elements created by this pattern. |
| [RangeBox](../RectangularPatternFeature/RectangularPatternFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RectangularPatternFeature/RectangularPatternFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../RectangularPatternFeature/RectangularPatternFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RectangularPatternFeature/RectangularPatternFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [SurfacesOpaque](../RectangularPatternFeature/RectangularPatternFeature_SurfacesOpaque.md) | Gets and sets whether all the resulting surfaces are opaque or transparent. |
| [SurfacesVisible](../RectangularPatternFeature/RectangularPatternFeature_SurfacesVisible.md) | Gets and sets whether all the resulting surfaces are visible or not. |
| [Type](../RectangularPatternFeature/RectangularPatternFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[RectangularPatternFeatureProxy.NativeObject](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy_NativeObject.md), [RectangularPatternFeatures.AddByDefinition](../RectangularPatternFeatures/RectangularPatternFeatures_AddByDefinition.md), [RectangularPatternFeatures.Item](../RectangularPatternFeatures/RectangularPatternFeatures_Item.md)

## Derived Classes

[RectangularPatternFeatureProxy](../RectangularPatternFeatureProxy/RectangularPatternFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Pattern Feature with PatternBoundarySetting Sample](../../sample-programs/CreatePatternBoundarySettingSample_Sample.md) | This sample demonstrates how to create a rectangular pattern feature with boundary settings. |

## Version

Introduced in version 5
