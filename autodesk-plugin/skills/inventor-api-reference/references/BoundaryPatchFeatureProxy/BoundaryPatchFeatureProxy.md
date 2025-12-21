# BoundaryPatchFeatureProxy Object

Derived from: [BoundaryPatchFeature](../BoundaryPatchFeature/BoundaryPatchFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Definition.md) | Property that returns the BoundaryPatchDefinition object which defines the various input used to create the boundary patch feature. |
| [ExtendedName](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../BoundaryPatchFeatureProxy/BoundaryPatchFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
