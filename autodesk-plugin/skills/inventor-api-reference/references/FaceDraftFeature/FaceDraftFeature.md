# FaceDraftFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The FaceDraftFeature object represents a face draft on a part..

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../FaceDraftFeature/FaceDraftFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../FaceDraftFeature/FaceDraftFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../FaceDraftFeature/FaceDraftFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../FaceDraftFeature/FaceDraftFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../FaceDraftFeature/FaceDraftFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../FaceDraftFeature/FaceDraftFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../FaceDraftFeature/FaceDraftFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../FaceDraftFeature/FaceDraftFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../FaceDraftFeature/FaceDraftFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../FaceDraftFeature/FaceDraftFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../FaceDraftFeature/FaceDraftFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FaceDraftFeature/FaceDraftFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../FaceDraftFeature/FaceDraftFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../FaceDraftFeature/FaceDraftFeature_Definition.md) | Read-write property that gets and sets the FaceDraftDefinition object associated with this feature. |
| [ExtendedName](../FaceDraftFeature/FaceDraftFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../FaceDraftFeature/FaceDraftFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../FaceDraftFeature/FaceDraftFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../FaceDraftFeature/FaceDraftFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../FaceDraftFeature/FaceDraftFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../FaceDraftFeature/FaceDraftFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../FaceDraftFeature/FaceDraftFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../FaceDraftFeature/FaceDraftFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../FaceDraftFeature/FaceDraftFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../FaceDraftFeature/FaceDraftFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../FaceDraftFeature/FaceDraftFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../FaceDraftFeature/FaceDraftFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../FaceDraftFeature/FaceDraftFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../FaceDraftFeature/FaceDraftFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../FaceDraftFeature/FaceDraftFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[FaceDraftDefinition.Parent](../FaceDraftDefinition/FaceDraftDefinition_Parent.md), [FaceDraftFeatureProxy.NativeObject](../FaceDraftFeatureProxy/FaceDraftFeatureProxy_NativeObject.md), [FaceDraftFeatures.Add](../FaceDraftFeatures/FaceDraftFeatures_Add.md), [FaceDraftFeatures.Item](../FaceDraftFeatures/FaceDraftFeatures_Item.md)

## Derived Classes

[FaceDraftFeatureProxy](../FaceDraftFeatureProxy/FaceDraftFeatureProxy.md)

## Version

Introduced in version 5
