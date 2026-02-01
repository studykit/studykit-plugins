# iFeature Object

Derived from: [ReferenceFeature](../ReferenceFeature/ReferenceFeature.md) Object

## Description

The iFeature object represents the instance of a placed iFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iFeature/iFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../iFeature/iFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../iFeature/iFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../iFeature/iFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../iFeature/iFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../iFeature/iFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../iFeature/iFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../iFeature/iFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../iFeature/iFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../iFeature/iFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../iFeature/iFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../iFeature/iFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../iFeature/iFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ExtendedName](../iFeature/iFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../iFeature/iFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../iFeature/iFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../iFeature/iFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iFeatureDefinition](../iFeature/iFeature_iFeatureDefinition.md) | Property that returns the associated iFeatureDefinition. |
| [iFeatureTemplateDescriptor](../iFeature/iFeature_iFeatureTemplateDescriptor.md) | Property that returns the iFeatureTemplateDescriptor object associated with this iFeature. |
| [IsOwnedByFeature](../iFeature/iFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../iFeature/iFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../iFeature/iFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../iFeature/iFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../iFeature/iFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../iFeature/iFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../iFeature/iFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ReferenceComponent](../iFeature/iFeature_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../iFeature/iFeature_ReferencedEntity.md) | Property that returns the entity in the base part or assembly document. In the case of a derived assembly, the ReferencedEntity property returns the component occurrence in the base assembly that this ReferenceFeature represents. In the case of a derived part, the ReferencedEntity property can return a solid or surface body of the source part or a surface in the source part.. In cases where the component occurrence, solid or surface body entity is referencing a model entity, but the model entity no longer exists because it has been consumed by a subsequent modeling operation, this property will return Nothing. |
| [Shared](../iFeature/iFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Sketches](../iFeature/iFeature_Sketches.md) | Property that returns the sketches that were created when the iFeature was placed. In most case there will be a single sketch. |
| [Suppressed](../iFeature/iFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../iFeature/iFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../iFeature/iFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeatureProxy.NativeObject](../iFeatureProxy/iFeatureProxy_NativeObject.md), [iFeatures.Add](../iFeatures/iFeatures_Add.md), [iFeatures.Item](../iFeatures/iFeatures_Item.md)

## Derived Classes

[iFeatureProxy](../iFeatureProxy/iFeatureProxy.md)

## Version

Introduced in version 2009
