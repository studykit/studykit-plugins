# ReferenceFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The ReferenceFeature object currently supports all of the methods and properties of the base PartFeature class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ReferenceFeature/ReferenceFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ReferenceFeature/ReferenceFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ReferenceFeature/ReferenceFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ReferenceFeature/ReferenceFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ReferenceFeature/ReferenceFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ReferenceFeature/ReferenceFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ReferenceFeature/ReferenceFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ReferenceFeature/ReferenceFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ReferenceFeature/ReferenceFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ReferenceFeature/ReferenceFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ReferenceFeature/ReferenceFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ReferenceFeature/ReferenceFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ReferenceFeature/ReferenceFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../ReferenceFeature/ReferenceFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ReferenceFeature/ReferenceFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ReferenceFeature/ReferenceFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ReferenceFeature/ReferenceFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ReferenceFeature/ReferenceFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ReferenceFeature/ReferenceFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ReferenceFeature/ReferenceFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ReferenceFeature/ReferenceFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ReferenceFeature/ReferenceFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ReferenceFeature/ReferenceFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ReferenceFeature/ReferenceFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ReferenceComponent](../ReferenceFeature/ReferenceFeature_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../ReferenceFeature/ReferenceFeature_ReferencedEntity.md) | Property that returns the entity in the base part or assembly document. In the case of a derived assembly, the ReferencedEntity property returns the component occurrence in the base assembly that this ReferenceFeature represents. In the case of a derived part, the ReferencedEntity property can return a solid or surface body of the source part or a surface in the source part.. In cases where the component occurrence, solid or surface body entity is referencing a model entity, but the model entity no longer exists because it has been consumed by a subsequent modeling operation, this property will return Nothing. |
| [Shared](../ReferenceFeature/ReferenceFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ReferenceFeature/ReferenceFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ReferenceFeature/ReferenceFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ReferenceFeature/ReferenceFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iPartMember.PrimaryBody](../iPartMember/iPartMember_PrimaryBody.md), [ReferenceFeatureProxy.NativeObject](../ReferenceFeatureProxy/ReferenceFeatureProxy_NativeObject.md), [ReferenceFeatures.Item](../ReferenceFeatures/ReferenceFeatures_Item.md), [ReferenceFeaturesEnumerator.Item](../ReferenceFeaturesEnumerator/ReferenceFeaturesEnumerator_Item.md)

## Derived Classes

[iFeature](../iFeature/iFeature.md), [ReferenceFeatureProxy](../ReferenceFeatureProxy/ReferenceFeatureProxy.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |