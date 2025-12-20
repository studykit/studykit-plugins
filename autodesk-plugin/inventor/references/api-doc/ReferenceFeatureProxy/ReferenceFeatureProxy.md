# ReferenceFeatureProxy Object

Derived from: [ReferenceFeature](../ReferenceFeature/ReferenceFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ReferenceFeatureProxy/ReferenceFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ReferenceFeatureProxy/ReferenceFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ReferenceFeatureProxy/ReferenceFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ReferenceFeatureProxy/ReferenceFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ReferenceFeatureProxy/ReferenceFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ReferenceFeatureProxy/ReferenceFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ReferenceFeatureProxy/ReferenceFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ReferenceFeatureProxy/ReferenceFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ReferenceFeatureProxy/ReferenceFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ReferenceFeatureProxy/ReferenceFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ReferenceFeatureProxy/ReferenceFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ReferenceFeatureProxy/ReferenceFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ReferenceFeatureProxy/ReferenceFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../ReferenceFeatureProxy/ReferenceFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../ReferenceFeatureProxy/ReferenceFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ReferenceFeatureProxy/ReferenceFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ReferenceFeatureProxy/ReferenceFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ReferenceFeatureProxy/ReferenceFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ReferenceFeatureProxy/ReferenceFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ReferenceFeatureProxy/ReferenceFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../ReferenceFeatureProxy/ReferenceFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../ReferenceFeatureProxy/ReferenceFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ReferenceFeatureProxy/ReferenceFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ReferenceFeatureProxy/ReferenceFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ReferenceFeatureProxy/ReferenceFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ReferenceFeatureProxy/ReferenceFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ReferenceComponent](../ReferenceFeatureProxy/ReferenceFeatureProxy_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../ReferenceFeatureProxy/ReferenceFeatureProxy_ReferencedEntity.md) | Property that returns the entity in the base part or assembly document. In the case of a derived assembly, the ReferencedEntity property returns the component occurrence in the base assembly that this ReferenceFeature represents. In the case of a derived part, the ReferencedEntity property can return a solid or surface body of the source part or a surface in the source part.. In cases where the component occurrence, solid or surface body entity is referencing a model entity, but the model entity no longer exists because it has been consumed by a subsequent modeling operation, this property will return Nothing. |
| [Shared](../ReferenceFeatureProxy/ReferenceFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ReferenceFeatureProxy/ReferenceFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ReferenceFeatureProxy/ReferenceFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ReferenceFeatureProxy/ReferenceFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |