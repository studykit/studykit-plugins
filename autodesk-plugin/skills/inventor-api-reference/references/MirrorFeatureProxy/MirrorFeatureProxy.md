# MirrorFeatureProxy Object

Derived from: [MirrorFeature](../MirrorFeature/MirrorFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../MirrorFeatureProxy/MirrorFeatureProxy_AddParticipant.md) | Add the specified occurrence from the list of participants for this feature. This method only applies to assembly features. |
| [Delete](../MirrorFeatureProxy/MirrorFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../MirrorFeatureProxy/MirrorFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../MirrorFeatureProxy/MirrorFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../MirrorFeatureProxy/MirrorFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../MirrorFeatureProxy/MirrorFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../MirrorFeatureProxy/MirrorFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../MirrorFeatureProxy/MirrorFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../MirrorFeatureProxy/MirrorFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../MirrorFeatureProxy/MirrorFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../MirrorFeatureProxy/MirrorFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../MirrorFeatureProxy/MirrorFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../MirrorFeatureProxy/MirrorFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../MirrorFeatureProxy/MirrorFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../MirrorFeatureProxy/MirrorFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../MirrorFeatureProxy/MirrorFeatureProxy_Definition.md) | Read-write property that gets and sets the MirrorFeatureDefinition object associated with this feature. |
| [ExtendedName](../MirrorFeatureProxy/MirrorFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../MirrorFeatureProxy/MirrorFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../MirrorFeatureProxy/MirrorFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../MirrorFeatureProxy/MirrorFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../MirrorFeatureProxy/MirrorFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../MirrorFeatureProxy/MirrorFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../MirrorFeatureProxy/MirrorFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../MirrorFeatureProxy/MirrorFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../MirrorFeatureProxy/MirrorFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../MirrorFeatureProxy/MirrorFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../MirrorFeatureProxy/MirrorFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [PatternElements](../MirrorFeatureProxy/MirrorFeatureProxy_PatternElements.md) | Gets the FeaturePatternElements collection that contains the elements created by this pattern. |
| [RangeBox](../MirrorFeatureProxy/MirrorFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [ResultFeatures](../MirrorFeatureProxy/MirrorFeatureProxy_ResultFeatures.md) | Property that returns the features that were created for this mirror. These can be work planes, work axes, work points and work surfaces. |
| [Shared](../MirrorFeatureProxy/MirrorFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../MirrorFeatureProxy/MirrorFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../MirrorFeatureProxy/MirrorFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [SurfacesOpaque](../MirrorFeatureProxy/MirrorFeatureProxy_SurfacesOpaque.md) | Gets and sets whether all the resulting surfaces are opaque or transparent. |
| [SurfacesVisible](../MirrorFeatureProxy/MirrorFeatureProxy_SurfacesVisible.md) | Gets and sets whether all the resulting surfaces are visible or not. |
| [Type](../MirrorFeatureProxy/MirrorFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |