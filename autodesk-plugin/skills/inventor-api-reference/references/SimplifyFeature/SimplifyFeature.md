# SimplifyFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

Part Simplify Feature Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../SimplifyFeature/SimplifyFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../SimplifyFeature/SimplifyFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../SimplifyFeature/SimplifyFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../SimplifyFeature/SimplifyFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../SimplifyFeature/SimplifyFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../SimplifyFeature/SimplifyFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../SimplifyFeature/SimplifyFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../SimplifyFeature/SimplifyFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../SimplifyFeature/SimplifyFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../SimplifyFeature/SimplifyFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../SimplifyFeature/SimplifyFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SimplifyFeature/SimplifyFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../SimplifyFeature/SimplifyFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../SimplifyFeature/SimplifyFeature_Definition.md) | Property that gets and sets the SimplifyDefinition object associated with this simplify feature. |
| [ExtendedName](../SimplifyFeature/SimplifyFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../SimplifyFeature/SimplifyFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../SimplifyFeature/SimplifyFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../SimplifyFeature/SimplifyFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../SimplifyFeature/SimplifyFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../SimplifyFeature/SimplifyFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../SimplifyFeature/SimplifyFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../SimplifyFeature/SimplifyFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../SimplifyFeature/SimplifyFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../SimplifyFeature/SimplifyFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../SimplifyFeature/SimplifyFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../SimplifyFeature/SimplifyFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../SimplifyFeature/SimplifyFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../SimplifyFeature/SimplifyFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../SimplifyFeature/SimplifyFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SimplifyDefinition.Parent](../SimplifyDefinition/SimplifyDefinition_Parent.md), [SimplifyFeatureProxy.NativeObject](../SimplifyFeatureProxy/SimplifyFeatureProxy_NativeObject.md), [SimplifyFeatures.Add](../SimplifyFeatures/SimplifyFeatures_Add.md), [SimplifyFeatures.Item](../SimplifyFeatures/SimplifyFeatures_Item.md)

## Derived Classes

[SimplifyFeatureProxy](../SimplifyFeatureProxy/SimplifyFeatureProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Part SimplifyFeature Sample](../../sample-programs/PartSimplifyFeatureSample_Sample.md) | This sample demonstrates how to create a simplify feature in part document. |

## Version

Introduced in version 2026

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |